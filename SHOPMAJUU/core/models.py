from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

# Create your models here.
class Warehouse(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=2, default="US")


def __str__(self):
    return f"{self.code} – {self.city}"

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=2)
    assigned_warehouse = models.ForeignKey(Warehouse, null=True, blank=True, on_delete=models.SET_NULL)
    customer_code = models.CharField(max_length=12, unique=True, default="")


def save(self, *args, **kwargs):
    if not self.customer_code:
        self.customer_code = uuid.uuid4().hex[:12].upper()
    super().save(*args, **kwargs)


def __str__(self):
    return f"Profile for {self.user.username}"


class Package(models.Model):
    class Status(models.TextChoices):
        CREATED = "CREATED", "Created"
        RECEIVED_AT_WAREHOUSE = "RECEIVED", "Received at Warehouse"
        IN_TRANSIT = "IN_TRANSIT", "In Transit"
        OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY", "Out for Delivery"
        DELIVERED = "DELIVERED", "Delivered"


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    tracking_number = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, blank=True)
    weight_kg = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    length_cm = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    width_cm = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    height_cm = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CREATED)
    created_at = models.DateTimeField(default=timezone.now)
    received_at = models.DateTimeField(null=True, blank=True)


def volumetric_weight(self) -> float:
    # industry standard divisor 5000 for cm; adjust in utils if needed
    v = (float(self.length_cm) * float(self.width_cm) * float(self.height_cm)) / 5000.0
    return round(v, 2)


def billable_weight(self) -> float:
    return max(float(self.weight_kg), self.volumetric_weight())


def __str__(self):
    return f"{self.tracking_number} ({self.get_status_display()})"


class TrackingEvent(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="events")
    timestamp = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=120)
    status = models.CharField(max_length=100)
    details = models.TextField(blank=True)


class Meta:
    ordering = ["-timestamp"]


class Invoice(models.Model):
    package = models.OneToOneField(Package, on_delete=models.CASCADE, related_name="invoice")
    currency = models.CharField(max_length=3, default="USD")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_at = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)


def __str__(self):
    return f"Invoice {self.package.tracking_number} – {self.amount} {self.currency}"