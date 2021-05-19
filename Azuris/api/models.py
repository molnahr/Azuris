from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('User must have an email adress')
        if not username:
            raise ValueError('User must have username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username = username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    data_joined = models.DateTimeField(verbose_name='data joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    spellA = models.IntegerField(default=0)
    spellB = models.IntegerField(default=0)
    spellC = models.IntegerField(default=0)

    #By default Django usermodel use the field USERNAME to log in... the username is the key, but we ave to login with email.
    #https://www.youtube.com/watch?v=Wq6JqXqOzCE&list=PLgCYzUzKIBE9Pi8wtx8g55fExDAPXBsbV&index=7
    #15:28...
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser




x = settings.AUTH_USER_MODEL
# # #If a user registre to the server a token will be generated
@receiver(post_save,sender=x)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)


class Spell(models.Model):
    id = models.IntegerField(primary_key=True)
    type_spell = models.CharField(max_length=30,unique=False)
    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=3000)
    power = models.IntegerField()
    evasion_rate = models.IntegerField()
    level_requirement = models.IntegerField(default=1)
    cooldown = models.IntegerField()
    file = models.TextField(default=1)
    position = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name[:50]

class Mob(models.Model):
    name = models.CharField(max_length=30,unique=True)
    level = models.IntegerField(default=1)
    hp = models.IntegerField(default=1)
    dmg = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name[:50]