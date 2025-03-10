from rest_framework import serializers
from .models import Item, Category
from datetime import date

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    forbidden_symbols = "!@#$%^&*"

    def validate_name(self, value):
        if len(value) < 5: raise serializers.ValidationError('min 5 symbols')

        forbidden_symbols = "!@#$%^&*"
        for i in value:
            if i in forbidden_symbols: raise serializers.ValidationError(f'forbidden symbols {forbidden_symbols}')
        return value

    def validate_description(self, value):
        if len(value.split()) < 2: raise serializers.ValidationError('at least 2 words')
        forbidden_symbols = "!@#$%^&*"
        for i in value:
            if i in forbidden_symbols: raise serializers.ValidationError(f'forbidden symbols {forbidden_symbols}')
        return value

    def validate_width(self, value):
        if value and value < 0: raise serializers.ValidationError('can`t be negative')
        return value

    def validate_height(self, value):
        if value and value < 0: raise serializers.ValidationError('can`t be negative')
        return value

    def validate_weight(self, value):
        if value and value< 0: raise serializers.ValidationError('can`t be negative')
        return value

    def validate_expiration_date(self, value):
        if value < date.today(): raise serializers.ValidationError('expiration_date should not be from past')
        return value

    def validate(self, data):
        category = data.get('category')
        expiration_date = data.get('expiration_date')
        if category.name.lower() in ('food', 'drink') and not expiration_date:
            raise serializers.ValidationError('expiration_Date necessary for food and drinks')
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'