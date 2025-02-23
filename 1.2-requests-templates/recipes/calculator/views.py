from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'graten': {
        'Картофель, г': 150,
        'Сливки, мл': 25,
        'Сыр твёрдый, г': 25,
        'Масло сливочное, г': 4,
    }
}

def recipe(request, dish):
    recipe_data = DATA.get(dish, {})
    servings = request.GET.get('servings')
    if servings and servings.isdigit() and int(servings) > 0:
        servings = int(servings)
        recipe_data = {ingredient: amount * servings for ingredient, amount in recipe_data.items()}
    context = {
    'recipe': recipe_data
    }
    return render(request, 'calculator/index.html', context)