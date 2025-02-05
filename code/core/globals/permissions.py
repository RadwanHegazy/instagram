from rest_framework.permissions import IsAuthenticated


class BaseIsObjOwner (IsAuthenticated) : 

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

    
class IsPostOwner (BaseIsObjOwner) : 
    pass

class IsStoryOwner(BaseIsObjOwner) : 
    pass


class IsMessageSender(IsAuthenticated) : 

    def has_object_permission(self, request, view, obj):
        return request.user == obj.sender


class InChatUsers(IsAuthenticated) : 

    def has_object_permission(self, request, view, obj):
        return request.user in obj.users.all()
    