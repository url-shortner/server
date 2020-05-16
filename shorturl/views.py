from datetime import timedelta, datetime

import pytz
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.openapi import Schema, TYPE_OBJECT
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view

from shorturl import models
from shorturl.models import Route
from shorturl.permissions import CheckApiKey
from shorturl.serializers import RouteSerializer
from shorturl.signals import transaction_sig


def redirection(request, key):
    route = models.Route.objects.get(key=key)
    ttl = timedelta(seconds=route.ttl)
    end = (route.created + ttl).replace(tzinfo=pytz.UTC)
    start = (route.created).replace(tzinfo=pytz.UTC)
    dest = (datetime.now()).replace(tzinfo=pytz.UTC)

    # TODO: 유효성 검사
    if start > dest or dest > end:
        route.disable_count += 1
        route.save()
        transaction_sig.send(sender=None, request=request, key=route, disabled=True)
        return redirect('https://ucut.in/' + str(route.key))

    route.count += 1
    route.save()
    transaction_sig.send(sender=None, request=request, key=route, disabled=False)
    return redirect(route.origin)

@api_view(('GET',))
def ad_tenping(request, key):
    return Response({'msg':key}, status=status.HTTP_200_OK)

class Route(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [CheckApiKey, ]

    @swagger_auto_schema(responses={
        status.HTTP_423_LOCKED: Schema(
            type=TYPE_OBJECT,
            properties={
            }
        )
    })
    def retrieve(self, request, key, *args, **kwargs):
        route = models.Route.objects.get(key=key)
        ttl = timedelta(seconds=route.ttl)
        end = (route.created + ttl).replace(tzinfo=pytz.UTC)
        start = (route.created).replace(tzinfo=pytz.UTC)
        dest = (datetime.now()).replace(tzinfo=pytz.UTC)

        # TODO: 유효성 검사
        if start > dest or dest > end:
            route.disable_count += 1
            route.save()
            transaction_sig.send(sender=None, request=request, key=route, disabled=True)
            return Response({}, status=status.HTTP_423_LOCKED)

        route.count += 1
        route.save()
        transaction_sig.send(sender=None, request=request, key=route, disabled=False)
        return Response(RouteSerializer(route).data, status=status.HTTP_200_OK)


