from rest_framework import viewsets
from .models import *
from .serializers import *

class DimSupplierViewSet(viewsets.ModelViewSet):
    queryset = DimSupplier.objects.all()
    serializer_class = DimSupplierSerializer

class DimCategoryViewSet(viewsets.ModelViewSet):
    queryset = DimCategory.objects.all()
    serializer_class = DimCategorySerializer

class DimProductViewSet(viewsets.ModelViewSet):
    queryset = DimProduct.objects.all()
    serializer_class = DimProductSerializer

class DimProductImageViewSet(viewsets.ModelViewSet):
    queryset = DimProductImage.objects.all()
    serializer_class = DimProductImageSerializer

class DimCustomerViewSet(viewsets.ModelViewSet):
    queryset = DimCustomer.objects.all()
    serializer_class = DimCustomerSerializer

class DimEmployeeViewSet(viewsets.ModelViewSet):
    queryset = DimEmployee.objects.all()
    serializer_class = DimEmployeeSerializer

class DimPaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = DimPaymentMethod.objects.all()
    serializer_class = DimPaymentMethodSerializer

class DimMovementReferenceViewSet(viewsets.ModelViewSet):
    queryset = DimMovementReference.objects.all()
    serializer_class = DimMovementReferenceSerializer

class DimPurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = DimPurchaseOrder.objects.all()
    serializer_class = DimPurchaseOrderSerializer

class FactPOItemViewSet(viewsets.ModelViewSet):
    queryset = FactPOItem.objects.all()
    serializer_class = FactPOItemSerializer

class FactInvoiceViewSet(viewsets.ModelViewSet):
    queryset = FactInvoice.objects.all()
    serializer_class = FactInvoiceSerializer

class FactInvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = FactInvoiceItem.objects.all()
    serializer_class = FactInvoiceItemSerializer

class FactPaymentItemViewSet(viewsets.ModelViewSet):
    queryset = FactPaymentItem.objects.all()
    serializer_class = FactPaymentItemSerializer

class FactShipmentViewSet(viewsets.ModelViewSet):
    queryset = FactShipment.objects.all()
    serializer_class = FactShipmentSerializer

class FactShipmentItemViewSet(viewsets.ModelViewSet):
    queryset = FactShipmentItem.objects.all()
    serializer_class = FactShipmentItemSerializer

class FactInventoryMovementViewSet(viewsets.ModelViewSet):
    queryset = FactInventoryMovement.objects.all()
    serializer_class = FactInventoryMovementSerializer

class FactReturnViewSet(viewsets.ModelViewSet):
    queryset = FactReturn.objects.all()
    serializer_class = FactReturnSerializer
