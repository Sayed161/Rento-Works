from django.contrib.auth.models import AbstractUser, Group, Permission,BaseUserManager,PermissionsMixin
from django.db import models
from Company.models import Company


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser, PermissionsMixin):
    CUSTOMER = 'customer'
    COMPANY_ADMIN = 'company_admin'
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='admins',
        help_text="The company the user is associated with if they are an admin."
    )
    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (COMPANY_ADMIN, 'Company Admin'),
    ]
    
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER,
    )
    def is_customer(self):
        return self.role == self.CUSTOMER

    def is_company_admin(self):
        return self.role == self.COMPANY_ADMIN

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set", 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  
        blank=True
    )

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"