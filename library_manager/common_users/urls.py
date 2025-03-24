from django.urls import path
from .views import AdminSignupView, AdminLoginView, BookListCreateView,AdminListView, BookRetrieveUpdateDeleteView, StudentBookListView

urlpatterns = [
    path('signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('login/', AdminLoginView.as_view(), name='admin-login'),
    path('admins/', AdminListView.as_view(), name='admin-list'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
    path('student/books/', StudentBookListView.as_view(), name='student-book-list'),
]
