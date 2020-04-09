from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from shorturl.models import Route, ApiKey, Transaction, ApiDomain


@admin.register(Route)
class RouteAdmin(ModelAdmin):
    base_model = Route  # Explicitly set here!
    list_display = [field.name for field in Route._meta.fields]

@admin.register(ApiKey)
class ApiKeyAdmin(ModelAdmin):
    base_model = ApiKey
    list_display = [field.name for field in ApiKey._meta.fields]

@admin.register(ApiDomain)
class ApiDomainAdmin(ModelAdmin):
    base_model = ApiDomain
    list_display = [field.name for field in ApiDomain._meta.fields]

@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    base_model = Transaction
    list_display = [field.name for field in Transaction._meta.fields]