#!/usr/bin/python

import math

# Your function should output the maximum number of whole batches   that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary.

# We need to take two arrays compare values at the same index, and take the lowest whole number from the two arrays and output that as the result

# First we need to take the recipe dictionary and grab the values and put them in their own array

# Then we need to take the ingredients dictionary and grab the values and put them in their own array

# Then we take the two arrays, put them in a for loop, and maybe we can use a list comprehension, but we can take the two values and divide the recipe by the ingredients with a floor (//) and then take that result and get the minimum from the array, and thats the number of batches that you have. allegedly.

def recipe_batches(recipe, ingredients):
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
