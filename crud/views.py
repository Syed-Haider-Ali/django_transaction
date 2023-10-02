from rest_framework.viewsets import ModelViewSet
from .controller import ProductController


product_controller = ProductController()

class ProductView(ModelViewSet):

    def create(self, request):
        return product_controller.create(request)

    def fetch(self, request):
        return product_controller.fetch(request)

    def update(self, request):
        return product_controller.update(request)

    def destroy(self, request):
        return product_controller.destroy(request)
