from django.db import models
import random
import string

# Create your models here.
# mdoel == table

def genetate_unique_code():
    max_len = 6 
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=max_len))
        if Room.objects.filter(code=code).count() == O:
            break
    return code         
    
class Room(models.Model):
    code = models.CharField(max_length=8, default= "", unique=True)
    host = models.CharField(max_length = 50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False,default=1)
    created_at = models.DateTimeField(auto_now_add =True)