from django.urls import path, include
from .views import  (ProcedureListCreateView,
                    ProcedureRetrieveUpdateDestroyView,
                    SpecialistListCreateView,
                    SpecialistRetrieveUpdateDestroyView,
                    BookProcedureView)


urlpatterns = [
    path('procedures/', ProcedureListCreateView.as_view(), name='procedure-list-create'),
    path('procedures/<int:pk>/', ProcedureRetrieveUpdateDestroyView.as_view(), name='procedure-retrieve-update-destroy'),
    path('specialists/', SpecialistListCreateView.as_view(), name='specialist-list-create'),
    path('specialists/<int:pk>/', SpecialistRetrieveUpdateDestroyView.as_view(), name='specialist-retrieve-update-destroy'),
    path('book_procedure/<int:pk>/', BookProcedureView.as_view(), name='book-procedure'),
]