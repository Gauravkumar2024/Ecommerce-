from django.db import models
import uuid

class baseModel(models.Model):
    id= id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    # use this we create a unique id everytime
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
