from users.models import User
try:
    user = User.objects.create_user(phone_number='0900000000', password='password123', full_name='Test User')
    print("TẠO USER THÀNH CÔNG!")
except Exception as e:
    print(f"LỖI TẠO USER: {e}")