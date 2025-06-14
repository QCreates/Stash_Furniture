from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    DimSupplierViewSet,
    DimCategoryViewSet,
    DimProductViewSet,
    DimProductImageViewSet,
    DimCustomerViewSet,
    DimEmployeeViewSet,
    DimPaymentMethodViewSet,
    DimMovementReferenceViewSet,
    DimPurchaseOrderViewSet,
    FactPOItemViewSet,
    FactInvoiceViewSet,
    FactInvoiceItemViewSet,
    FactPaymentItemViewSet,
    FactShipmentViewSet,
    FactShipmentItemViewSet,
    FactInventoryMovementViewSet,
    FactReturnViewSet,
)

router = DefaultRouter()
router.register(r'suppliers', DimSupplierViewSet)
router.register(r'categories', DimCategoryViewSet)
router.register(r'products', DimProductViewSet)
router.register(r'product-images', DimProductImageViewSet)
router.register(r'customers', DimCustomerViewSet)
router.register(r'employees', DimEmployeeViewSet)
router.register(r'payment-methods', DimPaymentMethodViewSet)
router.register(r'movement-references', DimMovementReferenceViewSet)
router.register(r'purchase-orders', DimPurchaseOrderViewSet)
router.register(r'po-items', FactPOItemViewSet)
router.register(r'invoices', FactInvoiceViewSet)
router.register(r'invoice-items', FactInvoiceItemViewSet)
router.register(r'payment-items', FactPaymentItemViewSet)
router.register(r'shipments', FactShipmentViewSet)
router.register(r'shipment-items', FactShipmentItemViewSet)
router.register(r'inventory-movements', FactInventoryMovementViewSet)
router.register(r'returns', FactReturnViewSet)

urlpatterns = router.urls
