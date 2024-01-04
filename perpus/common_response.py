from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled

class JsonResponseWrapper:
  @staticmethod
  def success(data=None, message="Success", status_code=status.HTTP_200_OK):
    return JsonResponse({
      "code": status_code,
      "status": "success",
      "message": message,
      "data": data
    }, status=status_code)
  
  @staticmethod
  def created(data=None, message="Success", status_code=status.HTTP_201_CREATED):
    return JsonResponse({
      "code": status_code,
      "status": "created",
      "message": message,
      "data": data
    }, status=status_code)

  @staticmethod
  def error(message="Error", errors="Error", status_code=status.HTTP_400_BAD_REQUEST):
    response_data = {
      "code": status_code,
      "status": "error",
      "errors": errors,
      "message": message
    }

    return JsonResponse(response_data, status=status_code)
  
  @staticmethod
  def errormethod(message="Use GET method instead"):
    response_data = {
      "code": status.HTTP_405_METHOD_NOT_ALLOWED,
      "status": "error",
      "errors": "Method not allowed !",
      "message": message
    }

    return JsonResponse(response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
  
  @staticmethod
  def errorserver(message="Error", errors="Error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
    response_data = {
      "code": status_code,
      "status": "error",
      "errors": errors,
      "message": message
    }

    return JsonResponse(response_data, status=status_code)

def ThrottledHandler(exc, context):
  response = exception_handler(exc, context)

  if isinstance(exc, Throttled):
    response_data = {
      "code": status.HTTP_429_TOO_MANY_REQUESTS,
      "status": "error",
      "errors": "Too many requests !",
      "message": "Try again in %d seconds"%exc.wait
    }
    response.data = response_data

  return response