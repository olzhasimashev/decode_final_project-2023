from rest_framework import generics
from procedures.models import Procedure
from .serializers import ProcedureSerializer, SpecialistSerializer, SpecialistCreateSerializer
from specialists.models import Specialist
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .permissions import    (IsSpecialist,
                            CanCreateProcedure,
                            IsOwnerOrReadOnly,
                            IsAdminUser,
                            IsOwner,
                            IsNotSpecialist
                            )

class ProcedureListCreateView(generics.ListCreateAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsSpecialist]
        return super().get_permissions()
    
    def get_queryset(self):
        # If the user is a specialist, return all procedures
        if hasattr(self.request.user, 'specialist'):
            return Procedure.objects.all()
        # Exclude procedures that are booked
        return Procedure.objects.filter(booked_by__isnull=True)

    def perform_create(self, serializer):
        # Here, we can add any logic before saving a procedure, e.g. associating it with a user
        serializer.save(user=self.request.user)
        
class ProcedureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return super().get_permissions()

class SpecialistListCreateView(generics.ListCreateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    permission_classes = [IsAuthenticated, IsSpecialist]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
            self.serializer_class = SpecialistCreateSerializer
        return super().get_permissions()
    
class SpecialistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()
    
class BookProcedureView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            procedure = Procedure.objects.get(pk=pk, booked_by__isnull=True)
        except Procedure.DoesNotExist:
            return Response({"error": "Procedure not available or already booked."}, status=status.HTTP_400_BAD_REQUEST)

        procedure.booked_by = request.user
        procedure.save()

        return Response({"message": "Procedure booked successfully!"}, status=status.HTTP_200_OK)
