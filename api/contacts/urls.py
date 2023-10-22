from django.urls import path
from .views import CreateContact, ListContact, RetrieveContact, UpdateContact, DeleteContact

urlpatterns = [
    path('create/', CreateContact.as_view(), name='create-contact'),
    path('list/', ListContact.as_view(), name='list-contacts'),
    path('retrieve/<int:contact_id>/', RetrieveContact.as_view(), name='retrieve-contact'),
    path('update/<int:contact_id>/', UpdateContact.as_view(), name='update-contact'),
    path('delete/<int:contact_id>/', DeleteContact.as_view(), name='delete-contact'),
]
