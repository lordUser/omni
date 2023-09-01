from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Order
from api.serializers import OrderSerializer, OrderStatusSerializer


class OrderAPI(ModelViewSet):
    http_method_names = "get", "post", "patch"
    object = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=("get",), detail=True, serializer_class=OrderStatusSerializer)
    def status(self, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
