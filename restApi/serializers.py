from rest_framework import serializers
from restApi.models import ParkingSystem, SlotMaster


class SlotMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotMaster
        fields = ('id', 'name', 'is_slot_available')


class ParkingSystemSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSystem
        fields = ['id', 'car_number', 'slot_number', 'customer_name', 'contact_no', 'in_date_time', 'out_date_time',
                  'is_checked_out']


class ParkingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSystem
        fields = ['id', 'car_number', 'slot_number', 'customer_name', 'contact_no', 'in_date_time', 'out_date_time',
                  'is_checked_out']
        read_only_fields = ('slot_number', 'is_checked_out')

class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSystem
        fields = ['id', 'car_number', 'slot_number', 'customer_name', 'contact_no', 'in_date_time', 'out_date_time',
                  'is_checked_out']
        read_only_fields = ('car_number', 'customer_name', 'contact_no',  'is_checked_out')

class CheckOutSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSystem
        fields = ['id', 'car_number', 'slot_number', 'customer_name', 'contact_no', 'in_date_time', 'out_date_time',
                  'is_checked_out']


