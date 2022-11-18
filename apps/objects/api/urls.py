from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.objects.api.v1.urls'))
]
