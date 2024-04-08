from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email,username, first_name,last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, first_name,last_name,password=None,):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user