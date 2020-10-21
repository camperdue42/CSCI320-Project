from django.db import models

#reference: https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types
#PostgreSQL reference: https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/fields/

# Create your models here.
class User(models.Model):
	UID = models.PositiveIntegerField(primary_key=True) #primary_key=True implies null=False and unique=True
	Name = models.CharField(max_length=100)
	StorageLocations = models.ForeignKey(StorageLocation, on_delete=models.CASCADE) #not too sure about this one

class Recipe(models.Model):
	RecipeName = models.CharField(max_length=100, primary_key=True)
	PreparationTime = models.PositiveIntegerField() #I picked this so it would be a minute counter. Theoretically could be a time field
	Price = models.DecimalField(max_digits=5, decimal_places=2) #should go up to 999.99
	ServingSize = models.PositiveIntegerField()
	Users = models.ManyToManyField(User, through='Makes')
	Utensils = models.ManyToManyField(Utensil)
	#PreviouslyMade is derived from DatesMade relationship attribute

class Makes(models.Model):
	DatesMade = ArrayField(
		models.DateField(auto_now_add=False, auto_now=False) #dates will not be automatically added on creation or update. Manually add data
	)

class Step(models.Model):
	StepNumber = models.PositiveIntegerField(primary_key=True)
	QuantitiesOfIngredients = HStoreField() #PostgreSQL specific field, functions like dict. see ref
	RecipeName = models.ForeignKey(Recipe, on_delete=models.CASCADE) #many to one w/ recipe
	Instructions = models.TextField(max_length=400)
	Ingredients = models.ManyToManyField(Ingredient) #many to many w/ Ingredient

class Ingredient(models.Model):
	IngredientName = models.CharField(max_length=100, primary_key=True)
	AmountLeft = models.PositiveIntegerField()
	StorageLocation = models.ForeignKey(StorageLocation, on_delete=models.CASCADE) #not too sure about this one

class StorageLocation(models.Model):
	LocationID = models.PositiveIntegerField(primary_key=True)
	LocationType = models.BooleanField()

class Utensil(models.Model):
	UtensilName = models.CharField(max_length=100, primary_key=True)