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
    model_year = models.DateField(year_only=True)
    model_type = models.CharField(null=False, max_length=30, default='Type')
    model_make = ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
