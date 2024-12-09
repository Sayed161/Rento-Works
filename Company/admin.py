from django.contrib import admin
from django.utils import timezone
from .models import RoleRequest,Company,CompanyImage,OfficeAmenities
# Register your models here.
admin.site.register(CompanyImage)
admin.site.register(OfficeAmenities)
admin.site.register(Company)

class RoleRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'requested_role', 'status', 'reviewed_at')
    list_filter = ('status', 'company')
    search_fields = ('user__username', 'company__name')
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        print('queryset', queryset)
        queryset.update(status='Approve', reviewed_at=timezone.now())
        queryset.save()
    def reject_requests(self, request, queryset):
        queryset.update(status='reject', reviewed_at=timezone.now())
        queryset.save()
admin.site.register(RoleRequest, RoleRequestAdmin)