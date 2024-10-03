from django.contrib.auth.models import User
User.objects.create_user(username='testuser', email='test@example.com', password='password')