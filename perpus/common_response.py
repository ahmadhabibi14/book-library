from rest_framework.response import Response
from rest_framework import status

class JsonResponseWrapper:
  @staticmethod
  def success(data=None, message="Success", status_code=status.HTTP_200_OK):
    return Response({
      "status": "success",
      "message": message,
      "data": data
    }, status=status_code)
  
  @staticmethod
  def created(data=None, message="Success", status_code=status.HTTP_201_CREATED):
    return Response({
      "status": "created",
      "message": message,
      "data": data
    }, status=status_code)

  @staticmethod
  def error(message="Error", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    response_data = {
      "status": "error",
      "message": message
    }

    if errors:
      response_data["errors"] = errors

    return Response(response_data, status=status_code)
  
  @staticmethod
  def errorserver(message="Error", errors=None, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
    response_data = {
      "status": "error",
      "message": message
    }

    if errors:
      response_data["errors"] = errors

    return Response(response_data, status=status_code)