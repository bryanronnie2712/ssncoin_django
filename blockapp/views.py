from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
import random
from Crypto.PublicKey import RSA
from django.contrib import messages
from polls.models import Staff,Student
from django.contrib.auth.models import User
import hashlib
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import json
from.models import block,transaction
from polls.forms import signupform,loginform
from.forms import mineform,pollform,mineverificationform
# Create your views here.
data={}
@login_required(login_url="home/name/login")
def home(request,name):
    #data=get_object_or_404(User,name)
    #authenticate(use)
    #print(data)
    print(request.user)
    #print(request.GET.get("u")  )
    '''if(request.user.is_active==False):
        messages.add_message(request, messages.INFO, 'you need to login')  
        return redirect("blockapp:login")
    else:'''
    return render(request,"blockapp/home.html")
def userlogout(request,name):
    print(request.user.is_active)
    u=User.objects.get(username=name)
    u.is_active=False
    logout(request)
    print("login")
    print(request.method)
    return render(request,"blockapp/login.html",{"name":name})
    if(request.method=="POST"):
        #u=User.objects.get(username=name) 
        print(request.GET)
        if (request.GET.get('next', None)):
            u=authenticate(username=request.POST["name"],password=request.POST["pwd"])
            print("u si")
            print("user is ")
            print(u)
            if(u):
                u.is_active=True
                login(request,u)
                return redirect(request.GET["next"])
            else:
                messages.add_message(request, messages.INFO, 'invalid login') 
                return render(request,"blockapp/login.html",{"name":name})
        else:  
            u=authenticate(username=request.POST["name"],password=request.POST["pwd"])
            if(u):
                u.is_active=True
                login(request,u)
                return redirect("blockapp:home",name)
            else:
                messages.add_message(request, messages.INFO, 'invalid login')    
                return render(request,"blockapp/login.html",{"name":name})
    else:
        print("1111")
        form=AuthenticationForm()
        return render(request,"blockapp/login.html",{"form":form,"name":name})
@login_required(login_url="home/name/login")
def mine(request,name):
    #trans=transaction.objects.filter(staff=name)
    form=mineform()
    return render(request,"blockapp/mine.html",{"form":form})
    if(request.method=="POST"):
        #cat=Staff.objects.get(achievement=request.POST["achievement"])
        #print(cat)
        form=pollform()
        return render(request,"blockapp/mine.html",{"form":form})
        '''block chain should be present only in this '''
