from rest_framework import serializers
from .models import Item, Category


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
        if value < 0: raise serializers.ValidationError('can`t be negative')
        return value

    def validate_height(self, value):
        if value < 0: raise serializers.ValidationError('can`t be negative')
        return value

    def validate_length(self, value):
        if value < 0: raise serializers.ValidationError('can`t be negative')
        return value

    def validate_weight(self, value):
        if value < 0: raise serializers.ValidationError('can`t be negative')
        return value

    def validate_expiration_date(self, value):
        if self.initial_data.get('category') and ('food' in self.initial_data('category') or 'drink' in self.initial_data('category')):
            if value is None:
                raise serializers.ValidationError('expiration_date is required for food and drink categories')
        return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'