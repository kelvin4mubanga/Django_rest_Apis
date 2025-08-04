
from rest_framework import serializers

from .models import BlockchainTransaction

# Blockchain app serializers
class BlockchainTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainTransaction
        fields = '__all__'
        
        
#'api.serializers'