from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32,blank=False,null=True)
    def _str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=32,blank=False,null=True)
    code = models.CharField(max_length=3,blank=False,null=True,unique=True)
    def _str__(self):
        return self.name

class Transaction(models.Model):
    category = models.ForeignKey(Category,on_delete= models.SET_NULL,null=True,blank=False)
    currency =  models.ForeignKey(Currency,on_delete= models.PROTECT,null=True,blank=False)
    date_created =  models.DateTimeField(auto_now_add= True,auto_now=False)
    amount = models.DecimalField(max_digits=15,decimal_places=2,null=True,blank=False)
    description = models.TextField(blank=True,null=True)
    def _str__(self):
        return f"{self.amount}-{self.currency.code}-{self.date_created}"