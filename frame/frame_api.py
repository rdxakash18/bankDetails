from rest_framework import serializers
from .models import bankData
from rest_framework import viewsets

class NoteSerialiser(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = bankData
        fields = ('IFSC', 'bank_id', 'branch', 'address', 'city', 'district','state','bank_name')


class NoteViewSet(viewsets.ModelViewSet):

    queryset = bankData.objects.filter(IFSC='ABHY0065001')
    serializer_class = NoteSerialiser
 
