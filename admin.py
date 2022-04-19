from telnetlib import STATUS
from django.contrib import admin
#Post 모델을 임포트, admin과 같은 경로 상에 있기 때문에 .models
from .models import Faq
#TabularInline, StackedInline 어떻게 배치할 것인가의 차이, 1:n의 관계일 때, n을 어떻게 할 것인지.

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    #(괄호 안에는 모델의 속성명을 넣어주는 것.)
    list_display = ('id', 'title', 'question', 'comment', 'created_at', 'created_by', 'view_count', 'modified_by', 'modified_at')
    #list_editable = ('content') -> 리스트 화면에서 수정이 바로 가능하다.
    list_filter = ('created_at',)
    #튜플형태 () 와 리스트형태 [] 는 다르다. 튜플형태일 때 마지막에 콤마를 넣어야한다.
    search_fields = ('id', )
    #작성자를 넣게 된다면... lgitookup
    #search_fields = ('id', 'writer__username') 언더바_ *2
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    #readonly속성을 줌으로써, post내부에 게시날짜가 보이게 함.
    readonly_fields = ('created_at', )

    #admin에서 중요한 기능인, actions를 정의해보자.
    actions = ['make_published']

    #인자값으로 받은 세개의 정보
    def make_published(modeladmin, request, queryset):
        #admin action에 대한 결과가 queryset에 들어온다.
        for item in queryset:
            item.title='운영 규정 위반으로 인한 게시글 삭제 처리.'
            item.save()

        #queryset.update(status='p')