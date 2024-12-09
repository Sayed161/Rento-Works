from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.create_company, name='company'),
    path('role-request/<int:company_id>/', views.request_role, name='role_request'),
]
