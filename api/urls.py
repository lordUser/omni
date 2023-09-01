from rest_framework.routers import SimpleRouter

from api.api import OrderAPI

order_router = SimpleRouter()

order_router.register("orders", OrderAPI, basename="orders")
