from django.urls import path
from . import views

urlpatterns=[
    path('books/', views.BookListCreateView.as_view(), name='list'),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='detail'),
]