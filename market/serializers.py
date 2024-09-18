from rest_framework import serializers

from .models import CustomUser

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'photo']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print('create function')
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def validate(self, data):
        photo = data['photo']
        password = data['password']
        if not password.isalnum:
            raise serializers.ValidationError('parol harf va raqamlardan iborat bolishi kerak')
        if data['password']
        print(photo.name)
        if not photo.name.endswith(("png", "jpg", 'PNG', "Jpg", "JPG", "JPEG", "jpeg", "Webp")):
            raise serializers.ValidationError('notogri file kiritildi.')
        print(dir(photo))
        print("000000")
            # raise serializers.ValidationError("Username allaqachon mavjud..")
        return data

    def validate_photo(self, value):
        ...

        return value
        