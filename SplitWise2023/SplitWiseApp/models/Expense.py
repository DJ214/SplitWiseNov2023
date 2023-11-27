from django.db import models
from .BaseModel import BaseModel
from .User import User
from .Group import Group


class Expense(BaseModel):
    amount = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='create_group')
    # expense : user
    #    M    :  1
    created_by = models.ForeignKey(to='User', on_delete=models.PROTECT, related_name='create')
    description = models.CharField(max_length=255, default=" ")
    created_at = models.DateTimeField()
    participants = models.ManyToManyField(User)
