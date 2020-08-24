import logging

from pyramid.view import view_config


@view_config(route_name='root', renderer='json')
def root_view(request):
    logging.info("Test")
    return True

