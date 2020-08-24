from ndbpyramid import datastore_client


class datastore_tween_factory(object):
    def __init__(self, handler, registry):
        self.handler = handler
        self.registry = registry

    def __call__(self, request):

        with datastore_client.context():
            response = self.handler(request)

        return response
