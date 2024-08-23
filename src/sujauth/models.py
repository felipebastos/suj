from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

CAMPI = (
    ('ndf', 'Não definido'),
    ('ara', 'Aracati'),
    ('for', 'Fortaleza'),
)

class User(AbstractUser):
    campus = models.CharField(max_length=3, choices=CAMPI, default=CAMPI[0][0])

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['campus', 'username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

