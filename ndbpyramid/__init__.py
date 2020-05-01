from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    with Configurator(settings=settings) as config:
        config.include('.routes')
        config.scan()
        # Comment this line to stop memory leak
        config.add_tween('ndbpyramid.datastore_tween.datastore_tween_factory')

    return config.make_wsgi_app()
