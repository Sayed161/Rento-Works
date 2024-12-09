from django import forms
from .models import OfficeAmenities,Company,CompanyImage,RoleRequest

class OfficeAmenitiesForm(forms.ModelForm):
    class Meta:
        model = OfficeAmenities
        fields = ['amenity', 'image']

class RoleRequestForm(forms.ModelForm):
    class Meta:
        model = RoleRequest
        fields = ['company', 'requested_role']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'Location', 'Company_number', 'About', 'website', 'company_mail','amenites']

class OfficeAmenitiesForm(forms.ModelForm):
    class Meta:
        model = OfficeAmenities
        fields = ['amenity', 'image']