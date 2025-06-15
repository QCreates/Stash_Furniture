from django.shortcuts import render

# Generic view function factory to generate simple page views with custom titles
def simple_table_view_factory(table_title):
    def view(request):
        return render(request, 'api/simple_table.html', {'title': table_title})
    return view

# Create views for each table
dim_suppliers_view = simple_table_view_factory('Suppliers')
dim_categories_view = simple_table_view_factory('Categories')
dim_products_view = simple_table_view_factory('Products')
dim_customers_view = simple_table_view_factory('Customers')
dim_employees_view = simple_table_view_factory('Employees')
dim_payment_methods_view = simple_table_view_factory('Payment Methods')
dim_purchase_orders_view = simple_table_view_factory('Purchase Orders')
fact_invoices_view = simple_table_view_factory('Invoices')
fact_returns_view = simple_table_view_factory('Returns')
fact_shipments_view = simple_table_view_factory('Shipments')
# Add more as needed
