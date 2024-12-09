from django.shortcuts import render, redirect, get_object_or_404    
from .forms import OfficeAmenitiesForm,CompanyForm,RoleRequestForm
from .models import Company
def create_office_amenity(request):
    if request.method == 'POST':
        form = OfficeAmenitiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('amenities_list')  
    else:
        form = OfficeAmenitiesForm()
    return render(request, 'create_office_amenity.html', {'form': form})

def request_role(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    
    # Check if the user is already associated with the company before requesting a role
    if not request.user.company == company:
        return redirect('apply_for_company')  # Redirect if user is not associated with the company
    
    if request.method == 'POST':
        form = RoleRequestForm(request.POST)
        if form.is_valid():
            role_request = form.save(commit=False)
            role_request.user = request.user  # Automatically associate the logged-in user
            role_request.save()
            return redirect('role_request_success')  # Redirect to a success page
    else:
        form = RoleRequestForm(initial={'company': company})
    
    return render(request, 'request_role.html', {'form': form, 'company': company})


def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()  # Company is created
            return redirect('role_request', company_id=company.id)  # Redirect to the role request form
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {'form': form})