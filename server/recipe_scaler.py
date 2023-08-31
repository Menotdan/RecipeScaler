from fractions import Fraction
from math import log10, ceil

filename = "ingredient_list.txt"

def gather_scale_and_ingredients(ingredient_list_file: str):
    fp = open(ingredient_list_file, "r")
    lines = fp.read().splitlines()

    scale = float(lines[0].replace("x", "")) # {scale}x, eg. 0.5x
    lines = lines[1:] # Discard first line after parsing for `scale`
    ingredients = [l for l in lines if not l == '']

    return (ingredients, scale)

def try_parse_fraction_or_number(potential_value: str):
    if "/" in potential_value:
        try:
            output = Fraction(potential_value)
        except (ValueError, ZeroDivisionError):
            return None
        else:
            return output.real

    if potential_value.isnumeric():
        return float(potential_value)

    return None

def scale_ingredient(ingredient: str, scale: float):
    # Check if the ingredient is numbered, and return it if it's not
    potential_number = ingredient.split(" ")[0]
    parsed_number = try_parse_fraction_or_number(potential_number)
    if parsed_number == None:
        return ingredient

    # We know it's a number, convert to a fractional value before returning the new list
    number = Fraction(parsed_number * scale)
    ingredient = ingredient.replace(potential_number, str(number), 1)
    return ingredient

def scale_ingredients(ingredient_list: list, scale: float):
    scaled_ingredients = [scale_ingredient(ingredient, scale) for ingredient in ingredient_list]
    return scaled_ingredients

def display_ingredients(ingredients: list):
    max_width = ceil(log10(len(ingredients))) + 1

    for idx, scaled_ingredient in enumerate(ingredients):
        number_format = f"{idx + 1}."
        print(f"{number_format:{max_width+1}} {scaled_ingredient}")

# Main
ingredient_list, scale = gather_scale_and_ingredients(filename)
scaled_recipe = scale_ingredients(ingredient_list, scale)
display_ingredients(scaled_recipe)