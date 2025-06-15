from django.urls import path
from django.views.generic import TemplateView
from .views import (
    dim_suppliers_view,
    dim_categories_view,
    dim_products_view,
    dim_customers_view,
    dim_employees_view,
    dim_payment_methods_view,
    dim_purchase_orders_view,
    fact_invoices_view,
    fact_returns_view,
    fact_shipments_view,
    # add more views here...
)

urlpatterns = [
    path('pages/', TemplateView.as_view(template_name='api/index.html'), name='home'),
    path('pages/suppliers/', dim_suppliers_view, name='page-suppliers'),
    path('pages/categories/', dim_categories_view, name='page-categories'),
    path('pages/products/', dim_products_view, name='page-products'),
    path('pages/customers/', dim_customers_view, name='page-customers'),
    path('pages/employees/', dim_employees_view, name='page-employees'),
    path('pages/payment-methods/', dim_payment_methods_view, name='page-payment-methods'),
    path('pages/purchase-orders/', dim_purchase_orders_view, name='page-purchase-orders'),
    path('pages/invoices/', fact_invoices_view, name='page-invoices'),
    path('pages/returns/', fact_returns_view, name='page-returns'),
    path('pages/shipments/', fact_shipments_view, name='page-shipments'),

]
