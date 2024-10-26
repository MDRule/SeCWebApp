from rest_framework import permissions
from graphql import GraphQLError




class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    


# ... other permissions here ...
def IsOwnerGQL(user, obj):
    if obj.owner != user:
        raise GraphQLError('You do not have appropriate permissions.')