from django.urls import path
from . import views
from.views import uploadXray, homepage, singleView, viewAllXrays, deleteXray

urlpatterns = [
    path('uploadXray/',uploadXray,name = 'uploadXray'),
    path('', homepage, name = 'homepage'),
    path('singleViewXray/<int:xray_id>/',singleView, name='singleView'),
    path('viewAllXrays/',viewAllXrays, name='viewAllXrays'),
    path('deleteXray/<int:xray_id>/',deleteXray, name= 'deleteXray')
]
