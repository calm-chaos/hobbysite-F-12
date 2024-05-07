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

    ctx = {
        "commission_detail": commission_detail,
        "job_detail": job_detail,
        "total_manpower_required": total_manpower_required,
        "author_of_commission": commission_detail.author,
        "total_available_manpower": total_available_manpower,
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
def commission_jobapplication(request):

    jobapplication_form = JobApplicationForm(request.POST or None)
    if request.method == "POST":
        if jobapplication_form.is_valid():
            applyingjob = jobapplication_form.save(commit=False)
            applyingjob.applicant = request.user.profile
            applyingjob.save()

    ctx = {
        "jobapplication_form":jobapplication_form,
    }

    return render(request, "commission_jobapplication.html", ctx)
