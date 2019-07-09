from django.db import models

class Recipes(models.Model):
    title = models.CharField(max_length=50)
    tagLine = models.CharField(max_length=255)
    recipeImages

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ('headline',)

    def __str__(self):
        return self.headline

    #   recipeName: '',
    #   tagLine: '',
    #   recipeImages: [],
    #   availableIngredients: [],
    #   availableCategories: [],
    #   availableTags: [],
    #   instructions: [],
    #   ingredientsText: [],
    #   category: '',
    #   tags: [],
    #   ingredients: [],
    #   heat: '1',
    #   yield: '',
    #   difficulty: '1',
    #   prepTime: '',
    #   html: '',