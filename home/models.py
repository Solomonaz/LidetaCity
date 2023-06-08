from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User


class CabinetModel(models.Model):
    cabinete_name = models.CharField(max_length=255)
    education_preparation = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(blank=True, max_length=255)
    fax = models.CharField( max_length=255, blank=True)
    cabinete_image = models.ImageField(upload_to='media/cabinetes/')
    address = models.CharField(blank=True, max_length=255)
    cabinete_title = models.CharField(blank=True, max_length=255)
    work_experience = models.IntegerField()
    cabinate_message = models.TextField()


    def __str__(self):
        return self.cabinete_name

class CarouselModel(models.Model):
    carousel_image = models.ImageField(upload_to='media/carousels/')
    carousel_title = models.TextField()

    def get_title(self):
        return self.carousel_title.split('.', 1)[0]

class SubCityModel(models.Model):
    logo = models.ImageField(blank=True ,upload_to='media/logo/')
    subcity_address = models.CharField(blank=True, max_length=255)
    subcity_phone_number = models.CharField(blank=True, max_length=20)
    subcity_email = models.EmailField(blank=True, max_length=255)
    # chief_executive_name = models.CharField(max_length=200)
    # chief_executive_image = models.ImageField(upload_to='media/chief_executive/')
    # chief_executive_message = models.TextField(blank=True)
    # carousel_image = models.ImageField(blank=True, upload_to='media/carousels/')
    # carousel_title = models.TextField(blank=True)
    area_of_subcity = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    elivation = models.IntegerField(null=True, blank=True)
    fax = models.CharField(blank=True,max_length=200)
    pobox = models.CharField(blank=True, max_length=20)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)


    def __str__(self):
        return self.subcity_email


class WoredaModel(models.Model):
    woreda_name = models.CharField(max_length=255)
    woreda_image = models.ImageField(upload_to='media/woredas')
    email = models.EmailField(blank=True)
    fax = models.CharField(blank=True,max_length=200)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    pobox = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.woreda_name

class GalleryModel(models.Model):
    gallery_title = models.CharField(max_length=100)
    gallery_image = models.ImageField(upload_to='media/gallery/')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    # def desc(self):
    #     return self.description[:10]
    
    def __str__(self):
        return self.gallery_title
    
class OfficeModel(models.Model):
    office_name  = models.CharField(max_length=255)
    office_image = models.ImageField(upload_to='media/offices/')

    def __str__(self):
        return self.office_name

class CommentModel(models.Model):
    # message_on_comment = models.TextField()
    commented_person_name = models.CharField(max_length=255) # responsible guy for the complain
    comment_sector = models.CharField(max_length=255) # responsible sector
    comment_body = models.TextField() # complain
    date_commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_commented',)

    def __str__(self):
        return self.comment_sector
    
class NewsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_title = models.CharField(blank=True,  max_length=255)
    news_body = models.TextField(blank=True,)
    news_image = models.ImageField(blank=True,upload_to='media/news_image/')
    date_created = models.DateTimeField(default=timezone.now)

    @property
    def is_recent(self):
        # Defining criteria for recent posts
        threshold = timezone.now() - timedelta(days=7)
        return self.date_created >= threshold

    def get_news_body(self):
        return self.news_body[:50]

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.user.username

class HeadlineNewsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline_news_title = models.CharField(blank=True,max_length=255)
    headline_news_body = models.TextField()
    headline_news_image = models.ImageField(blank=True,upload_to='media/headline_news')
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.user.username
    
class TenderModel(models.Model):
    tender_title = models.CharField(max_length=255)
    tender_description = models.TextField()
    date_created = models.DateTimeField()
    expired_date = models.DateTimeField()

    def __str__(self):
        return self.tender_title

class VacancyModel(models.Model):
    vacancy_title = models.CharField(max_length=255)
    vacancy_description = models.TextField()
    date_created = models.DateTimeField()
    expired_date = models.DateTimeField()

    def __str__(self):
        return self.vacancy_title
class EventModel(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_image = models.ImageField(upload_to='media/event_image/')

    def __str__(self):
        return self.event_name

# class AboutModel(models.Model):
#     about = models.TextField()

