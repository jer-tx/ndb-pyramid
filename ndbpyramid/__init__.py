from pyramid.config import Configurator
from google.cloud import ndb
import google.cloud.logging

client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()

datastore_client = ndb.Client(project='my-project')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    with Configurator(settings=settings) as config:
        config.include('.routes')
        config.scan()
        # Comment this line to stop memory leak
        config.add_tween('ndbpyramid.datastore_tween.datastore_tween_factory')

    return config.make_wsgi_app()
