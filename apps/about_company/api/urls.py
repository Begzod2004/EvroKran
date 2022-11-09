from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.about_company.api.v1.urls'))
]
