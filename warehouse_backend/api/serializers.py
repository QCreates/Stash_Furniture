from rest_framework import serializers
from .models import *

class DimSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimSupplier
        fields = '__all__'

class DimCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DimCategory
        fields = '__all__'

class DimProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimProduct
        fields = '__all__'

class DimProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimProductImage
        fields = '__all__'

class DimCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimCustomer
        fields = '__all__'

class DimEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimEmployee
        fields = '__all__'

class DimPaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimPaymentMethod
        fields = '__all__'

class DimMovementReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimMovementReference
        fields = '__all__'

class DimPurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimPurchaseOrder
        fields = '__all__'

class FactPOItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactPOItem
        fields = '__all__'

class FactInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactInvoice
        fields = '__all__'

class FactInvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactInvoiceItem
        fields = '__all__'

class FactPaymentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactPaymentItem
        fields = '__all__'

class FactShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactShipment
        fields = '__all__'

class FactShipmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactShipmentItem
        fields = '__all__'

class FactInventoryMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactInventoryMovement
        fields = '__all__'

class FactReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactReturn
        fields = '__all__'
