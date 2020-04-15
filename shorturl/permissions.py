from django.conf import settings

from rest_framework.permissions import BasePermission

from shorturl.models import ApiKey


class CheckApiKey(BasePermission):
    def has_permission(self, request, view):
        try:
            api_key = ApiKey.objects.get(key=request.headers.get('X-Api-Key'))
        except:
            return False
        domains = api_key.domains.filter(domain=request.get_host())
        if len(domains) > 0:
            return True
        else:
            return False