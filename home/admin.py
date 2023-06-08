from django.contrib import admin
from . models import SubCityModel, WoredaModel, CabinetModel, GalleryModel, CommentModel, EventModel, VacancyModel,TenderModel, OfficeModel, NewsModel, HeadlineNewsModel, CarouselModel

class SubCityAdmin(admin.ModelAdmin):
    list_display = ('area_of_subcity','population','elivation','fax','pobox')

class CabinateAdmin(admin.ModelAdmin):
    list_display = ('cabinete_name','education_preparation','phone_number','email','fax','address','cabinete_title','work_experience')

class WoredaAdmin(admin.ModelAdmin):
    list_display = ('woreda_name','phone_number','address','fax','email','pobox')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('gallery_title','date_created','description')

class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id','office_name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commented_person_name','comment_sector','comment_body','date_commented')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('user','news_title','news_body','date_created')

class HeadlineNewsAdmin(admin.ModelAdmin):
    list_display = ('user','headline_news_title','headline_news_body','date_created')

class TenderAdmin(admin.ModelAdmin):
    list_display = ('tender_title','tender_description','date_created','expired_date')    

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('vacancy_title','vacancy_description','date_created','expired_date')  

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_description')

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('carousel_title', )



admin.site.register(CabinetModel, CabinateAdmin)
admin.site.register(WoredaModel, WoredaAdmin)
admin.site.register(GalleryModel,GalleryAdmin)
admin.site.register(CommentModel,CommentAdmin)
admin.site.register(SubCityModel, SubCityAdmin)
admin.site.register(EventModel, EventAdmin)
admin.site.register(OfficeModel,OfficeAdmin)
admin.site.register(VacancyModel, VacancyAdmin)
admin.site.register(TenderModel, TenderAdmin)
admin.site.register(NewsModel,NewsAdmin)
admin.site.register(HeadlineNewsModel, HeadlineNewsAdmin)
admin.site.register(CarouselModel, CarouselAdmin)