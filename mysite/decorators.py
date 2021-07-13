from django.shortcuts import HttpResponse


def allowed_users(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user = request.user
            if user.groups.exists():
                groups = request.user.groups.all()
                for group in groups:
                    if group.name in allowed_groups:
                        return view_func(request, *args, **kwargs)

            return HttpResponse('You are not authorized to access this page!')

        return wrapper_func

    return decorator
