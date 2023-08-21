class ArticlesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.htmx = True if 'Hx-Request' in request.headers else False
        response = self.get_response(request)
        return response
