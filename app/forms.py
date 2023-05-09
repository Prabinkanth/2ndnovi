from django import forms
from.models import BinaryTree,parrent


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = BinaryTree 
        fields = ['name','parent_id','position']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'parent_id':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            
        }


