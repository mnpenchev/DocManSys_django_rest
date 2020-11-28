from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ allows user to update their own profile """

    def has_object_permission(self, request, view, obj):
        """ check if user is trying to edit their own proffile """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


# class UpdateOwnStatus(permissions.BasePermission):
#     """ Allow users to update their own documents """
#
#     def has_object_permissions(self, request, view, obj):
#         """ check the user is trying to update their own status """
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user_profile.id == request.user.id
