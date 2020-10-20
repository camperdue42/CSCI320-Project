from django.db import models

#reference: https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types

# Create your models here.
class User(models.Model):
	UID = models.PositiveIntegerField(primary_key=True) #primary_key=True implies null=False and unique=True
	Name = models.CharField(max_length=100)

class Recipe(models.Model):
	RecipeName = models.CharField(max_length=100, primary_key=True)
	PreparationTime = models.PositiveIntegerField() #could this be a time field? rn I picked this so it would be a minute counter
	Price = models.DecimalField(max_digits=5, decimal_places=2) #should go up to 999.99
	ServingSize = models.PositiveIntegerField()
	Users = models.ManyToManyField(User) #not sure about how to define relationships tbh. idk if this is even necessary
	#PreviouslyMade is derived from DatesMade relationship attribute

class Step(models.Model):
	StepNumber = models.PositiveIntegerField(primary_key=True)
	QuantitiesOfIngredients = #don't know how to represent this one
	RecipeName = models.ForeignKey(Recipe, on_delete=models.CASCADE) #how to indicate foreign key?
	Instructions = models.TextField(max_length=400)
	Ingredients = models.ManyToManyField(Ingredient)

class Ingredient(models.Model):
	IngredientName = models.CharField(max_length=100, primary_key=True)
	AmountLeft = models.PositiveIntegerField()

class StorageLocation(models.Model):
	LocationID = models.PositiveIntegerField(primary_key=True)
	LocationType = models.BooleanField()

class Utensil(models.Model):
	UtensilName = models.CharField(max_length=100, primary_key=True)