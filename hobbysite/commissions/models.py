from django.db import models
from django.urls import reverse

from user_management.models import Profile

status_open = "a"
status_full = "b"
status_completed = "c"
status_discontinued = "d"
status_pending = "a"
status_accepted = "b"
status_rejected = "c"

status_choices_commission = {
    status_open: "Open",
    status_full: "Full",
    status_completed: "Completed",
    status_discontinued: "Discontinued",
}

status_choices_job= {
    status_open: "Open",
    status_full: "Full",
}

status_choices_jobapplication = {
    status_pending: "Pending",
    status_accepted: "Accepted",
    status_rejected: "Rejected",
}

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    status = models.CharField(
        max_length=255, choices=status_choices_commission, default=status_choices_commission[status_open],
    )

    def get_status(self):
        return status_choices_commission[self.status]

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='authored_commission' 
     )

    class Meta:
        ordering = ['status','-created_on'] #order by created on ascending order

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_detail', args=[self.pk])

class Job(models.Model):
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()
        
    status = models.CharField(
        max_length=255, choices=status_choices_job, default=status_choices_job[status_open]
    )

    def get_status(self):
        return status_choices_job[self.status]
    
    def accepted_applicants(self):
        return self.jobapplication.filter(status=status_accepted).count()

    commission = models.ForeignKey(
        'Commission', 
        on_delete=models.CASCADE, 
        null=True, blank=True,
        related_name='job' 
     )

    class Meta:
        ordering = [
            'status',  # Sort by status (Open > Full)
            '-manpower_required',  # Then by manpower_required in descending order
            'role'  # Then by role in ascending order
        ]
    
    def __str__(self):
        return self.role


class JobApplication(models.Model):

    job = models.ForeignKey(
        'Job', 
        on_delete=models.CASCADE, 
        related_name='jobapplication' 
     )    
        
    applicant = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='applicantprofile' 
     )
    
    status = models.CharField(
        max_length=255, choices=status_choices_jobapplication, default=status_choices_jobapplication[status_pending]
    )   
    
    applied_on = models.DateTimeField(auto_now_add=True)

    def get_status(self):
        return status_choices_jobapplication[self.status]

    class Meta:
         ordering = ['status','-applied_on'] #order by applied on descending order