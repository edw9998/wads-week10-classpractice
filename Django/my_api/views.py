from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Hero
from .serializers import HeroSerializer

# function for GET requests(retrievements).
@api_view(['GET'])
def getData(req):
    heroes = Hero.objects.all()
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data)

# function for POST requests(insertions).
@api_view(['POST'])
def addHero(req):
    serializer = HeroSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)