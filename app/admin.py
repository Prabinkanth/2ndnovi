from django.contrib import admin
from .models import BinaryTree,Parent

# Register your models here.
@admin.register(BinaryTree)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','parent_id']



@admin.register(Parent)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','Name']