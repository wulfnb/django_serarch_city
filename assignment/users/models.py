# from django.contrib.auth.models import AbstractUser
from django.db import models


# class CustomUser(AbstractUser):
#     password = None
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     gender = models.CharField(max_length=1)
#     phone = models.CharField(max_length=15)
#     REQUIRED_FIELDS = ['email','first_name', 'last_name' , 'gender', 'phone']

#     def __str__(self):
#         return self.email

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, phone):
        if not email:
            raise ValueError('Users must have an email address')
        if not phone:
            raise ValueError('Users must have a phone')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )

        # user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone):
        user = self.create_user(
            email=self.normalize_email(email),
            phone=phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    password = None
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    gender          = models.CharField(max_length=1)
    phone           = models.CharField(max_length=15,unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True,null=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    class Meta:
        db_table = "user"
        

    objects = MyUserManager()

    def __str__(self):
        return '<' + str(self.email) +'>'

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Otp(models.Model):
    email = models.EmailField(verbose_name="email", max_length=60)
    otp = models.IntegerField()

    def __str__(self):
        return '<' + str(self.email) + ' ' + str(self.otp) +'>'