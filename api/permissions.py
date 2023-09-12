from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSpecialist(BasePermission):
    """Permission check for specialist."""
    
    def has_permission(self, request, view):
        return hasattr(request.user, 'specialist')


class CanCreateProcedure(BasePermission):
    """Permission check for creating a procedure."""
    
    def has_permission(self, request, view):
        if request.method == 'POST':
            return IsSpecialist().has_permission(request, view)
        return True


class IsOwnerOrReadOnly(BasePermission):
    """Permission check for object ownership or read-only requests."""
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # GET, HEAD or OPTIONS
            return True
        return obj.user == request.user 


class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    
    
class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
    
class IsNotSpecialist(BasePermission):

    def has_permission(self, request, view):
        return not hasattr(request.user, 'specialist')
