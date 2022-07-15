from django.forms import ChoiceField, ModelForm, inlineformset_factory 
from .models import Diet, Cuisine, Difficulty, CookTime, Ingredient, PrepMethod, QuantityUnit, Recipe, RecipeIngredient 


class CreateNewRecipe(ModelForm):
    difficulty = ChoiceField(choices=Difficulty.DIFFICULTIES)
    cook_time = ChoiceField(choices=CookTime.COOK_TIMES)
    
    class Meta:
        model = Recipe
        fields = '__all__'

IngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    exclude=('recipe',),
    extra=1
)




#class CreateRecipeIngredient(forms.Form):
    #ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all())
    #custom_ingredient = forms.CharField('custom ingredient', max_length=100)
    #quantity_unit = forms.ModelChoiceField(queryset=QuantityUnit.objects.all())
    #custom_unit = forms.CharField('custom unit', max_length=50)
    #prep_method = forms.ModelChoiceField(queryset=PrepMethod.objects.all())
    #custom_prep = forms.CharField('custom prep', max_length=100)
    #amount = forms.FloatField()