# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Contact
# from .serializers import ContactSerializer
# from django.views import View
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
# from django.utils.decorators import method_decorator

# import json

# class CreateContact(View):
#     @method_decorator(login_required)
#     @csrf_exempt
#     def post(self, request):
#         data = request.POST
#         username = data.get('username')
#         password = data.get('password')
#         print(username)
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#         else:
#             return JsonResponse({'message': 'User authentication failed.'}, status=401)

#         # Create the contact with the user
#         serializer = ContactSerializer(data=data, context={'user': user})
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message': 'Contact created successfully.'}, status=201)
#         return JsonResponse(serializer.errors, status=400)

# class ListContact(View):
#     @csrf_exempt
#     @login_required
#     def get(self, request):
#         contacts = Contact.objects.filter(data = json.loads(request.body))
        
#         serialized_contacts = [
#             {
#                 'id': contact.id,
#                 'first_name': contact.first_name,
#                 'last_name': contact.last_name,
#                 'phone_number': contact.phone_number,
#             }
#             for contact in contacts
#         ]
#         return JsonResponse({'contacts': serialized_contacts}, status=200)

# class RetrieveContact(View):
#     @login_required
#     def get(self, request, contact_id):
#         contacts = Contact.objects.filter(user=request.user, id=contact_id)
#         serialized_contacts = [
#             {
#                 'id': contact.id,
#                 'first_name': contact.first_name,
#                 'last_name': contact.last_name,
#                 'phone_number': contact.phone_number,
#             }
#             for contact in contacts
#         ]
#         return JsonResponse({'contacts': serialized_contacts}, status=200)


# class UpdateContact(View):
#     @login_required
#     def put(self, request, contact_id):
#         data = request.data
#         user = request.user
#         contact = Contact.objects.filter(user=user, id=contact_id).first()
#         if not contact:
#             return JsonResponse({'message': 'Contact not found.'}, status=404)

#         # Update contact fields
#         contact.first_name = data['first_name']
#         contact.last_name = data['last_name']
#         contact.phone_number = data['phone_number']
#         contact.save()
#         return JsonResponse({'message': 'Contact updated successfully.'}, status=200)

# class DeleteContact(View):
#     @login_required
#     def delete(self, request, contact_id):
#         user = request.user
#         contact = Contact.objects.filter(user=user, id=contact_id).first()
#         if not contact:
#             return JsonResponse({'message': 'Contact not found.'}, status=404)
#         contact.delete()
#         return JsonResponse({'message': 'Contact deleted successfully.'}, status=200)


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .serializers import ContactSerializer


class CreateContact(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return JsonResponse({'message': 'User authentication failed.'}, status=401)

        # Create the contact with the user
        serializer = ContactSerializer(data=data, context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Contact created successfully.'}, status=201)
        return JsonResponse(serializer.errors, status=400)


class ListContacts(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self, request):
        return Contact.objects.filter(user=request.user)


class RetrieveContact(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class UpdateContact(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class DeleteContact(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
