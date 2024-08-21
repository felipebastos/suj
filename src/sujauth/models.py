from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

CAMPI = (
    ('ara', 'Aracati'),
    ('for', 'Fortaleza'),
    ('ndf', 'Não definido'),
)

class User(AbstractUser):
    campus = models.CharField(max_length=3, choices=CAMPI, default=CAMPI[2][0])

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['campus', 'username']
    USERNAME_FIELD = 'email'

