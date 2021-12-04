from django.shortcuts import render
from api.models import Experience, Skills
from api.serializer import ExperienceSerializer, SkillSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
 

class PortFolioAPI(APIView):
    def get(self,request):
        skill_query = Skills.objects.all()
        experience_query = Experience.objects.all()

        skill_serializer = SkillSerializer(skill_query,many=True)
        experience_serializer = ExperienceSerializer(experience_query,many=True)


        response_data = {
            "method" : "GET",
            "message" : "data fetch successfull",
            "statuscode" : 200,
            "skills" : skill_serializer.data,
            "experiences" : experience_serializer.data
        }

        return Response(response_data,status=status.HTTP_200_OK)