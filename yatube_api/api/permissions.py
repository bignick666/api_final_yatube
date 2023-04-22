from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    # Не совсем понимаю как избавиться от
    # request.user.is_authenticated
    # Пытаюсь добавлять пермишн во вьюхах, но
    # Вылезает куча ошибок
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
