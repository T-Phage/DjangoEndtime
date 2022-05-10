from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        verbose_name='username',
        max_length=100,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True,
    )
    firstname = models.CharField(
        verbose_name='firstname',
        max_length=100,
    )
    surname = models.CharField(
        verbose_name='lastname',
        max_length=100,
    )
    othername = models.CharField(
        verbose_name='othernames',
        max_length=100,
        blank=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_full_name(self):
        # The user is identified by their email address
        return self.firstname + " " + self.surname

    class Meta:
        verbose_name_plural = 'Users'

class Eschatology(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    content = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Eschatology'

    def __str__(self):
        return self.title

class Devotionals(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    prayer = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Devotionals'

    def __str__(self):
        return self.title

class Sermons(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    content = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Sermons'

    def __str__(self):
        return self.title