@login_required(login_url="home/name/login")
def mine1(request,name,id):
    if(request.method!="POST"):
        form=mineverificationform()
        context={"form":form}
        return render(request,"blockapp/mine.html",context)
    #trans=transaction.objects.filter(staff=name)
    grade=request.POST["grade"]
    proof=request.POST["proof"]
    if(proof=="on"):
        proof=True
    else:
        proof=False        
    print(type(proof))
    trans=transaction.objects.get(id=id)
    trans.grade=grade
    trans.proof=proof
    trans.save()
    class Block:
            nonce=0
            prevhash=0x0
            transaction=0
            inhash=None
            #def __init__(self,name):
            def __init__(self,name,mail,i_d,transaction,grade,transactionid):
            
                b=block()
                b.blk_id=i_d
                b.name=name
                b.transactionid=transactionid
                b.mail=mail
                b.transaction=transaction
                b.proof=True
                self.data={
                        "id":i_d,
                        "transactionid":transactionid,
                        "mail":mail,
                        "name":name,
                        "transaction":transaction,
                        "index":0,
                        "prevhash":0x0,
                        "timesoftrial":1,
                        "proof":True,
                        "grade":grade,
                       
                        "nonce":0,         
                    }
                #self.inhash(self.data)
                self.data["inhash"]=self.inhash(self.data)
                print(self.data["inhash"])
                b.hash=self.data["inhash"]
                b.next1=None
                self.next=None
                b.save()
            @staticmethod
            def inhash(data):
                inhash=hashlib.sha256()
                #print(hashlib.algorithms_available)
                #print(hashlib.algorithms_guarenteed
                jsonobj=json.dumps(data)
                n = random.randint(1,1000)
                #print("jsonis")
                #print(jsonobj)
                inhash.update(str(jsonobj).encode()+str(n).encode())
                #print(inhash.hexdigest())
                #self.data["inhash"]=inhash.hexdigest()
                return inhash.hexdigest()
    class merkle:
            merktree=[]
            def treeform(self,blocks):
                    #print("block is")
                    #print(blocks)
                    self.temp=[]
                    new_blocks=[]
                    new_blocks=blocks.copy()
                    new_blocks=sorted(new_blocks)
                    hasher=hashlib.sha256()
                    if(len(blocks)%2!=0):
                        new_blocks.append(new_blocks[-1])
                    for k in[new_blocks[x:x+2] for x in range(0,len(new_blocks),2)]:
                        string=""
                        string=k[0]+k[1]
                        hasher.update(string.encode())
                        self.temp.append(hasher.hexdigest())
                        #print("temp is")
                        #print(self.temp)
                    self.merktree.extend(self.temp)
                    #print("merk is")
                    #print(self.merktree)
                    if(len(self.temp)>1):
                        self.treeform(self.temp)
                    if(len(self.temp)==1):
                        #print("merk tree is ")
                        #print(self.merktree)
                        return(self.merktree)
            
    class blockchain:
            maxnonce=2**256
            diff=10
            target=2**(256-diff)
            curr=None
            try:
                print("chain class start")
                curr=block.objects.filter(index=1)
                print("chain class start")
                curr=block.objects.all()
                print("chain class start")
                print(len(curr))
                curr=curr[len(curr)-1]
                print("chain class start")
                print("curr at start is ")
                print(curr)
            except:
                print("genesis blk generation")
                b=block()
                b.name="genensis"
                print("name")
                b.index=1
                b.mail=""
                b.blk_id=0
                b.transaction=""
                b.proof=True
                data={"name":b.name,"index":b.index,"mail":b.mail,"transaction":b.transaction}
                b.inhash=Block.inhash(data)
                b.prevhash=""
                b.next1=None
                print(b.next1)
                b.save()
                curr=b
            def add(self,bblock):
                print("id ")
                print(bblock.data["id"])
                b=block.objects.filter(name=trans.student,mail=u.email,blk_id=bblock.data["id"],transactionid=id)
                print(b)
                self.curr=block.objects.filter(index=self.curr.index)
                self.curr=self.curr[0]
                b=b[0]
                print("selected hser is")
                print(b)
                bblock.data["prevhash"]=self.curr.inhash
                bblock.data["index"]=self.curr.index+1
                print("sucess")
                print("self.curr before")
                print(self.curr)
                #bblock.next=self.curr.next1
                print("self.curr.next")
                print(self.curr.next1)
                print("self.curr is")
                print(self.curr)
                print(self.curr.name)
                print("sucess2")
                b.index=bblock.data["index"]
                b.nonce=bblock.data["nonce"]
                b.inhash=bblock.data["inhash"]
                b.prevhash=bblock.data["prevhash"]
                b.save()
                self.curr.next1=b   
                self.curr.save()
                self.curr=b
                # def check(self):
            #     if(dup.data[inhash]==dup.next.data[prevhash]):
            #        dup=dup.next

            def mine(self,block):
                for n in range(self.maxnonce):
                    h=block.inhash(block.data)
                    if(int(h, 16)<=self.target):
                        block.data["nonce"]=n
                        block.data["inhash"]=h
                        self.add(block)
                        break
                    else:
                        block.data["nonce"]+=1
    print("chain form")
    chain= blockchain()
    tree=merkle()
    merk=[]
    for i in range(10):
            l=[]
            for j in range(i,i+10,1):
                l.append(str(j))
        #print(l)
                merk=tree.treeform(l)      
        #print("merk tree is")
        #print(merk)
        #print("\n" "1merk rooot is")
        #print(merk[-1])
        #chain.mine(block(name))
    trans=transaction.objects.get(id=id)
    u=User.objects.get(username=trans.student)
    print(u)
    if(u.is_staff==False):
            s=Student.objects.get(student=u)
            if(proof):
                chain.mine(Block(trans.student,u.email,s.rollno,trans.transaction,grade,id))     
    elif(u.is_staff==True):
            s=Staff.objects.get(staff=u)
            if(vote):
                chain.mine(Block(name,u.email,s.staff_id,proof,grade))
        #chain.mine(block(name,u.email,s.rollno,form.cleaned_data["achievement"]))
    print("block chain is z")
    #return render(request,"blockapp/mine.html",{"form":form})
    list1=block.objects.all()
    form=mineform()
    context={"list":list1,"form":form}
    #return render(request,"blockapp/details.html",context)
    return redirect("../details")
