from .models import Category,Currency,Transaction
from rest_framework import serializers 


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    transactions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='description')
    url = serializers.HyperlinkedIdentityField(view_name="exchange:category-detail",)

    class Meta:
        model = Category
        fields = ('url','pk', 'name', 'transactions',)
        extra_kwargs = {
                    'url': {
                        'view_name': 'exchange:category-detail',
                        'lookup_field' :'name'
                        },
        }




class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('pk','name','code',)

# https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
# https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-multiple-objects
class TransactionSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/#serializer-relations
    # to show this field as readable way  not  as number,also inter data as word
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    currency = serializers.SlugRelatedField(many=False, read_only=True, slug_field='code')


    # https://www.youtube.com/watch?v=dunf5IqxRaA&list=PLLxk3TkuAYnrO32ABtQyw2hLRWt1BUrhj
    # to show this field as readable way  not  as number,also inter data as word
    # category = serializers.SlugRelatedField(slug_field='name',queryset=Category.objects.all()) ..also work ok 
    #currency = serializers.SlugRelatedField(slug_field='code', queryset=Currency.objects.all()) ..also work ok

    class Meta:
        model = Transaction
        fields = ('pk','uuid','category', 'currency','date_created', 'amount', 'description',)



