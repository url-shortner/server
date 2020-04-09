import hashlib
import uuid
from datetime import time

from django.db import models
from model_utils.models import TimeStampedModel


def get_key():
    return str(uuid.uuid4())[:5]


class Route(TimeStampedModel):
    class Meta:
        verbose_name_plural = "라우트"
        app_label = "shorturl"

    key = models.CharField(unique=True, default=get_key, max_length=128)
    origin = models.URLField(verbose_name="원본 url 주소", max_length=512)
    ttl = models.BigIntegerField(verbose_name="유효기간", default=259200)
    count = models.BigIntegerField(verbose_name="카운트", default=0)
    disable_count = models.BigIntegerField(verbose_name="비활성 카운트", default=0)

    def __str__(self):
        return self.key

class Transaction(TimeStampedModel):
    class Meta:
        verbose_name_plural = "트랜젝션"
        app_label = "shorturl"

    key = models.ForeignKey('Route', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(
        verbose_name=('IP Address')
    )
    user_agent = models.CharField(
        verbose_name=('HTTP User Agent'),
        max_length=300,
    )
    is_disabled = models.BooleanField(verbose_name="비활성화 된 요청인지 아닌지",default=False)


def get_api_key():
    return str(uuid.uuid4())

class ApiKey(TimeStampedModel):
    class Meta:
        verbose_name_plural = "Api키 발급"
        app_label = "shorturl"

    key = models.CharField(unique=True, default=get_api_key, max_length=190)
    domains = models.ManyToManyField('ApiDomain')


class ApiDomain(models.Model):
    class Meta:
        verbose_name_plural = "허용 호스트 설정"
        app_label = "shorturl"

    domain = models.CharField(max_length=256, verbose_name="허용 호스트")

    def __str__(self):
        return self.domain
