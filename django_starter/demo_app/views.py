from django.shortcuts import render

# Create your views here.


from rest_framework.response import Response
from rest_framework.views import APIView


class CustomerView(APIView):

    #method to be called when a GET request is made
    def get(self,request):
        get_message = "This is a message from get request"
        return Response({"message" : get_message})

    #method to be called when a POST request is made
    def post(self,request):
        post_message = "This is a message from post request"
        return Response({"message" : post_message})

