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
                        'lookup_field' :'pk'
                        },
                    }


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    transactions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='description')
    url = serializers.HyperlinkedIdentityField(view_name="exchange:currency-detail",)
    class Meta:
        model = Currency
        fields = ('url', 'pk', 'name', 'code', 'transactions',)
        extra_kwargs = {
                    'url': {
                        'view_name': 'exchange:currency-detail',
                        'lookup_field': 'pk'
                    },
                }


# https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
# https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-multiple-objects
#Django RESTful Web Services book page 153

class TransactionSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/#serializer-relations
    # to show this field as readable way  not  as number,also inter data as word
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')  # category is foreign key field
    currency = serializers.SlugRelatedField(queryset=Currency.objects.all(), slug_field='code')  # currency is foreign key field
    

    # https://www.youtube.com/watch?v=dunf5IqxRaA&list=PLLxk3TkuAYnrO32ABtQyw2hLRWt1BUrhj
    # category & currency  foreign key fields 
    # category = serializers.SlugRelatedField(slug_field='name',queryset=Category.objects.all()) ..also work ok 
    #currency = serializers.SlugRelatedField(slug_field='code', queryset=Currency.objects.all()) ..also work ok

    # url = serializers.HyperlinkedIdentityField(view_name="exchange:transaction-detail",) # url not work because pk is uuid! must return to default pk to work ok !

    class Meta:
        model = Transaction
        fields = ('pk','uuid','category', 'currency','date_created', 'amount', 'description',)
        # extra_kwargs = {
        #     'url': {
        #         # 'view_name': 'exchange:transaction-detail',
        #         'lookup_field': 'pk'
        #     },
        # }



