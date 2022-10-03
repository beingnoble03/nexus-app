from rest_framework import permissions


class Is3or4y(permissions.BasePermission):
    message = 'Only 3y and 4y are permitted.'

    def has_permission(self, request, view):
        return request.user.year >= 3

class CanViewMemberDetails(permissions.BasePermission):
    message = '2y or 1y are not permitted to view details of 3y or later.'

    def has_object_permission(self, request, view, obj):
        return request.user.year > 2 or obj.year < 3