from django.apps import AppConfig

class ContactsConfig(AppConfig):
    """
    연락처 앱의 구성을 정의하는 클래스입니다.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.contacts'

    def ready(self):
        """
        앱이 준비되었을 때 호출되는 메소드입니다.
        시그널 핸들러를 임포트하여 앱의 시그널을 연결합니다.
        """
        import apps.contacts.signals
