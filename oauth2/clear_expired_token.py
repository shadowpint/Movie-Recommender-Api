from django.utils import timezone
from oauth2_provider.models import (
    AccessToken,
    RefreshToken,
    clear_expired
)


def clear_expired_token():
    now = timezone.now()
    AccessToken.objects.filter(expires__lt=now).delete()

clear_expired_token()    