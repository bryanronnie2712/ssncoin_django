from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
class mineverificationform(forms.Form):
	grade=forms.IntegerField(label="grade",required=True)
	proof=forms.BooleanField(label="proof",required=False)

class mineform(forms.Form):
	Choices=(("professor","proffessor"),
    ("assistant_professor","asst_professor"))
	name= forms.CharField(label='User name',min_length=6,max_length=100,required=True)
	mail=forms.EmailField(label='Mail id',required=True)
	achievement=forms.ChoiceField(label='achievements',choices=Choices)
	department=forms.CharField(label='department',required=True)
	def clean_name(self):
		print(type(self.cleaned_data))
		try:
			p=User.objects.get(name=self.cleaned_data["name"])
			print(p)
			
		except:
			p=0
		print()
		if(p!=0):
			print("1111s")
			raise forms.ValidationError("This user name us taken.")
		else:
			return self.cleaned_data["name"]
		
class pollform(forms.Form):
	Choices=(("kumar","kumar"),
    ("assistant_professor","asst_professor"))
	name= forms.CharField(label='User name',min_length=6,max_length=100,required=True)
	mail=forms.EmailField(label='Mail id',required=True)
	vote=forms.ChoiceField(label='achievements',choices=Choices)
