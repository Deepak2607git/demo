from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, phone_number,username):
        email = self.normalize_email(email)
        user = self.model(email=email,phone_number = phone_number,username = username)
        user.set_password(password)
        user.save()
        return user

