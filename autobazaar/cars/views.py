from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Car
from .serializers import CarListSerializer, CarDetailSerializer


class CarListView(APIView):
    def get(self, request):
        cars = Car.objects.filter(sold=False)
        serializer = CarListSerializer(cars, many=True)
        return Response(serializer.data)



class CarDetailView(APIView):
    def get(self, request, pk):
        car = Car.objects.get(id=pk, sold=False)
        serializer = CarDetailSerializer(car)
        return Response(serializer.data)