def selectrandom(selectedusers):
    totalusers=len(selectedusers)
    maxlen=int(totalusers/3)
    if(maxlen<0):
        maxlen=1
    for i in range(maxlen):
        n=random.randint(0,totalusers)
        selectedusers[i]=selectedusers[n]
    return selectedusers
@login_required(login_url="home/name/login")
def details(request,name):
    u=User.objects.get(username=name)
    randomlist = []
    for i in range(0,100):
        n = random.randint(1,30)
        randomlist.append(n)
    #print(randomlist)
    if(request.method!="POST"):
        u=User.objects.get(username=name)
        print("non post form")
        print(u)
        form=mineform()
        try:
            staff=Staff.objects.get(staff=u)
        except:
            staff=0
        print(name)
        list1=block.objects.all()
        ''''''
        minetrans=[]
        #print last
        if(staff):
            transac=transaction.objects.filter(staff=name)
            print(transac)
            print(len(transac))
            j=0
            for i in transac:
                print("jnkrefbjrfbrfihrfnjrfnhjrfjirfjirfjkrfhrfnjrfjkrfjkrfjrfhjrfhjrf")
                print(i)
               
                if(i.proof!=True):
                    minetrans.append(i)
                    j=j+1
                print(minetrans)
                messages.add_message(request, messages.INFO, "you have a transaction to mine")
                '''selectedusers=Staff.objects.filter(department=staff.department)
                selectrandom(selectedusers)
                trans=transaction.objects.filter(department=staff.department,staff="abc")
                j=0
                for i in trans:
                    print(name)
                    print(i)
                    print(i.staff)
                    print(selectedusers[j].staff.username)
                    if(i!=None):
                        print("111")
                        if(i.staff=="abc"):
                            print("111")
                            if(selectedusers[j]!=None):
                                i.staff=selectedusers[j].staff.username
                                print("111")
                                print(i.staff)
                                i.save()
                                j=j+1'''
                #minetrans=transaction.objects.filter(staff=name)
            # print(minetrans)               
            list1=block.objects.all()
            context={"trans":minetrans,"list1":list1}            
            return render(request,"blockapp/details.html",context)
        list1=block.objects.all()
        context={"list1":list1,"form":form}
        return render(request,"blockapp/details.html",context)
    elif(request.method=="POST"):
        # create transaction
        #{}
        form=mineform(request.POST)
        print(form)
        print("detailsss")
        print(request.POST)
        #trans=transaction.objects.create(student=request.POST["name"],transaction=request.POST["achievement"],department=request.POST["department"],staff="abc")
        #trans.save()
        selectedusers=Staff.objects.filter(department=request.POST["department"])
        print("lkjhgfdsfghjkl;lkjhgfdsadfghjkl")
        print(selectedusers)
        selectrandom(selectedusers)
        totalusers=len(selectedusers)-1
        messages.add_message(request, messages.INFO, "your transaction is added")
        n=random.randint(0,totalusers)
        #trans=transaction.objects.filter(student=request.POST["name"])
        #trans=trans[0]
        #trans.staff=selectedusers[n].staff.username
        trans=transaction.objects.create(student=request.POST["name"],transaction=request.POST["achievement"],department=request.POST["department"],staff=selectedusers[n].staff.username)
        #trans.save()
        list1=block.objects.all()
        context={"list1":list1}
        return render(request,"blockapp/details.html",context)
        
