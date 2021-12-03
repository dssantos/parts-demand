from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have a email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField('Usuário', max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name_plural = 'Usuários'
        verbose_name = 'Usuário'

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name.split(" ")[0]

    def __str__(self):
        """Return string representation of our user"""
        return self.name


class DeliveryAddress(models.Model):
    """Delivery address model for parts demands"""

    local_description = models.CharField('Local', max_length=50)
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Anunciante'
    )
    postal_code = models.CharField(
        'CEP', 
        max_length=8, 
        validators=[MinLengthValidator(8)]
    )
    street = models.CharField('Rua', max_length=50)
    street_number = models.CharField('Número', max_length=10)
    complement = models.CharField(
        'Complemento', 
        max_length=50, 
        blank=True, 
        default=''
    )
    district = models.CharField('Bairro', max_length=50)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=50)
    country = models.CharField('País', max_length=50)


    class Meta:
        verbose_name_plural = 'endereços de entrega'
        verbose_name = 'endereço de entrega'

    def __str__(self):
        """Return string representation of delivery address"""
        return self.local_description


class PartsDemand(models.Model):
    """Parts demand model"""
    part_description = models.CharField('Descrição da peça', max_length=100)
    delivery_address = models.ForeignKey(
        DeliveryAddress, 
        on_delete=models.CASCADE, 
        verbose_name='Endereço de entrega')
    email = models.CharField('Email', max_length=50)
    phone = models.CharField('Telefone', max_length=11)
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name='Anunciante'
    )
    status = models.BooleanField('Status de finalização', default=False)


    class Meta:
        verbose_name_plural = 'demandas de peça'
        verbose_name = 'demanda de peça'

    def __str__(self):
        """Return string representation of part demand"""
        return self.part_description
