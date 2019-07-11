from . import models
from rest_framework import serializers


class ManualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manual
        fields = ('id', 'name', 'code', 'version', 'date_created')


class ProcedureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Procedure
        fields = ('id', 'name', 'code', 'version', 'date_created')

class FormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Form
        fields = ('id', 'name', 'code', 'version', 'date_created')