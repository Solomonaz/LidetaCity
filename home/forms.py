from django import forms
from .models import CommentModel

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['commented_person_name', 'comment_sector', 'comment_body'] 

        widgets = {
            'commented_person_name': forms.TextInput(attrs={'class': 'form-control bg-white border-0', 'placeholder':'ማን ላይ ነው ቅሬታ ያለዎት?'}),
            'comment_sector': forms.TextInput(attrs={'class': 'form-control bg-white border-0', 'placeholder':'ቅሬታ የሚያቀርቡበት ቢሮ ስም?'}),
            'comment_body': forms.Textarea(attrs={'class': 'form-control bg-white border-0', 'placeholder':'ቅሬታዎን ይጻፉ'}),
        }
