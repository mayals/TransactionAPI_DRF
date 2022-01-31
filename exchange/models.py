from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32,blank=False,null=True,unique=True)
    
    def __str__(self):
        return self.name
    
    
   
class Currency(models.Model):
    name = models.CharField(max_length=32,blank=False,null=True)
    code = models.CharField(max_length=3,blank=False,null=True,unique=True)

    def __str__(self):
        return self.name



class Transaction(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True) # DO SECOND STEP 
    # uuid = models.UUIDField(default=uuid.uuid4, unique=True)# DO FIRST STEP
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=False, related_name='transactions')
    currency =  models.ForeignKey(Currency,on_delete= models.CASCADE,null=True,blank=False)
    date_created =  models.DateTimeField(auto_now_add= True,auto_now=False)
    amount = models.DecimalField(max_digits=15,decimal_places=2,null=True,blank=False)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.uuid)
        # return f"{self.amount}-{self.currency.code}-{self.date_created}"
