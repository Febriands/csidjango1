from . import models
from rest_framework import serializers


class StandardSerializer(serializers.HyperlinkedModelSerializer):
    standard_manual = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Standard
        fields = ('id', 'name', 'date_created', 'standard_manual')

class ManualSerializer(serializers.HyperlinkedModelSerializer):
    manual_procedure = serializers.StringRelatedField(many=True)
    manual_form = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Manual
        fields = ('id', 'name', 'code', 'version', 'date_created', 'manual_procedure', 'manual_form')

class ProcedureSerializer(serializers.HyperlinkedModelSerializer):
    procedure_form = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Procedure
        fields = ('id', 'name', 'code', 'version', 'date_created', 'procedure_form')

class FormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Form
        fields = ('id', 'name', 'code', 'version', 'date_created')