from rest_framework import permissions

class GlobalPermission(permissions.BasePermission):

    def has_permission(self, request, view):
       
        method_perms = {
            'GET': 'view',
            'OPTIONS': 'view',
            'HEAD': 'view',
            'POST': 'add',
            'PATCH': 'change',
            'PUT': 'change',
            'DELETE': 'delete',
        }
        
       
        method = request.method
        if method not in method_perms:
            return False
        
       
        action = method_perms[method]

    
        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
            model = queryset.model
        elif hasattr(view, 'queryset') and view.queryset is not None:
            model = view.queryset.model
        else:
            return False

        
        app_label = model._meta.app_label
        model_name = model._meta.model_name
        required_perm = f'{app_label}.{action}_{model_name}'
        
        
        return request.user.has_perm(required_perm)
