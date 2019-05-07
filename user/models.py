# from django.contrib.postgres.fields import ArrayField

from utilities.constants import HIDE_LAST, LANGUAGES, RUSSIAN
from utilities.image_utilities import get_url
from utilities.upload import avatar_upload

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# from utils import mobizonproxy


# Create your models here.
class MainUserManager(BaseUserManager):
    """
    Custom user manager.
    """
    
    def create_user(self, phone, password):
        """
        Creates and saves a User with the given phone and password
        """
        if not phone or not password:
            raise ValueError('Users must have an phone and password')
        
        user = self.model(phone=phone.lower())
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password):
        """
        Creates and saves a superuser with the given phone and password
        """
        user = self.create_user(phone=phone,
                                password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MainUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with phone and email.
    """
    phone = models.CharField(max_length=200, blank=True, null=True, unique=True, db_index=True)
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True, null=True, unique=True, db_index=True)
    language = models.IntegerField(choices=LANGUAGES, default=RUSSIAN)
    
    avatar = models.ImageField(upload_to=avatar_upload, blank=True, null=True)
    avatar_big = models.ImageField(upload_to=avatar_upload, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    
    #   for one signal notifications
    # player_ids = ArrayField(models.CharField(max_length=255, blank=True, null=True, default=""), default=list)
    
    objects = MainUserManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.phone
    
    def __unicode__(self):
        return self.phone
    
    def __str__(self):
        return self.phone or self.email
        # or self.vk_id or self.fb_id or self.insta_id
    
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_admin
    
    def json(self, short=False, user=None):
        if not short:
            result = {
                "user_id": self.pk,
                "phone": self.hidden_phone(user),
                "name": self.name,
                "email": self.hidden_email(user),
                "avatar": get_url(self.avatar),
                "avatar_big": get_url(self.avatar_big) or get_url(self.avatar),
                # "languages": [l.name for l in self.languages.all()],
                "language_id": self.language,
                "language": self.get_language_display(),
                "verified": self.verified(),
            }
        else:
            result = {
                "user_id": self.pk,
                "phone": self.hidden_phone(user),
                "email": self.hidden_email(user),
                "name": self.name,
                "avatar": get_url(self.avatar),
            }
        return result
    
    def owner_json(self, short=False):
        if not short:
            result = {
                "user_id": self.pk,
                "phone": self.phone,
                "name": self.name,
                "email": self.email,
                "avatar": get_url(self.avatar),
                "avatar_big": get_url(self.avatar_big) or get_url(self.avatar),
                # "languages": [l.name for l in self.languages.all()],
                "language_id": self.language,
                "language": self.get_language_display(),
                "verified": self.verified(),
            }
        else:
            result = {
                "user_id": self.pk,
                "phone": self.phone,
                "email": self.email,
                "name": self.name,
                "avatar": get_url(self.avatar),
            }
        return result
    
    def hidden_email(self, user=None):
        if self.email and user != self:
            return '*' * len(self.email)
        return self.email or None
    
    def hidden_phone(self, user=None):
        if self.phone and user != self:
            return self.phone[:(len(self.phone) - HIDE_LAST)] + '*' * HIDE_LAST
        return self.phone or None
    
    def verified(self):
        email = False
        if self.email:
            email = True
        
        phone = False
        if self.phone:
            phone = True
        
        return {
            "phone": phone,
            "email": email,
        }
    
    # def set_social_id(self, social_type, social_id):
    #     if social_type == "facebook" and not self.fb_id:
    #         self.fb_id = social_id
    #         self.save()
    #     elif social_type == "vk" and not self.vk_id:
    #         self.vk_id = social_id
    #         self.save()
    #     elif social_type == "insta" and not self.insta_id:
    #         self.insta_id = social_id
    #         self.save()
    #     elif social_type == "google" and not self.email:
    #         self.email = social_id
    #         self.save()
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    # def save(self, *args, **kwargs):
    #     if self.contact_number is None and self.phone:
    #         self.contact_number = self.phone
    #     super(MainUser, self).save(*args, **kwargs)
