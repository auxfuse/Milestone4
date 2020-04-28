from django.db import models

"""List of payment frequency types to be passed into dropdown `frequency` for 
each frequency type."""
frequency_types = [
    ('', 'Select Payment Frequency Type'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('biannual', 'Biannual'),
    ('yearly', 'Yearly')
]


# Models
class Membership(models.Model):
    type = models.CharField(max_length=50)
    brief_desc = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    frequency = models.CharField(max_length=29, choices=frequency_types)

    def __str__(self):
        return "#{0} - {1}".format(
            self.id, self.type)
