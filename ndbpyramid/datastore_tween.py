from google.cloud import ndb


class datastore_tween_factory(object):
    def __init__(self, handler, registry):
        self.handler = handler
        self.registry = registry

    def __call__(self, request):
        datastore_client = ndb.Client(project='your-gcp-project')
        with datastore_client.context():
            response = self.handler(request)

        return response
