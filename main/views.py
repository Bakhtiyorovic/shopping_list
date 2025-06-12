from rest_framework import viewsets, permissions
from .models import Shopping_item
from .serializers import ShoppingItemSerializer

class ShoppingItemViewSet(viewsets.ModelViewSet):
    queryset = Shopping_item.objects.all()
    serializer_class = ShoppingItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Shopping_item.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)