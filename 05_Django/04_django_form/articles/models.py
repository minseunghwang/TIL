from django.db import models
from django.conf import settings

# Create your models here.
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return f'[{self.pk}] {self.content}'


class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'


class Comment(models.Model):
    # Comment -> 이중 1:N 관계 (Article, User)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 메타데이터 옵션 설정 -> 정렬 기능 사용
    class Meta:
        ordering = ['-pk',]
    
    # 객체 표현 방식
    def __str__(self):
        return f'{self.content}'

class Mapmap(models.Model):
    road_num = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    created_at = models.CharField(max_length=30)
    xposition = models.CharField(max_length=30)
    yposition = models.CharField(max_length=30)

    class Meta:
        ordering = ['-pk',]

class CCTV(models.Model):
    CCTV_MANAGEMENT = models.CharField(max_length=30)
    CCTV_ADDRESS_NAME = models.CharField(max_length=30)
    CCTV_LONGITUDE = models.CharField(max_length=20)
    CCTV_LATITUDE = models.CharField(max_length=20)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return f'{self.pk}'

    







# from django.db import models
# from django.conf import settings
# # Create your models here.


# class StreetlampKind(models.Model):
#     # STR_KIND = models.CharField(max_length=15, unique=True)
#     STR_RADIUS = models.CharField(max_length=15, unique=True)

#     class Meta:
#         ordering = ['pk', ]

#     def __str__(self):
#         return f'{self.pk}'


# class Streetlamp(models.Model):
#     STR_ADDRESS_NAME = models.CharField(max_length=30)
#     STR_KIND = models.ForeignKey(StreetlampKind, on_delete=models.CASCADE)
#     STR_LONGITUDE = models.CharField(max_length=20)
#     STR_LATITUDE = models.CharField(max_length=20)

#     class Meta:
#         ordering = ['pk', ]

#     def __str__(self):
#         return f'{self.pk}'


# class CCTVKind(models.Model):
#     # CCTV_KIND = models.CharField(max_length=15, unique=True)
#     CCTV_RADIUS = models.CharField(max_length=15, unique=True)

#     class Meta:
#         ordering = ['pk', ]

#     def __str__(self):
#         return f'{self.pk}'


# class CCTV(models.Model):
#     CCTV_ADDRESS_NAME = models.CharField(max_length=30)
#     CCTV_KIND = models.ForeignKey(CCTVKind, on_delete=models.CASCADE)
#     CCTV_LONGITUDE = models.CharField(max_length=20)
#     CCTV_LATITUDE = models.CharField(max_length=20)

#     class Meta:
#         ordering = ['pk', ]

#     def __str__(self):
#         return f'{self.pk}'


class StreetlampKind(models.Model):
    # STR_KIND = models.CharField(max_length=15, unique=True)
    STR_RADIUS = models.CharField(max_length=15, unique=True)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return f'{self.pk}'


class Streetlamp(models.Model):
    STR_ADDRESS_NAME = models.CharField(max_length=30)
    STR_KIND = models.ForeignKey(StreetlampKind, on_delete=models.CASCADE)
    STR_LONGITUDE = models.CharField(max_length=20)
    STR_LATITUDE = models.CharField(max_length=20)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return f'{self.pk}'


class CCTVKind(models.Model):
    # CCTV_KIND = models.CharField(max_length=15, unique=True)
    CCTV_RADIUS = models.CharField(max_length=15, unique=True)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return f'{self.pk}'


class CCTV(models.Model):
    CCTV_ADDRESS_NAME = models.CharField(max_length=30)
    CCTV_KIND = models.ForeignKey(CCTVKind, on_delete=models.CASCADE)
    CCTV_LONGITUDE = models.CharField(max_length=20)
    CCTV_LATITUDE = models.CharField(max_length=20)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return f'{self.pk}'
