import re
from rest_framework.exceptions  import ValidationError as DRFValidationError
from django.db                  import transaction
from django.core.exceptions     import ValidationError as DjangoValidationError
from apps.contacts.models       import Contact, Label
from apps.contacts.validators   import validate_email, validate_phone_number


@transaction.atomic
def create_contact(data):
    """
    새 연락처를 생성하고 해당 연락처에 라벨을 할당합니다.

    Args:
        data (dict): 연락처 정보와 라벨이 포함된 딕셔너리입니다.

    Returns:
        Contact: 생성된 연락처 인스턴스입니다.
    
    Raises:
        DRFValidationError: 이메일 또는 전화번호 형식이 유효하지 않거나, 연락처 생성 중 문제가 발생한 경우.
    """
    try:
        # 이메일과 전화번호 유효성 검사
        validate_email(data.get('email'))
        validate_phone_number(data.get('phone_number'))
        
        labels_data = data.pop('labels', [])
        contact = Contact.objects.create(**data)
        
        for label_data in labels_data:
            label, _ = Label.objects.get_or_create(name=label_data['name'])
            contact.labels.add(label)
        
        return contact
    except DjangoValidationError as e:
        # 이메일 또는 전화번호 유효성 검증 실패 시
        raise e
    except Exception as e:
        # 기타 예외 발생 시
        print(e)
        raise DRFValidationError("연락처 생성 중 문제가 발생했습니다.") from e

def update_contact(instance, data):
    """
    기존 연락처를 업데이트하고 해당 연락처의 라벨을 수정합니다.

    Args:
        instance (Contact): 업데이트할 연락처 인스턴스입니다.
        data (dict): 업데이트된 연락처 정보와 라벨이 포함된 딕셔너리입니다.

    Returns:
        Contact: 업데이트된 연락처 인스턴스입니다.
    
    Raises:
        DRFValidationError: 이메일 또는 전화번호 형식이 유효하지 않거나, 연락처 업데이트 중 문제가 발생한 경우.
    """
    try:
        # 이메일과 전화번호 유효성 검사
        if 'email' in data:
            validate_email(data.get('email'))
        if 'phone_number' in data:
            validate_phone_number(data.get('phone_number'))

        labels_data = data.pop('labels', [])
        
        # 연락처 필드 업데이트
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()

        # 라벨 업데이트
        instance.labels.clear()
        for label_data in labels_data:
            label, _ = Label.objects.get_or_create(name=label_data['name'])
            instance.labels.add(label)
        
        return instance
    except DjangoValidationError as e:
        # 이메일 또는 전화번호 유효성 검증 실패 시
        raise e
    except Exception as e:
        # 기타 예외 발생 시
        raise DRFValidationError("연락처 업데이트 중 문제가 발생했습니다.") from e
