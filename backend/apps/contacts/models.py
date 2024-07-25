from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(models.Model):
    # 필수 필드
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    # 선택적 필드
    profile_picture = models.URLField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    # 날짜/시간 필드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 다대다 관계 필드
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.name
