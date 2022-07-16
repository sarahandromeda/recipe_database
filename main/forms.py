from django.forms import BaseInlineFormSet, ChoiceField, ModelForm, inlineformset_factory 
from .models import Diet, Cuisine, Difficulty, CookTime, Ingredient, PrepMethod, QuantityUnit, Recipe, RecipeIngredient 

class CustomInlineIngredientFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            ingredient = form.cleaned_data['ingredient']
            quantity_unit = form.cleaned_data['quantity_unit']
            prep_method = form.cleaned_data['prep_method']
            if ingredient not in Ingredient.objects.all():
                new_ingredient = Ingredient(ingredient_name=ingredient)
                new_ingredient.save()
                form.cleaned_data['ingredient'] = new_ingredient.id
                form.instance.ingredient = new_ingredient.id
        super().clean()


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
    extra=1,
    formset=CustomInlineIngredientFormset
)
