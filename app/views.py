from django.shortcuts import render
from django.views import generic, View
from . forms import  CustomerProfileForm
from .models import *
from django.contrib import messages

# Create your views here.
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            parent_id  = form.cleaned_data['parent_id']
            position  = form.cleaned_data['position']
            
            reg = BinaryTree(name=name,parent_id=parent_id,position=position)
            reg.save()
            messages.success(request,"Congratulation! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'app/profile.html',locals())
    

def BinaryView(request):
    query = request.GET.get('q')  # Get the query string from the URL parameters
    if query:
        add = BinaryTree.objects.filter(name__icontains=query)
    else:
        add = BinaryTree.objects.all()
    return render(request, 'app/address.html', {'add': add, 'query': query})