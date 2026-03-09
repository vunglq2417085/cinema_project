from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None,**extra_field):
        if not phone_number:
            raise ValueError('số điện thoại là bắt buộc')
        user = self.model(phone_number = phone_number, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, phone_number, password=None, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active',True)
        if extra_field.get('is_staff') is not True:
            raise ValueError('Superuser phải có is_staff=True')
        return self.create_user(phone_number,password, **extra_field)
class User(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(max_length=10, unique = True,db_index=True, verbose_name="số điện thoại")
    full_name = models.CharField(max_length = 50,verbose_name = "họ và tên (Nhập đúng trên căn cước!)" )
    identity_card = models.CharField(unique=True,null=True, blank=True,max_length= 12, verbose_name = "Số Căn Cước Công Dân")
    is_verified = models.BooleanField(default= False, verbose_name= "Đã xác minh")
    role_choices = (
        ('CUSTOMER', 'khách hàng'),
        ('STAFF','nhân viên'),
        ('ADMIN','Quản trị viên'),
    )
    role = models.CharField(max_length=10,choices=role_choices, default='CUSTOMER')
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS =['full_name']
    objects = UserManager()
    def __str__(self):
        return f"{self.full_name}"