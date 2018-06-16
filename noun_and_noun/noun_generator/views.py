#from django.shortcuts import render
from django.http import HttpResponse
import random

noun_list = ['Flower', 'Water', 'Basil', 'Hazelnut', 'Thistle', 'Thread', 'Herb', 'Wood']
and_symbol_list = [' & ', ' + ']


def index(request):
    noun_one = random.choice(noun_list)
    same_noun = True
    while same_noun is True:  # could also copy the noun list, pop a value, and get a second value from copied list
        noun_two = random.choice(noun_list)
        if noun_one != noun_two:
            same_noun = False
    and_symbol = random.choice(and_symbol_list)
    return HttpResponse(noun_one + and_symbol + noun_two)
