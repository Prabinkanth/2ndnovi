from django import forms
from .models import BinaryTree,Parent


class CustomerProfileForm(forms.ModelForm):

    
    class Meta:
        model = BinaryTree 
        fields = ['name','parent_id','position']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'parent_id':forms.TextInput(attrs={'class':'form-control'}),
            'position': forms.Select(choices= [('left', 'Left'), ('right', 'Right')], attrs={'class':'form-control'}),
        }
            
        


