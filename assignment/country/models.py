from django.db import models


CONTINENT_CHOICES = [
    ('Asia', 'Asia'),
    ('Europe', 'Europe'),
    ('North America',  'North America'),
    ('Africa', 'Africa'),
    ('Oceania', 'Oceania'),
    ('Antarctica', 'Antarctica'),
    ( 'South America', 'South America')
]


class Country(models.Model):
    code            = models.CharField(max_length=3, unique=True,primary_key=True)
    name            = models.CharField(max_length=52,default='')
    continent       = models.CharField(
                        max_length=13,
                        choices=CONTINENT_CHOICES,
                        default='Asia',
                    )
    region          = models.CharField(max_length=45,default='',null=True)
    surface_area    = models.FloatField(default='0.00',null=True)
    indep_year      = models.SmallIntegerField(default=None,null=True)
    population      = models.IntegerField(default=0,null=True)
    life_expectancy = models.FloatField(default=None,null=True)
    gnp             = models.FloatField(default=None,null=True)
    gnp_old         = models.FloatField(default=None,null=True)
    local_name      = models.CharField(max_length=45,default='',null=True)
    government_form = models.CharField(max_length=45,default='',null=True)
    head_of_state   = models.CharField(max_length=60,default=None,null=True)
    capital         = models.IntegerField(default=None,null=True)
    code2           = models.CharField(max_length=2,default='',null=True)

    class Meta:
        db_table = "country"


class City(models.Model):
    name        = models.CharField(max_length=35)
    country     = models.ForeignKey(Country,on_delete=models.CASCADE)
    district    = models.CharField(max_length=20)
    population  = models.IntegerField()
    # CountryCode = models.ForeignKey(Country)

    class Meta:
        db_table = "city"
    
    def __str__(self):
        return '<' + str(self.name) +'>'

LANGUAGE_ENUMS = [
    ('T','T'),
    ('F','F'),
]

class Languages(models.Model):
    country     = models.ForeignKey(Country,on_delete=models.CASCADE)
    language    = models.CharField(max_length=30)
    is_official = models.CharField(
                    max_length=2,
                    choices= LANGUAGE_ENUMS,
                    default='F'
    )
    percentage  = models.FloatField(default='0.0')

    class Meta:
        db_table = "country_languages"
