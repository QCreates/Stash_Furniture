from django.db import models

# Enums as choices
PRODUCT_STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]
PURCHASE_ORDER_STATUS_CHOICES = [('Arrived', 'Arrived'), ('Outgoing', 'Outgoing'), ('Canceled', 'Canceled')]
INVOICE_STATUS_CHOICES = [('Complete', 'Complete'), ('In Progress', 'In Progress'), ('Canceled', 'Canceled')]
INVOICE_TYPE_CHOICES = [('Quote', 'Quote'), ('Invoice', 'Invoice')]
SHIPMENT_STATUS_CHOICES = [('Completed', 'Completed'), ('Partially Complete', 'Partially Complete'), ('Pending', 'Pending'), ('Canceled', 'Canceled')]
SHIPMENT_TYPE_CHOICES = [('Ship', 'Ship'), ('Pickup', 'Pickup')]
SHIPMENT_ITEM_STATUS_CHOICES = [('Arrived', 'Arrived'), ('Outgoing', 'Outgoing'), ('Staged', 'Staged'), ('Pending', 'Pending'), ('Canceled', 'Canceled')]
RETURN_STATUS_CHOICES = [('Complete', 'Complete'), ('Incomplete', 'Incomplete')]

class DimSupplier(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class DimCategory(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class DimProduct(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    qty = models.IntegerField(default=0)
    supplier = models.ForeignKey(DimSupplier, on_delete=models.CASCADE)
    category = models.ForeignKey(DimCategory, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    msrp = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS_CHOICES, default='Active')
    finish = models.CharField(max_length=100, blank=True)
    material = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"

class DimProductImage(models.Model):
    sku = models.ForeignKey(DimProduct, on_delete=models.CASCADE)
    url = models.TextField()

    def __str__(self):
        return f"Image for {self.sku.sku}"

class DimCustomer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    secondary_email = models.EmailField(blank=True)
    secondary_phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    suite = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class DimEmployee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    suite = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class DimPaymentMethod(models.Model):
    method = models.CharField(max_length=100)

    def __str__(self):
        return self.method

class DimMovementReference(models.Model):
    reference_id = models.IntegerField()
    referenced_from = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.referenced_from} - {self.reference_id}"

class DimPurchaseOrder(models.Model):
    supplier = models.ForeignKey(DimSupplier, on_delete=models.CASCADE)
    po_date = models.DateField()
    eta = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=PURCHASE_ORDER_STATUS_CHOICES, default='Outgoing')

    def __str__(self):
        return f"PO {self.pk} from {self.supplier.name}"

class FactPOItem(models.Model):
    po = models.ForeignKey(DimPurchaseOrder, on_delete=models.CASCADE)
    sku = models.ForeignKey(DimProduct, on_delete=models.CASCADE)
    qty = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class FactInvoice(models.Model):
    customer = models.ForeignKey(DimCustomer, on_delete=models.CASCADE)
    employee = models.ForeignKey(DimEmployee, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    system_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=INVOICE_STATUS_CHOICES, default='In Progress')
    type = models.CharField(max_length=20, choices=INVOICE_TYPE_CHOICES, default='Invoice')

class FactInvoiceItem(models.Model):
    invoice = models.ForeignKey(FactInvoice, on_delete=models.CASCADE)
    sku = models.ForeignKey(DimProduct, on_delete=models.CASCADE)
    qty = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_sold = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    system_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class FactPaymentItem(models.Model):
    invoice = models.ForeignKey(FactInvoice, on_delete=models.CASCADE)
    employee = models.ForeignKey(DimEmployee, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(DimPaymentMethod, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class FactShipment(models.Model):
    invoice = models.ForeignKey(FactInvoice, on_delete=models.CASCADE)
    shipment_date = models.DateField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stage_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=SHIPMENT_STATUS_CHOICES, default='Pending')
    type = models.CharField(max_length=20, choices=SHIPMENT_TYPE_CHOICES)

class FactShipmentItem(models.Model):
    shipment = models.ForeignKey(FactShipment, on_delete=models.CASCADE)
    sku = models.ForeignKey(DimProduct, on_delete=models.CASCADE)
    qty = models.IntegerField()
    arrival_date = models.DateField(null=True, blank=True)
    stage_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=SHIPMENT_ITEM_STATUS_CHOICES, default='Pending')

class FactInventoryMovement(models.Model):
    sku = models.ForeignKey(DimProduct, on_delete=models.CASCADE)
    qty = models.IntegerField()
    movement_reference = models.ForeignKey(DimMovementReference, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class FactReturn(models.Model):
    invoice = models.ForeignKey(FactInvoice, on_delete=models.CASCADE)
    sku = models.ForeignKey(DimProduct, on_delete=models.CASCADE)
    qty = models.IntegerField()
    reason = models.TextField(blank=True)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    return_date = models.DateField()
    status = models.CharField(max_length=20, choices=RETURN_STATUS_CHOICES)
