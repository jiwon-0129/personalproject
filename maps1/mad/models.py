from django.db import models
from django.db.models import fields, manager
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.

class Restaurant(models.Model):
    name=models.CharField(max_length=15, unique=True)
    location=models.CharField(max_length=50,default='',  blank=True)
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)
    signature_menu=models.CharField('Description', max_length=100, default='')
    created_dt=models.DateField('CREATE DATE', auto_now_add=True)
    modify_by=models.DateTimeField('MODIFY DATE', auto_now=True)
    CHOICES=[('family','family'),
    ('friends','friends'),
    ('self','self'),
    ('lovers','lovers'),
    ('senior','senior'),]
    choice=models.CharField(max_length=20, choices=CHOICES, default='self')
    image=models.ImageField(upload_to='images/', default="images/019plate1_114171.png")
    tags=TaggableManager(blank=True)
    class Meta:
        constraints=[models.UniqueConstraint(
            fields=["name","location", "latitude", "longitude"],
            name="unique restaurants",
        ),
        ]
        ordering=('name',)
    def __str__(self):
        return self.name


class Filter(models.Model):
    family=models.BooleanField(default='True')
    friends=models.BooleanField(default='True')
    self=models.BooleanField(default='True')
    lovers=models.BooleanField(default='True')
    senior=models.BooleanField(default='True')



class Comment(models.Model):
    post=models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    point_choices = zip( range(1,6), range(1,6) ) 
    point=models.IntegerField(choices=point_choices, blank=True)
    photo=models.ImageField(upload_to='images/', blank=True)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text
   
