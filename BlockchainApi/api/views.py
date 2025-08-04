from rest_framework import generics
from .models import BlockchainTransaction
from .serializers import BlockchainTransactionSerializer




class BlockchainTransactionList(generics.ListCreateAPIView):

    queryset =BlockchainTransaction.objects.all()
    serializer_class=BlockchainTransactionSerializer



class BlockchainTransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=BlockchainTransaction.objects.all()
    serializer_class=BlockchainTransactionSerializer
