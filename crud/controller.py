from django.db import transaction
from .serializers import *
from utils.helper import *
from utils.response_messages import *

class ProductController:
    product_serializer = ProductSerializer
    image_serializer = ImagesSerializer

    def create_product(self, request):
        try:
            serialized_product = self.product_serializer(data=request.data)

            if serialized_product.is_valid:
                with transaction.atomic():
                    response_data = serialized_product.save()

                    if "images" in request.data:
                        for i in request.data.getlist('images'):
                            image = {
                                'product': response_data.id,
                                'image': i
                            }
                            serialized_image = self.image_serializer(data=image)
                            if serialized_image.is_valid:
                                serialized_image.save()
                            else:
                                return create_response({}, get_first_error_message_from_serializer_errors(
                                    serialized_image.errors, UNSUCCESSFUL), 400)

                return create_response(self.product_serializer(response_data).data, SUCCESSFUL, 200)
            else:
                return create_response({}, get_first_error_message_from_serializer_errors(
                    serialized_product.errors, UNSUCCESSFUL), 400)

        except Exception as e:
            return create_response({'error':str(e)}, UNSUCCESSFUL, 500)


    def fetch_product(self, request):
        try:
            records = self.product_serializer.Meta.model.objects.all()
            response = self.product_serializer(records).data
            return create_response(response, SUCCESSFUL, 200)

        except Exception as e:
            return create_response({'error':str(e)}, UNSUCCESSFUL, 500)

    def update_product(self, request):
        pass

    def destroy_product(self, request):
        pass