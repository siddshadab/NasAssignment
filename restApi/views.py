from rest_framework.exceptions import Throttled
from restApi.customthrottle import AnonTenPerTenSecondsThrottle
from restApi.models import ParkingSystem, SlotMaster
from restApi.serializers import ParkingSystemSerializer, CheckOutSerializer,ParkingSystemSubmitSerializer,CheckOutSubmitSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from django.db.models import Q
import datetime


class get_check_out_details(viewsets.ModelViewSet):
    throttle_classes = [AnonTenPerTenSecondsThrottle]

    def throttled(self, request, wait):
        raise Throttled(detail={
            "message": "request limit exceeded",
            "availableIn": f"{wait} seconds",
            "throttleType": "type"
        })

    queryset = ParkingSystem.objects.all()
    serializer_class = CheckOutSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        return ParkingSystem.objects.filter()

    def create(self, request):
        queryset = ParkingSystem.objects.all()
        serializer_class = CheckOutSubmitSerializer
        queryset = queryset.filter(Q(slot_number=request.data['slot_number']) | Q(is_checked_out=0))
        try:
            queryset[0].id
        except:
            content = {'Please contact Admin Team': 'Slot Not Allotted to any Car'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
            print(queryset)
        ParkingSystem.objects.filter(pk=queryset[0].id).update(is_checked_out=1, out_date_time=datetime.datetime.now())
        SlotMaster.objects.filter(pk=request.data['slot_number']).update(is_slot_available=0)
        return Response(status=status.HTTP_201_CREATED)


class get_parking(viewsets.ModelViewSet):
    throttle_classes = [AnonTenPerTenSecondsThrottle]

    def throttled(self, request, wait):
        raise Throttled(detail={
            "message": "request limit exceeded",
            "availableIn": f"{wait} seconds",
            "throttleType": "type"
        })

    queryset = ParkingSystem.objects.all()
    serializer_class = ParkingSystemSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = ParkingSystem.objects.all()
        car_number = self.request.query_params.get('car_number', None)
        print(car_number)
        slot_number = self.request.query_params.get('slot_number', None)
        if car_number is not None:
            queryset = queryset.filter(car_number=car_number, is_checked_out=0)
        elif slot_number is not None:
            queryset = queryset.filter(slot_number=slot_number, is_checked_out=0)
        return queryset

    def create(self, request):
        queryset = SlotMaster.objects.all()
        queryset = queryset.filter(Q(is_slot_available=0) | Q(is_slot_available=None))
        try:
            queryset[0].id
        except:
            content = {'Please contact Admin Team': 'Slots Not Avalable'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
            print(queryset)
        request.data._mutable = True
        request.data['slot_number'] = queryset[0].id
        request.data['is_checked_out'] = 0
        request.data._mutable = False
        SlotMaster.objects.filter(pk=queryset[0].id).update(is_slot_available=1)
        serializer = ParkingSystemSubmitSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)
