from django.urls import path
from .views import ProductView

urlpatterns = [
    path('', ProductView.as_view({'get':'fetch', 'post':'create', 'patch':'update', 'delete':'destroy'}))
]
