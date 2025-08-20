from django.shortcuts import render
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permission_class = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_class.append(IsAdminUser)
        return [permission() for permission in permission_class]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permission_class = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]
    
class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(name=self.request.user.username)

    def get_permissions(self):
        return [IsAuthenticated()]
    
class SingleBookingView(generics.RetrieveDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        return [IsAdminUser()]
