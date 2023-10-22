from django.urls import path
from .views import CreateContact, ListContacts, RetrieveContact, UpdateContact, DeleteContact

urlpatterns = [
    path('create/', CreateContact.as_view(), name='create_contact'),
    path('list/', ListContacts.as_view(), name='list_contacts'),
    path('retrieve/<int:pk>/', RetrieveContact.as_view(), name='retrieve_contact'),
    path('update/<int:pk>/', UpdateContact.as_view(), name='update_contact'),
    path('delete/<int:pk>/', DeleteContact.as_view(), name='delete_contact'),
]
