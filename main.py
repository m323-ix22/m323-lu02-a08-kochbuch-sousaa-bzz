"""
functions to load and adjust recipes.
"""

import json



def load_recipe(json_string):
    return json.loads(json_string)


def adjust_recipe(recipes, new_servings):
    title = recipes['title']
    ingredients = recipes['ingredients']
    servings = recipes['servings']

    factor = new_servings / servings

    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in ingredients.items()}

    return {
        'title': title,
        'ingredients': adjusted_ingredients,
        'servings': new_servings
    }


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300'
                   ', "Minced Meat": 500}, "servings": 4}')

    recipe = load_recipe(recipe_json)

    new_serving = 2

    adjusted_recipe = adjust_recipe(recipe, new_serving)

    print('Angepasstes Rezept:')
    print(json.dumps(adjusted_recipe, indent=4))
