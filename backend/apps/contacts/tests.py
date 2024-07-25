from django.test    import TestCase
from .models        import Contact

class ContactSignalTestCase(TestCase):
    def setUp(self):
        """
        테스트 실행 전에 호출되는 메소드입니다.
        초기화 작업을 수행합니다.
        """
        self.contact = Contact.objects.create(
            name="test",
            email="test@test.com",
            phone_number="01000000000"
        )

    def test_contact_creation(self):
        """
        연락처가 생성될 때의 시그널이 제대로 동작하는지 테스트합니다.
        """
        contact = Contact.objects.create(
            name="new_test",
            email="new_test@test.com",
            phone_number="01011112222"
        )

    def test_contact_update(self):
        """
        연락처가 업데이트될 때의 시그널이 제대로 동작하는지 테스트합니다.
        """
        self.contact.email = "test2@test.com"
        self.contact.save()

