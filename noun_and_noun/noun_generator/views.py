#from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import random
from django.shortcuts import render
import os

and_symbol_list = [' & ', ' + ']


def index(request):
    noun_list = []
    with open(os.path.join(settings.PROJECT_ROOT, 'nouns.txt'), 'r') as f:
        noun_list = f.read().splitlines() 

    template = 'noun_generator/index.html'
    noun_one = random.choice(noun_list)
    same_noun = True
    while same_noun is True:  # could also copy the noun list, pop a value, and get a second value from copied list
        noun_two = random.choice(noun_list)
        if noun_one != noun_two:
            same_noun = False
    and_symbol = random.choice(and_symbol_list)
    context = {'noun_text': noun_one + ' ' + and_symbol + ' ' + noun_two}

    # download background image
    #download_url = 'https://farm%s.staticflickr.com/%s/%s_%s.jpg' % farm_id, server_id, idnum, secret_id

    return render(request, template, context)
