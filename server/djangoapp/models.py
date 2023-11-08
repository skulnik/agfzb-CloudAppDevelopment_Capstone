from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    make_name = models.CharField(null=False, max_length=30, default='Make')
    make_description = models.CharField(null=False, max_length=100, default='Description')

    def __str__(self):
        return "Make: " + self.make_name + "," + \
               "About: " + self.make_description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - __str__ method to print a car make object
class CarModel(models.Model):
    model_name = models.CharField(null=False, max_length=30, default='Model')
    dealer_id = models.IntegerField()
    model_year = models.DateField()
    model_type = models.CharField(null=False, max_length=30, choices=(('sedan', 'Sedan'), ('suv', 'SUV'), ('coupe', 'Coupe'), ('wagon', 'Wagon'), ('truck', 'Truck')))
    model_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Year: " + self.model_year + ", " + \
               "Make: " + self.model_make + "," + \
               "Model: " + self.model_name + "," + \
               "Type: " + self.model_type 

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
