from django.db import models

class Categories(models.Model):
    category = models.CharField(max_length=50)

class Recipes(models.Model):
    title = models.CharField(max_length=50)
    tagLine = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    heat = models.PositiveSmallIntegerField()
    output = models.PositiveSmallIntegerField()
    difficulty = models.PositiveSmallIntegerField()
    prepTime = models.PositiveSmallIntegerField()
    html = models.TextField()

class Ingredients(models.Model):
    recipe = models.ManyToManyField(Recipes)
    ingredient = models.CharField(max_length=50)

class Tags(models.Model):
    recipe = models.ManyToManyField(Recipes)
    tag = models.CharField(max_length=50)

class Instructions(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=255)
    step = models.PositiveSmallIntegerField()


class IngredientsText(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.CharField(max_length = 255)

class Images(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.PROTECT, null=True)
    url = models.CharField(max_length=255)
    altTag = models.CharField(max_length=50)
    imageHeight = models.PositiveSmallIntegerField()
    imageWidth = models.PositiveSmallIntegerField()
    imageType = models.PositiveSmallIntegerField(null=True)
    imagePosition = models.PositiveSmallIntegerField(null=True)

