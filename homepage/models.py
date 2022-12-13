from django.db import models
from django.contrib.auth.models import User


# User gồm: username, password, first_name, last_name, is_superuser, email, is_active, last_login. 

class AccountType(models.Model):
    id = models.AutoField(primary_key = True)
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    keyname = models.CharField(max_length=250, blank=True, null=True)
    
    createdate = models.DateTimeField(blank=True, null=True)  
    editdate = models.DateTimeField(blank=True, null=True) 
    isenable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AccountType'

class House(models.Model):
    id = models.AutoField(primary_key = True)
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    sonha = models.CharField(max_length=250, blank=True, null=True)
    duong = models.CharField(max_length=250, blank=True, null=True)
    phuong = models.CharField(max_length=250, blank=True, null=True)
    quan = models.CharField(max_length=250, blank=True, null=True)

    createdate = models.DateTimeField(blank=True, null=True)  
    editdate = models.DateTimeField(blank=True, null=True) 
    isenable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'House'

class Account(models.Model):
    id = models.AutoField(primary_key = True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='userid')
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='creator_user')
    accounttypeid = models.ForeignKey(AccountType, models.DO_NOTHING, blank=True, null=True)
    houseid = models.ForeignKey(House, models.DO_NOTHING, blank=True, null=True)
    
    tenthanh = models.CharField(max_length=250, blank=True, null=True)
    giatruong = models.CharField(max_length=250, blank=True, null=True)
    sinhnhat = models.CharField(max_length=250, blank=True, null=True)
    phaitinh = models.CharField(max_length=250, blank=True, null=True)
    bitich = models.CharField(max_length=250, blank=True, null=True)
    giaoly = models.CharField(max_length=250, blank=True, null=True)
    honnhan = models.CharField(max_length=250, blank=True, null=True)
    hocvan = models.CharField(max_length=250, blank=True, null=True)
    nghenghiep = models.CharField(max_length=250, blank=True, null=True)
    thunhap = models.CharField(max_length=250, blank=True, null=True)
    dienthoai = models.CharField(max_length=250, blank=True, null=True)
    
    
    createdate = models.DateTimeField(blank=True, null=True)  
    editdate = models.DateTimeField(blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Account'