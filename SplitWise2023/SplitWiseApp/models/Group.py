from django.db import models
from .BaseModel import BaseModel
from .User import User


class Group(BaseModel):
    name = models.CharField(max_length=255)
    # GROUP   : USERS
    #   M     :  M  --> MANY TO MANY RELATIONSHIP

    # EACH GROUP WILL HAVE EXPENSES
    # ONE GROUP CAN HAVE MULTIPLE EXPENSES
    # AN EXPENSE CANNOT BELONG TO MULTIPLE GROUPS
    # ONE TO MANY RELATIONSHIP  -> IN EXPENSE WE CAN JUST WRITE GROUP
    # WE ARE SUPPOSE TO HAVE A THIRD TABLE (MAPPING TABLE)

    participants = models.ManyToManyField(User, related_name="group_participants")
    admins = models.ManyToManyField(User, related_name="group_admins")
    # 1 to M RELATIONSHIP WITH EXPENSES
    description = models.CharField(max_length=255, default=" ")





