from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'full_name', 'role', 'is_staff', 'is_verified')
    search_fields = ('phone_number', 'full_name', 'identity_card')
    
    # Quan trọng: Chỉ liệt kê các trường thực sự có trong models.py
    fields = (
        'phone_number', 'password', 'full_name', 'identity_card', 
        'role', 'is_verified', 'is_staff', 'is_superuser', 
        'is_active', 'groups', 'user_permissions'
    )
    
    # Hàm này bắt buộc để mật khẩu được mã hóa trước khi lưu vào DB
    def save_model(self, request, obj, form, change):
        if 'password' in form.cleaned_data:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)