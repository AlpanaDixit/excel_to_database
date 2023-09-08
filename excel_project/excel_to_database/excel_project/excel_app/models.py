from django.db import models



class GenBankBranch(models.Model):
    
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True)
    
    def __str__(self):
        return self.name