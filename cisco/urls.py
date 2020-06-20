
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from IpconfigCRUD.views import get_Ipconfig
schema_view=get_swagger_view(title='welcome swagger app')
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url('swagger/',schema_view),
    url('v1/ipconfig/',include('IpconfigCRUD.urls')),
    url(r'^get_api_token', views.obtain_auth_token,name='get_api_token'),
    url(r'^ipconfig', get_Ipconfig),
]