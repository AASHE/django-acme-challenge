from django.urls import re_path
from .views import ACMEChallengeView

urlpatterns = [
    re_path(
        r'^(?P<challenge_slug>[\w\-]+)$',
        ACMEChallengeView.as_view(),
        name='acme-challenge'
    ),
]
