from django.db.models.signals   import post_save, pre_save
from django.dispatch            import receiver
from .models                    import Contact

@receiver(post_save, sender=Contact)
def log_contact_creation(sender, instance, created, **kwargs):
    """
    연락처가 저장된 후 호출되는 시그널 핸들러입니다.

    Args:
        sender (Model): 시그널을 발생시킨 모델입니다.
        instance (Contact): 저장된 연락처 인스턴스입니다.
        created (bool): 연락처가 새로 생성된 경우 True, 업데이트된 경우 False입니다.
        **kwargs: 추가적인 인자를 받을 수 있습니다.
    """
    if created:
        print(f'새 연락처가 생성되었습니다: {instance.name}')
    else:
        print(f'연락처가 업데이트되었습니다: {instance.name}')

@receiver(pre_save, sender=Contact)
def log_contact_update(sender, instance, **kwargs):
    """
    연락처가 저장되기 전에 호출되는 시그널 핸들러입니다.

    Args:
        sender (Model): 시그널을 발생시킨 모델입니다.
        instance (Contact): 저장될 연락처 인스턴스입니다.
        **kwargs: 추가적인 인자를 받을 수 있습니다.
    """
    if instance.id:
        print(f'연락처가 업데이트 중입니다: {instance.name}')
