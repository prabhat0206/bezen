from django.urls import path
from .views import RegisterView, GetUserRecords, AddRecord, UpdateRecord
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', obtain_auth_token, name='login'),
    path('records', GetUserRecords.as_view(), name='records'),
    path('add', AddRecord.as_view(), name='add'),
    path('update_record/<int:id>', UpdateRecord.as_view(), name='update_record')
]

