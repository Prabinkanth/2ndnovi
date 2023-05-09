from django.db import models

# Create your models here.
class BinaryTree(models.Model):
    name = models.CharField(max_length=200)
    parent_id = models.CharField(max_length=200)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name', 'parent_id', 'position')

class parrent(models.Model):
    Name = models.OneToOneField(BinaryTree,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name