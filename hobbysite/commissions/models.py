from django.db import models
from django.urls import reverse

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on'] #order by created on ascending order


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_detail', args=[self.pk])

class Comment(models.Model):
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    commission = models.ForeignKey(
        'Commission', 
        on_delete=models.CASCADE, 
        related_name='comment' 
    )

    class Meta:
        ordering = ['-created_on'] #order by created on descending order