from django.contrib import admin
from .models        import Contact, Label

class ContactAdmin(admin.ModelAdmin):
    """
    연락처 모델을 관리 사이트에서 어떻게 표시할지를 정의하는 관리자 클래스입니다.
    """
    list_display = (
        'name', 
        'email', 
        'phone_number', 
        'created_at', 
        'updated_at'
    )
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    filter_horizontal = ('labels',)  # 다대다 관계를 위한 필터링 UI 추가

    def get_queryset(self, request):
        """
        관리 사이트에서 보여줄 쿼리셋을 수정합니다.

        Args:
            request (HttpRequest): 현재 요청 객체입니다.

        Returns:
            QuerySet: 수정된 쿼리셋입니다.
        """
        queryset = super().get_queryset(request)
        
        return queryset

class LabelAdmin(admin.ModelAdmin):
    """
    라벨 모델을 관리 사이트에서 어떻게 표시할지를 정의하는 관리자 클래스입니다.
    """
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# 모델을 관리 사이트에 등록합니다.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Label, LabelAdmin)
