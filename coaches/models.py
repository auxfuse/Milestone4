from django.db import models
from datetime import datetime

qualification = [
    ('', ''),
    ('cf lvl1 trainer', 'CF Lvl1 Trainer'),
    ('strength & conditioning specialist (cscs)', 'Strength & Conditioning '
                                                  'Specialist (cscs)'),
    ('precision nutrition lvl1 certificate', 'Precision Nutrition Lvl1 '
                                             'Certificate'),
    ('neuromuscular therapist', 'Neuromuscular Therapist'),
    ('weightlifting lvl1', 'Weightlifting Lvl1'),
    ('exercise & fitness from ul', 'Exercise & Fitness from UL'),
    ('bsc in strength & conditioning', 'BSc in Strength & Conditioning')
]


# Create your models here.
class StaffMember(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(default='default.jpg',
                              upload_to='media/%Y/%m/%d/')
    brief_desc = models.CharField(max_length=300)
    qualification_1 = models.CharField(max_length=41, choices=qualification,
                                       blank=True)
    qualification_2 = models.CharField(max_length=41, choices=qualification,
                                       blank=True)
    qualification_3 = models.CharField(max_length=41, choices=qualification,
                                       blank=True)
    qualification_4 = models.CharField(max_length=41, choices=qualification,
                                       blank=True)
    currently_employed = models.BooleanField(default=True)
    employed_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
