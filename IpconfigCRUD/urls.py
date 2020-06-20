from rest_framework.routers import SimpleRouter
from IpconfigCRUD.views import IPDATAViewset

simplerouter=SimpleRouter()
simplerouter.register('ipdetails',IPDATAViewset)
urlpatterns=simplerouter.urls
