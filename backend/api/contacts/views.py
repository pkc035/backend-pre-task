from rest_framework             import viewsets
from rest_framework.exceptions  import ValidationError as DRFValidationError
from rest_framework.pagination  import PageNumberPagination
from apps.contacts.models       import Contact, Label
from apps.contacts.services     import create_contact, update_contact
from .serializers               import ContactSerializer, LabelSerializer

class ContactPagination(PageNumberPagination):
    """
    연락처 목록 페이지네이션을 위한 클래스입니다.
    """
    page_size = 10  # 페이지당 항목 수를 10으로 설정합니다.

class ContactViewSet(viewsets.ModelViewSet):
    """
    연락처 모델에 대한 CRUD 작업을 처리하는 뷰셋입니다.
    """
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    pagination_class = ContactPagination

    def perform_create(self, serializer):
        """
        새 연락처를 생성할 때 호출되는 메소드입니다.

        Args:
            serializer (ContactSerializer): 유효성 검사를 통과한 직렬화입니다.
        """
        try:
            create_contact(serializer.validated_data)
        except DRFValidationError as e:
            raise DRFValidationError(detail=str(e))
        except Exception as e:
            print(e)
            raise DRFValidationError("연락처 생성 중 오류가 발생했습니다.") from e

    def perform_update(self, serializer):
        """
        기존 연락처를 업데이트할 때 호출되는 메소드입니다.

        Args:
            serializer (ContactSerializer): 유효성 검사를 통과한 직렬화입니다.
        """
        try:
            update_contact(self.get_object(), serializer.validated_data)
        except DRFValidationError as e:
            raise DRFValidationError(detail=str(e))
        except Exception as e:
            raise DRFValidationError("연락처 업데이트 중 오류가 발생했습니다.") from e

class LabelViewSet(viewsets.ModelViewSet):
    """
    라벨 모델에 대한 CRUD 작업을 처리하는 뷰셋입니다.
    """
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
