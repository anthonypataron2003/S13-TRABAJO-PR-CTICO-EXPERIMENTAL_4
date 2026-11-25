from django.conf import settings
def features(request):
    return {k:getattr(settings,k) for k in ('PRODUCT_VARIANT','ENABLE_REPORTS','ENABLE_NOTIFICATIONS')}
