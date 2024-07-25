from rest_framework         import serializers
from apps.contacts.models   import Contact, Label

class LabelSerializer(serializers.ModelSerializer):
    """
    라벨 모델을 직렬화하는 클래스입니다.
    """
    class Meta:
        model = Label
        fields = ['id', 'name']

class ContactSerializer(serializers.ModelSerializer):
    """
    연락처 모델을 직렬화하는 클래스입니다.
    """
    labels = LabelSerializer(many=True, required=False)

    class Meta:
        model = Contact
        fields = [
            'id', 
            'profile_picture', 
            'name', 
            'email', 
            'phone_number', 
            'company', 
            'position', 
            'memo', 
            'labels', 
            'address', 
            'birthday', 
            'website', 
            'created_at'
        ]

    def create(self, validated_data):
        """
        유효성 검사를 통과한 데이터로 새 연락처를 생성합니다.

        Args:
            validated_data (dict): 유효성 검사를 통과한 데이터입니다.

        Returns:
            Contact: 생성된 연락처 인스턴스입니다.
        """
        labels_data = validated_data.pop('labels', [])
        contact = Contact.objects.create(**validated_data)

        for label_data in labels_data:
            label, _ = Label.objects.get_or_create(name=label_data['name'])
            contact.labels.add(label)

        return contact

    def update(self, instance, validated_data):
        """
        주어진 연락처 인스턴스를 업데이트합니다.

        Args:
            instance (Contact): 업데이트할 연락처 인스턴스입니다.
            validated_data (dict): 유효성 검사를 통과한 데이터입니다.

        Returns:
            Contact: 업데이트된 연락처 인스턴스입니다.
        """
        labels_data = validated_data.pop('labels', [])
        instance = super().update(instance, validated_data)

        # 기존 라벨을 모두 삭제하고 새 라벨을 추가합니다.
        instance.labels.clear()
        for label_data in labels_data:
            label, _ = Label.objects.get_or_create(name=label_data['name'])
            instance.labels.add(label)

        return instance
