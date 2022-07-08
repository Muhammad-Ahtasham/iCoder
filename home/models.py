import email
from operator import mod
from pickle import TRUE
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateField(auto_now_add=TRUE, blank=True)

    def __str__(self):
        return self.name + " - " + self.email