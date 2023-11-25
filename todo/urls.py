from django.urls import path , include
from .views import ApiList, CreateApi ,RetrieveApi

urlpatterns = [
    path('list/', ApiList.as_view()),
    path('create/',CreateApi.as_view()),
    path('<int:pk>/', RetrieveApi.as_view()),
]
