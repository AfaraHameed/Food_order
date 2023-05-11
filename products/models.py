from django.db import models
import uuid
# Create your models here.
class Product(models.Model):
    uid=models.UUIDField(default=uuid.uuid4)