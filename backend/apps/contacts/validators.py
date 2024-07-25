import re
from rest_framework.exceptions  import ValidationError as DRFValidationError
from django.core.exceptions     import ValidationError as DjangoValidationError
from django.core.validators     import EmailValidator


def validate_email(email):
    """
    이메일 형식을 검증합니다.

    Args:
        email (str): 검증할 이메일 주소입니다.

    Raises:
        DRFValidationError: 이메일 형식이 유효하지 않은 경우.
    """
    validator = EmailValidator(message="유효하지 않은 이메일 형식입니다.")
    try:
        validator(email)
    except DjangoValidationError as e:
        raise DRFValidationError(str(e))

def validate_phone_number(phone_number):
    """
    전화번호 형식을 검증합니다.

    Args:
        phone_number (str): 검증할 전화번호입니다.

    Raises:
        DRFValidationError: 전화번호 형식이 유효하지 않은 경우.
    """
    if not re.match(r"^\d{2,4}-\d{3,4}-\d{4}$", phone_number):
        raise DRFValidationError("유효하지 않은 전화번호 형식입니다.")
