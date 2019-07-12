import graphene  
from graphene_django.types import DjangoObjectType
from salsa.models import Categories, Recipes, Ingredients, Tags, Instructions, IngredientsText, Images

# Create a GraphQL type for the actor model
class RecipeType(DjangoObjectType):  
    class Meta:
        model = Recipes

# Create a GraphQL type for the movie model
class CategoryType(DjangoObjectType):  
    class Meta:
        model = Categories

class IngredientType(DjangoObjectType):  
    class Meta:
        model = Ingredients

class TagType(DjangoObjectType):  
    class Meta:
        model = Tags

class InstructionType(DjangoObjectType):  
    class Meta:
        model = Instructions

class IngredientsTextType(DjangoObjectType):  
    class Meta:
        model = IngredientsText

class ImageType(DjangoObjectType):  
    class Meta:
        model = Images

class Query(object):  
    recipe = graphene.Field(RecipeType, id=graphene.Int())
    category = graphene.Field(CategoryType, id=graphene.Int())
    ingredient = graphene.Field(IngredientType, id=graphene.Int())
    tag = graphene.Field(TagType, id=graphene.Int())
    instruction = graphene.Field(InstructionType, id=graphene.Int())
    ingredientsText = graphene.Field(IngredientsTextType, id=graphene.Int())
    image = graphene.Field(ImageType, id=graphene.Int())
    recipes = graphene.List(RecipeType)
    categories= graphene.List(CategoryType)
    ingredients = graphene.List(IngredientType)
    tags = graphene.List(TagType)
    instructions = graphene.List(InstructionType)
    ingredientsTexts = graphene.List(IngredientsTextType)
    images = graphene.List(ImageType)

    def resolve_recipe(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Recipes.objects.get(pk=id)

        return None

    def resolve_recipes(self, info, **kwargs):
        return Recipes.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Categories.objects.all()

    def resolve_tags(self, info, **kwargs):
        return Tags.objects.all()

    def resolve_ingredients(self, info, **kwargs):
        return Ingredients.objects.all()

    def resolve_instructions(self, info, **kwargs):
        return Instructions.objects.all()
    
    def resolve_ingredientsText(self, info, **kwargs):
        return IngredientsText.objects.all()

    def resolve_images(self, info, **kwargs):
        return Images.objects.all()

# class RecipesInput(graphene.InputObjectType):  
#     id = graphene.ID()
#     name = graphene.String()
#     title = graphene.String()
#     tagLine = graphene.String()
#     category = graphene.Field(Categories, on_delete=models.PROTECT)
#     heat = models.PositiveSmallIntegerField()
#     output = models.PositiveSmallIntegerField()
#     difficulty = models.PositiveSmallIntegerField()
#     prepTime = models.PositiveSmallIntegerField()
#     html = models.TextField()

# class CategoriesInput(graphene.InputObjectType):  
#     id = graphene.ID()
#     title = graphene.String()
#     actors = graphene.List(ActorInput)
#     year = graphene.Int()