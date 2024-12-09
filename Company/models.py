from django.db import models
from django.utils import timezone

class Location(models.Model):
    name = models.CharField(max_length=255)
    embed_map_url = models.URLField(blank=True, null=True)  # Field to store the embedded map URL

    def __str__(self):
        return self.name


class OfficeAmenities(models.Model):
    amenity = models.CharField(max_length=255)
    image = models.ImageField(upload_to='amenites/', null=True, blank=True)
    def __str__(self):
        return f"{self.amenity}"
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    Location = models.ForeignKey(Location,on_delete=models.CASCADE)
    Company_number = models.CharField(max_length=11,null=True)
    About = models.TextField(blank=True)
    website = models.URLField(blank=True)
    company_mail = models.EmailField(null=True)
    ratings =models.IntegerField(null=True,default=0)
    amenites = models.ManyToManyField(OfficeAmenities)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CompanyImage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='company_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)







class RoleRequest(models.Model):
    COMPANY_ADMIN = 'company_admin'
    user = models.ForeignKey('Account.User', on_delete=models.CASCADE, related_name='role_requests')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='Company')
    requested_role = models.CharField(max_length=20, default=COMPANY_ADMIN)  
    STATUS_CHOICES = [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reviewed_at = models.DateTimeField(null=True, blank=True)

    def approve(self):
        self.user.role = self.requested_role
        self.user.company = self.company
        self.user.save()
        self.company.is_visible = True
        self.company.save()
        self.approved = True
        self.reviewed_at = timezone.now()
        self.save()

    def reject(self):
        self.approved = False
        self.reviewed_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.user} - {self.requested_role} for {self.company}"