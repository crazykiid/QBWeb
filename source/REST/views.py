from rest_framework.views import APIView
from rest_framework.response import Response


# ~/
class WelcomeView(APIView):
  
  def get(self, request, format=None):
    data = {
      'response' : 200,
      'message' : 'welcome to qb api v1.0'
    }
    return Response(data)