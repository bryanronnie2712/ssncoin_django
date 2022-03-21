from django import forms
from django.shortcuts import render
from .models import Staff,Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
class signupform(forms.Form):
	Choices=(("professor","proffessor"),
    ("assistant_professor","asst_professor"))
	name = forms.CharField(label='User name',min_length=3,max_length=100,required=True)
	mail=forms.EmailField(label='Mail id',required=True)
	staffid= forms.IntegerField(label='id',required=True)
	password=forms.CharField(label='Password',max_length=23,min_length=8,widget=forms.PasswordInput,required=True)
	department= forms.CharField(label='department',min_length=2,max_length=100,required=True)
	category=forms.ChoiceField(label='category',choices=Choices)
	#def clean_name(self):

	#def clean_staffid(self):

	def clean(self):
		print("111")
		print(type(self.cleaned_data))
		try:
			p=User.objects.filter(username=self.cleaned_data["name"])
			p=p.count()
			print(p)
		except:
			p=0
		print("count in form is ")
		print(p)
		if(p==0):
			print("1111s")
			raise forms.ValidationError("no such user1.")
			print("sss")
		elif(p>1):
			raise forms.ValidationError("name is already taken.")
		print(self)
		print(type(self.cleaned_data))
		print(self.data)
		cleaned_data = super().clean()
		print(cleaned_data)
		print(cleaned_data.get("password"))
		auth=authenticate(username=cleaned_data.get("name"),password=cleaned_data.get("password"))
		#p=User.objects.get(password=cleaned_data.get("password"),username=cleaned_data.get("name"))
		#p=p.password
		'''print(cleaned_data.get("password"))
		print("23243445")
		print(cleaned_data.get("name"))
		print(User.objects.filter(username=cleaned_data.get("name")))
		try:
			p=User.objects.filter(username=cleaned_data.get("name"))
			p=p[0].password
			print(p)
		except:
			p=0
        #cc_myself = cleaned_data.get("cc_myself")
		p1=cleaned_data.get("password")
		print(p1)
		#self.cleaned_data["password2"]
		#print(p1,self.cleaned_data["password2"])'''
		if(auth==0):
			raise forms.ValidationError("password doesnt match")
		print("111")
		print("ididid")
		print(self.cleaned_data)
		#Staff.objects.filter(staffid=self.cleaned_data["staffid"])
		pwd=0
		try:
			u=User.objects.get(username=cleaned_data.get("name"))
			print(u)
			p=Staff.objects.get(staff=u)
			pwd=p.staffid
			print(pwd)
		except:
			pwd=0
		print("count in form is ")
		print(pwd)
		if(pwd!=cleaned_data.get("staffid")):
			print("1111s")
			raise forms.ValidationError("This is invaklid id 1233455 .")
		else:
			print("sucess")
		return self

class loginform(forms.Form):
	name = forms.CharField(label='User name',min_length=6,max_length=100,required=True)
	mail=forms.EmailField(label='Mail id',required=True)
	rollno= forms.IntegerField(label='rollno',required=True)
	password=forms.CharField(label='Password',max_length=23,min_length=8,widget=forms.PasswordInput,required=True)
	#password2=forms.CharField(label='Password2',max_length=23,min_length=8,widget=forms.PasswordInput,required=True)
	department= forms.CharField(label='department',min_length=2,max_length=100,required=True)
	def clean(self):
		print("111")
		print(type(self.cleaned_data))
		try:
			p=User.objects.filter(username=self.cleaned_data["name"])
			p=p.count()
			print(p)

		except:
			p=0
		print("count in form is ")
		print(p)
		if(p==0):
			print("1111s")
			raise forms.ValidationError("no such user1.")
			print("sss")
		elif(p>1):
			raise forms.ValidationError("name is already taken.")
		print(self)
		print(type(self.cleaned_data))
		print(self.data)
		cleaned_data = super().clean()
		print(cleaned_data)
		print(cleaned_data.get("password"))
		p=authenticate(username=cleaned_data.get("name"),password=cleaned_data.get("password"))
		#p=User.objects.get(password=cleaned_data.get("password"),username=cleaned_data.get("name"))
		#p=p.password
		'''print(cleaned_data.get("password"))
		print("23243445")
		print(cleaned_data.get("name"))
		print(User.objects.filter(username=cleaned_data.get("name")))
		try:
			p=User.objects.filter(username=cleaned_data.get("name"))
			p=p[0].password
			print(p)
		except:
			p=0
        #cc_myself = cleaned_data.get("cc_myself")
		p1=cleaned_data.get("password")
		print(p1)
		#self.cleaned_data["password2"]
		#print(p1,self.cleaned_data["password2"])'''
		if(p==0):
			raise forms.ValidationError("password doesnt match")
		print("111")
		print("ididid")
		print(self.cleaned_data)
		#Staff.objects.filter(staffid=self.cleaned_data["staffid"])
		pwd=0
		try:
			u=User.objects.get(username=cleaned_data.get("name"))
			print(u)
			p=Student.objects.get(student=u)
			pwd=p.rollno
			print(pwd)
		except:
			pwd=0
		print("count in form is ")
		print(pwd)
		if(pwd!=cleaned_data.get("rollno")):
			print("1111s")
			raise forms.ValidationError("This is invaklid id .")
		else:
			print("sucess")
		return self
		'''name = forms.CharField(label='User name',min_length=6,max_length=100,required=True)
		#userid=forms.IntegerField(label='Userid',required=True)
		password=forms.CharField(label='Password',max_length=23,min_length=8,widget=forms.PasswordInput,required=True)
		def clean_name(self):
			print(type(self.cleaned_data["name"]))
			name=self.cleaned_data["name"]
			#print(User.objects.get(name=name))
			print(name)
			print(User.objects.get(name=name))
			try:
				name2=User.objects.get(name=name)
				name2=name2.name
				print(name2)

			except:
				name2=""
			if(name!=name2):
				print("1111")
				raise forms.ValidationError("no  user name")
				return self
			else:
				pass
		def clean_password(self):	
			name=self.cleaned_data["password"]
			try:
				name2=User.objects.get(password=self.cleaned_data["password"])
				print("pwd")
				print(name2)
				name2=name2.password
			except:
				name2=""
			if(name!=name2):
				print("1hufhfhfhbbhvf111")
				raise forms.ValidationError("invalid")
			return self
				
			#try:
			#	pwd=cleaned_data["password"]
			#except KeyError:
			#	pwd=0
			try:
				print("form p is")
				#print(cleaned_data["name"])
				p=User.objects.get(name=self.cleaned_data["name"])
				print(User.objects.get(name=name))
				#name=cleaned_data["name"]
				print("form p is")
				print(p)
			except :
				p=0
			print(p)
			#x	pwd=cleaned_data["password"]
			
			if(p==0):
				print("111111111")
				raise forms.ValidationError('please go to sign up')
				return self
			if(p.password!=pwd):
					print("kejhvgfbhdcn")
					#raise forms.ValidationError('invalid')'''
