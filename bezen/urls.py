from django.urls import path
from .views import RegisterView, GetUserRecords, AddRecord, UpdateRecord
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', obtain_auth_token, name='login'),
    path('records', GetUserRecords.as_view(), name='records'),
    path('add', AddRecord.as_view(), name='add'),
    path('update_record/<int:id>', UpdateRecord.as_view(), name='update_record')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

