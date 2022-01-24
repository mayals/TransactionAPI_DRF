from .models import Category, Currency, Transaction
from .serializers import CategorySerializer, CurrencySerializer,TransactionSerializer 

# generics
from rest_framework import generics


# api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



############################## Category ##########################################
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'







############################### Currency ##############################
class CurrencyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    lookup_field = 'pk'



# https://www.django-rest-framework.org/api-guide/views/#function-based-views
############################### Transaction ##############################
@api_view(http_method_names=['GET', 'POST'])
def transaction_list(request, format=None):
    # GET
    if request.method == 'GET':
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    # POST
    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















# class TransactionViewSet(viewsets.ViewSet):
#     queryset = Transaction.objects.all()
#     from django.shortcuts import get_object_or_404
#     def list(self, request):
#         queryset = Transaction.objects.all()
#         serializer = TransactionSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Transaction.objects.all()
#         transection = get_object_or_404(queryset, pk=pk)
#         serializer = TransactionSerializer(transection)
#         return Response(serializer.data)
    
    
    
    # transaction class is has 2 type acording to action read or write,read_only=True or false  :

    # def get_serializer_class(self):
    #     if self.action in ('list', 'retrieve'):
    #         return ReadTransactionSerializer
    #     return WriteTransactionSerializer












# ############################### Transaction ##############################
# class TransactionListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     # transaction class is has 2 type acording to action read or write,read_only=True or false  :
#     def get_serializer_class(self):
#         if self.action in ('list', 'retrieve'):
#             return ReadTransactionSerializer
#         return WriteTransactionSerializer








# class TransactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()
#     # transaction class is has 2 type acording to action read or write,read_only=True or false :
#     def get_serializer_class(self):
#         if self.action in ('list', 'retrieve'):
#             return ReadTransactionSerializer
#         return WriteTransactionSerializer
