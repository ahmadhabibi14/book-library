from .common_response import *

class ContentTypeMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    content_type = request.headers.get('Content-Type')

    if request.method == 'POST' and request.path != request.path.startswith('/api/media'):
      if content_type and 'application/json' not in content_type:
        return JsonResponseWrapper.error(message='Invalid Content-Type, try to use "application/json" instead !', errors='Content-Type not allowed !', status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    response = self.get_response(request)
    return response