from django.urls import path
from .views import ProductListView, ProductSearchView,ChatMessageCreateView,ChatMessageListView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/search/', ProductSearchView.as_view(), name='product-search'),
    path('api/chat/save/', ChatMessageCreateView.as_view(), name='chat-save'),
    path('api/chat/history/', ChatMessageListView.as_view(), name='chat-history'),




]
