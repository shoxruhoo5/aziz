# from rest_framework.permissions import BasePermission, SAFE_METHODS


# class MyIsOwner(BasePermission):

#     # def has_permission(self, request, view):
        
#     #     return True

#     def has_object_permission(self, request, view, obj):
#         if request.user.is_authenticated and request.user=obj.user:
#             return True
#         elif request.method in SAFE_METHODS:
#             return True
#         return False
