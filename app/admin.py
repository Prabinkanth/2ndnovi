from django.contrib import admin
from .models import BinaryTree,parrent

# Register your models here.
@admin.register(BinaryTree)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','parent_id']



@admin.register(parrent)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','Name']