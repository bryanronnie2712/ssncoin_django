from django.db import models
class block(models.Model):
    index=models.IntegerField(primary_key=True)
    blk_id=models.IntegerField(default=0)
    inhash=models.CharField(max_length=100)
    prevhash=models.CharField(max_length=100)
    transactionid=models.IntegerField(default=0)
    transaction=models.CharField(max_length=40)
    name=models.CharField(max_length=40)
    proof=models.BooleanField(max_length=40)
    nonce=models.IntegerField(null=True)
    mail=models.EmailField()
    next1=models.ForeignKey('self', on_delete=models.SET_NULL,default=None,null=True)
class transaction(models.Model):
    student=models.CharField(max_length=40)
    id=models.IntegerField(primary_key=True)
    staff=models.CharField(max_length=40,default="abc")
    transaction=models.CharField(max_length=40)
    proof=models.BooleanField(default=0)
    grade=models.IntegerField(default=0)
    department=models.CharField(max_length=40)


