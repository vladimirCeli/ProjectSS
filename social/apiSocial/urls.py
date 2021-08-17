from django.urls import path
from .CRUD.CRUDProfile import GetProfile
from .CRUD.CRUDUser import GETUser

urlpatterns = [
    path('getProfiles/', GetProfile.as_view(), name='getProfile'),
    path('getUsers/', GETUser.as_view(), name='getUser')
]
