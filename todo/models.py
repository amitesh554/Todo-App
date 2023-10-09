from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=1000)
    created=models.DateField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-updated','-created']


    def __str__(self):
        return self.title
