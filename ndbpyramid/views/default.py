from pyramid.view import view_config


@view_config(route_name='root', renderer='json')
def root_view(request):
    return True

