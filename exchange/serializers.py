from .models import Category,Currency,Transaction
from rest_framework import serializers 




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk','name',)





class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('pk','name','code',)

# https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
# https://www.youtube.com/watch?v=dunf5IqxRaA&list=PLLxk3TkuAYnrO32ABtQyw2hLRWt1BUrhj
# https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-multiple-objects
class TransactionSerializer(serializers.ModelSerializer):
    # to show this field as readable way  not  as number,also inter data as word
    category = serializers.SlugRelatedField(slug_field='name',queryset=Category.objects.all())
    # to show this field as readable way  not  as number,also inter data as word
    currency = serializers.SlugRelatedField(slug_field='code',queryset=Currency.objects.all())

    class Meta:
        model = Transaction
        fields = ('pk', 'category', 'currency','date_created', 'amount', 'description',)



