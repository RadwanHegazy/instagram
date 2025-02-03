from rest_framework.permissions import BasePermission


class BaseIsObjOwner (BasePermission) : 

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        return request.user == obj.owner

class IsPostOwner (BaseIsObjOwner) : 
    pass

class IsStoryOwner(BaseIsObjOwner) : 
    pass
