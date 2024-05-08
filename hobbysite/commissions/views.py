from django.shortcuts import get_object_or_404, redirect, render

from commissions.models import *
from django.db.models import Sum

from .forms import *

from django.contrib.auth.decorators import login_required


def commission_list(request):

    commission_list = Commission.objects.all()

    if request.user.is_authenticated:
        user_commissions = Commission.objects.filter(author=request.user.profile)
        applied_commissions = Commission.objects.filter(job__jobapplication__applicant=request.user.profile).distinct()
        
        ctx = {
            "logged_user": request.user.profile,
            "user_commissions": user_commissions,
            "commission_list": commission_list,
            "applied_commissions": applied_commissions,
        }
    else:

        ctx = {
            "commission_list": commission_list,

        }
            
    return render(request, "commission_list.html", ctx)


def commission_detail(request, pk):
    commission_detail = Commission.objects.get(pk=pk)
    job_detail = Job.objects.filter(commission_id=pk)

    total_manpower_required = Job.objects.filter(commission_id=pk).aggregate(total = Sum("manpower_required"))
    total_manpower_required_value = total_manpower_required.get("total", 0)

    total_accepted_applicants = 0
    for job in job_detail:
        total_accepted_applicants += job.accepted_applicants()
    
    total_available_manpower = total_manpower_required_value - total_accepted_applicants

    if request.user.is_authenticated:
        job_apply = JobApplicationForm(
            initial={
                "job": Job.objects.get(pk=1),
                "applicant": Profile.objects.get(pk=request.user.pk),
                "status": "Pending",
            }
        )

        if request.method == "POST":
            job_apply = JobApplicationForm(request.POST)
            if job_apply.is_valid():
                new_application = JobApplication()
                job_id = int(request.POST.get("job-pk"))
                new_application.job = Job.objects.get(pk=job_id)
                new_application.applicant = Profile.objects.get(pk=request.user.pk)
                new_application.status = "Pending"
                new_application.save()
                return redirect("commissions:list")   
            
    ctx = {
        "commission_detail": commission_detail,
        "job_detail": job_detail,
        "total_manpower_required": total_manpower_required,
        "author_of_commission": commission_detail.author,
        "total_available_manpower": total_available_manpower,
        "job_apply": job_apply,
        }
    
    return render(request, "commission_detail.html", ctx)

@login_required
def commission_create(request):
    create_commission_form = CommissionForm()
    add_job_form = JobForm()

    if request.method == "POST":
        create_commission_form = CommissionForm(request.POST)
        add_job_form = JobForm(request.POST)
        if create_commission_form.is_valid() and add_job_form.is_valid():
            createcommission = create_commission_form.save(commit=False)
            createcommission.author = request.user.profile
            createcommission.save()

            addjob = add_job_form.save(commit=False)   
            addjob.commission = createcommission
            addjob.save()   
            return redirect("commissions:list")   
    
    ctx = {
        "create_commission_form":create_commission_form,
        "add_job_form":add_job_form,
    }
    
    return render(request, "commission_create.html", ctx)

@login_required
def commission_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    commission_update_form = CommissionUpdateForm(request.POST or None, request.FILES, instance = commission)
    if request.method == "POST":
        if commission_update_form.is_valid:
            commission_update_form.save()
            return redirect("commissions:commission_detail", pk=pk)
    
    ctx = {
        "commission_update_form":commission_update_form,
        "commission":commission,
    }

    return render(request, "commission_update.html", ctx)

@login_required
def commission_jobapplication(request, pk):
    job = get_object_or_404(Job, id=pk)
    applicant = request.user.profile
    selectable_jobs = Job.objects.exclude(status=status_accepted)

    JobApplication.objects.create(job=job, applicant=applicant, status=status_pending)

    jobapplication_form = JobApplicationForm(request.POST or None)
    if request.method == "POST":
        if jobapplication_form.is_valid():
            applyingjob = jobapplication_form.save(commit=False)
            applyingjob.applicant = request.user.profile
            applyingjob.save()

    ctx = {
        "jobapplication_form":jobapplication_form,
        "selectable_jobs": selectable_jobs,
    }

    return render(request, "commission_jobapplication.html", ctx)
