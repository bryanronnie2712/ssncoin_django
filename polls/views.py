
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
#from.models import User
import smtplib
from email.message import EmailMessage
from Crypto.PublicKey import RSA
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from.models import Student,Staff
#from .forms import CustomUserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import hashlib
from django.core.mail import send_mail
#from django.au
from django.utils.crypto import get_random_string
#from django.contrib.auth.models import User
from django.conf import settings
import hashlib
from.forms import signupform,loginform	
import smtplib
from django.contrib.auth import authenticate,login,logout
#!/usr/bin/env python 
def index(request):
     #template = loader.get_template('1st page.html')
     return render(request, 'polls/index.html')
     #return HttpResponse(template.render(request))
def signup(request):
	form=signupform()
	if(request.method!="POST"):
		context={"form":form}
		return render(request,'polls/signup.html',context )
	if(request.method=="POST"):
		form =signupform(request.POST)
		u=User()
		if(form.is_valid()):#dbt   
			activation_key = generate_activation_key(username=request.POST['name'])
			subject = "TheGreatDjangoBlog Account Verification"
			message = '''\n
	Please visit the following link to verify your account \n\n{0}://{1}/account/activate/?name={2}&key={3}
							'''.format(request.scheme, request.get_host(),request.POST["name"],activation_key)            
			error = 0
			emailadd="ssncoinmail@gmail.com"
			password="ssncoin2020"
			print("req is ")
			print(request.POST['mail'])
			print("hlooooooooooooooooobhbycxrszxdtfcygvuhbicxszdxfcgvhbkgcyfxdtfcgj")
			#print(type(settings.SERVER_EMAIL))
			msg=EmailMessage()
			msg['Subject']='SSNCOIN Authentication'
			msg['From']=emailadd
			msg['To']=request.POST['mail']
			msg.set_content(message)
			error=0
			try:
				print("111")
				print(User.objects.all())
				server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
				print("111")
				server.login(emailadd,password)
				print("msg sent")
				server.send_message(msg)
				messages.add_message(request,messages.INFO,'Account created! Click on the link sent to myour email to activate the account')
			except:
				error = 1
				messages.add_message(request,messages.INFO, 'Unable to send email verification. Please try again')
			if(error==0):
				if(User.objects.filter(username=request.POST["name"])!=None):
					u =User.objects.get(
								username=request.POST['name'],
					)
					if(u.is_staff==True):
						u.email=request.POST["mail"]
						#u.is_staff=True
						u.save()
						s=Staff.objects.filter(staffid=request.POST["staffid"],staff=u)
						if(s==None):
							'''print("yyyyyy")
							staff=Staff(staff=u,staffid=request.POST["staffid"],department=request.POST["department"],activation_key=generate_activation_key(u.username))
							staff.save()
							keycreate(staff)'''
							messages.add_message(request,messages.INFO,'no user')
						elif(s!=None):
							print("sssss")
							s[0].activation_key=generate_activation_key(u.username)
							s[0].save()
							s.email_validated=True
							keycreate(s[0])
					else:
						messages.add_message(request,messages.INFO,'you are not a staff ')
						return redirect('polls:signup')
				else:
					messages.add_message(request,messages.INFO,'no such user')
			return redirect('polls:signup')

			'''try:
				p=u.objects.get(name=self.cleaned_data["name"])
			except:
				p=0
			print("objects is ")
			print(form.cleaned_data["name"])
			#form.checkuser()
			#curr_user=user.objects.get(name=form["name"],password=form["password"],mail=form["mail"])
			if(p==0):
				curr_user=User.objects.create(name=form.cleaned_data["name"],password=form.cleaned_data["password"],mail=form.cleaned_data["mail"])
				#print("curr suer is ")
				print("sucesss")
		return render(request, 'polls/index.html')'''
	
