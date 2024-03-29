from .models import Category, Currency, Transaction
from .serializers import CategorySerializer, CurrencySerializer,TransactionSerializer 
# generics
from rest_framework import generics
# api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# pagination
from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination
# filtering
from rest_framework import filters
# using django_filters library
from django_filters.rest_framework import DjangoFilterBackend



# http://www.tomchristie.com/rest-framework-2-docs/api-guide/filtering
############################## Category ##########################################
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
 
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination # pagination
    
    #filtering #ordering by using default django restframe work filtering and ordering
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)    
    search_fields = ('name',)     # filtering
    ordering_fields = ('name',)   # ordering
    
    # filtering by using #django_filters library
    filterset_fields = ['category', 'in_stock']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'







############################### Currency ##############################
class CurrencyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = PageNumberPagination  # pagination
   
    #filtering #ordering by using default django restframe work filtering and ordering
    filter_backends = (filters.SearchFilter, filters.OrderingFilter) # filtering # ordering
    search_fields = ('name', 'code',)     # filtering
    ordering_fields = ('name','code',)    # ordering
   
    # filtering by using #django_filters library  ## work ok but no odrdering!!
    # filterset_fields = ['name', 'code']
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'code']



class CurrencyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    lookup_field = 'pk'














# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#select-related
# https://www.youtube.com/watch?v=dunf5IqxRaA&list=PLLxk3TkuAYnrO32ABtQyw2hLRWt1BUrhj
# https://www.django-rest-framework.org/api-guide/views/#function-based-views
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#wrapping-api-views
# https://stackoverflow.com/questions/34043378/how-to-paginate-response-from-function-based-view-of-django-rest-framework
############################### Transaction ##############################

@api_view(http_method_names=['GET', 'POST'])
def transaction_list(request, format=None):
    
    # GET
    if request.method == 'GET':
        
        queryset = Transaction.objects.all().select_related('category','currency').order_by('-date_created')

        # paginator #################################
        paginator = PageNumberPagination()
        paginator.page_size = 4
        queryset_with_paginate = paginator.paginate_queryset(queryset, request)
        serializer = TransactionSerializer(queryset_with_paginate, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
       

   
   
   
    # POST
    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(http_method_names=['GET','PUT','DELETE'])
def transaction_detail(request, pk):
    
    try:
        transaction = Transaction.objects.get(pk=pk) # instance object
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # GET # retreive
    if request.method == 'GET':
        serializer = TransactionSerializer(instance=transaction)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # PUT
    elif request.method == 'PUT':
        serializer = TransactionSerializer(instance=transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












