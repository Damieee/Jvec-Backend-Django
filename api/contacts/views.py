from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
from rest_framework.permissions import IsAuthenticated
from .serializers import ContactSerializer
from django.views import View
from rest_framework.decorators import permission_classes


import json
class CreateContact(View):
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = ContactSerializer(data = json.loads(request.body))
        if serializer.is_valid():
            serializer.save(user=request.user)
            return JsonResponse({'message': 'Contact created successfully.'}, status=201)
        return JsonResponse(serializer.errors, status=400)

class ListContact(View):
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def get(self, request):
        contacts = Contact.objects.filter(data = json.loads(request.body))
        serialized_contacts = [
            {
                'id': contact.id,
                'first_name': contact.first_name,
                'last_name': contact.last_name,
                'phone_number': contact.phone_number,
            }
            for contact in contacts
        ]
        return JsonResponse({'contacts': serialized_contacts}, status=200)

class RetrieveContact(View):
    @permission_classes([IsAuthenticated])
    def get(self, request, contact_id):
        contacts = Contact.objects.filter(user=request.user, id=contact_id)
        serialized_contacts = [
            {
                'id': contact.id,
                'first_name': contact.first_name,
                'last_name': contact.last_name,
                'phone_number': contact.phone_number,
            }
            for contact in contacts
        ]
        return JsonResponse({'contacts': serialized_contacts}, status=200)


class UpdateContact(View):
    @permission_classes([IsAuthenticated])
    def put(self, request, contact_id):
        data = request.data
        user = request.user
        contact = Contact.objects.filter(user=user, id=contact_id).first()
        if not contact:
            return JsonResponse({'message': 'Contact not found.'}, status=404)

        # Update contact fields
        contact.first_name = data['first_name']
        contact.last_name = data['last_name']
        contact.phone_number = data['phone_number']
        contact.save()
        return JsonResponse({'message': 'Contact updated successfully.'}, status=200)

class DeleteContact(View):
    @permission_classes([IsAuthenticated])
    def delete(self, request, contact_id):
        user = request.user
        contact = Contact.objects.filter(user=user, id=contact_id).first()
        if not contact:
            return JsonResponse({'message': 'Contact not found.'}, status=404)
        contact.delete()
        return JsonResponse({'message': 'Contact deleted successfully.'}, status=200)