def slogin(request):
	context={}
	form=loginform()
	if(request.method!="POST"):
		context={"form":form}
		return render(request,'polls/slogin.html',context )
	if(request.method =="POST"):
		# form =AuthenticationForm(request.POST)
		form =loginform(request.POST)
		u=User()
		if(form.is_valid()):   
			activation_key = generate_activation_key(username=request.POST['name'])
			subject = "TheGreatDjangoBlog Account Verification"
			message = '''\n
	Please visit the following link to verify your account \n\n{0}://{1}/account/activate/?name={2}&key={3}
							'''.format(request.scheme, request.get_host(),request.POST["name"],activation_key)            
			error = 0
			emailadd="ssncoinmail@gmail.com"
			password="ssncoin2020"
			print("req is ")
			print(request.POST['mail'])
			print("hlooooooooooooooooobhbycxrszxdtfcygvuhbicxszdxfcgvhbkgcyfxdtfcgj")
			#print(type(settings.SERVER_EMAIL))
			msg=EmailMessage()
			msg['Subject']='SSNCOIN Authentication'
			msg['From']=emailadd
			msg['To']=request.POST['mail']
			msg.set_content(message)
			error=0
			try:
				print("111")
				print(User.objects.all())
				server = smtplib.SMTP_SSL('smtp.gmail.com',465)
				print("111")
				server.login(emailadd,password)
				print("msg sent")
				
				server.send_message(msg)
				messages.add_message(request,messages.INFO,'Account created! Click on the link sent to myour email to activate the account')
			except:
				print("error in mail")
				error = 1
				messages.add_message(request,messages.INFprint(Block(4).data)O, 'Unable to send email verification. Please try again')
			if(error==0):
				if(User.objects.filter(username=request.POST["name"])!=None):
					u =User.objects.get(       
								username=request.POST['name'],				
					)
				if(u.is_staff==False):
					u.email=request.POST["mail"]
					u.is_staff=False
					u.save()
					s=Student.objects.filter(rollno=request.POST["rollno"],student=u)
					s=s[0]
					if(s==None):
						'''print("yyyyyy")
						s.rollno=request.POST["rollno"]
						s.department=request.POST["department"]
						s.activation_key=generate_activation_key(u.username)
						s.save()
						keycreate(s)'''
						messages.add_message(request,messages.INFO,'no user')
					elif(s!=None):
						print("sssss")
						print(u)
						print(u.username)
						s.rollno=request.POST["rollno"]
						s.department=request.POST["department"]
						s.activation_key=generate_activation_key(u.username)
						s.save()
						s.email_validated=True
						print(s)
						#s[0].save()	
						print(s.activation_key)
						keycreate(s)
					else:
						messages.add_message(request,messages.INFO,'you are a staaff')
				else:
					messages.add_message(request,messages.INFO,'no such user')
			return redirect('polls:login')
		'''form=loginform(request.POST)
		if form.is_valid():
		print(type(form.cleaned_data["name"]))
			#if(type(form.cleaned_data["name"])=="str"):
			print("sdfghjkjhg")
			name=request.POST["name"]
			pwd=request.POST['password']
			#else:
				#	name=form.cleaned_data["name"].data
				#	pwd=form.cleaned_data['password'].data
				print("name is")
				print(name)
				print(form.cleaned_data["name"])
				try:
					p=User.objects.get(name=name)
					print("p user is ")
					
					print(User.objects.get(name=name).name)	
					print("p is 1234")
					print(p.name,p.password)
				except:
					p=0
				#print(p.count())
				print("p is ")
				print(p)
				if(p==0):	
					print("user is")
					print(User)
					form=signupform()
					return render(request,'polls/signup.html',{"form":form})
				elif(p.name==name and p.password==pwd):'''
		'''name=request.POST["name"]
			messages.add_message(request, messages.INFO, 'welcome {}'.format(name))'''
		print("sucess")
				#template = loader.get_template('blockapp/home.html')
				#return render(request, 'polls/index.html')
				#return HttpResponse(template.render({"form":form}))
			#return redirect('blockapp:home',request.POST["name"])		
	context["form"]=form
	#messages.add_message(request, messages.INFO, 'Account created! Click on the link sent to your email to activate the account')
	return render(request,'polls/slogin.html',context)
# Create your views here.
def generate_activation_key(username):
	inhash=hashlib.sha256()
	chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	secret_key = get_random_string(20, chars)
	inhash.update((secret_key + username).encode('utf-8'))
	return inhash.hexdigest()
def activate(request):
	print(request.GET.get("key",False))
	print(request.GET.get("name",False))
	try:
		key=request.GET["key"]

		print(key)

	except:
		messages.add_message(request, messages.INFO, 'activation key not used')
		form=signupform()
		context={"form":form}
		return render(request,'polls/index.html',context)
	print("namein url")
	print(request.GET.get("name"))
	user=User.objects.get(username=request.GET.get("name"))
	print("obj is")

	print("obj is")
	print(user)
	print()
	#user=authenticate(username=u.username,password=u.password)
	#print(user)
	user.is_active=True
	print(user.is_active)
	user.save()
	messages.add_message(request, messages.INFO, 'Account activated enjoy')
	login(request,user)
	return redirect("blockapp:home",request.GET["name"])
def keycreate(u):
            key=RSA.generate(2048)
            pubkey=key.publickey()
            pubkey=pubkey.exportKey("PEM")
            privkey=key.exportKey("PEM")
            print(privkey.hex())
            print("pubkey iz")
            u.pubkey=pubkey.decode()
            u.privkey=privkey.decode()
            u.save()
            print(pubkey.hex())
