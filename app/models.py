from django.db import models


# Create your models here.
class BinaryTree(models.Model):
    name = models.CharField(max_length=200)
    parent_id = models.ForeignKey('Parent', null=True, blank=True, on_delete=models.DO_NOTHING, )
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('parent_id', 'position')


class Parent(models.Model):
    Name = models.OneToOneField(BinaryTree, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)