from django.shortcuts import render


def index(request):
    context = {'cart': {'total': 25.0,
                        'count': 2},
               'categories': [{'title': 'Drinks',
                               'subcategories': [
                                   {'title': 'Fizzy Drinks'},
                                   {'title': 'Hot Drinks'}
                               ]},
                              {'title': 'Not drinks',
                               'subcategories': [
                                   {'title': 'Sweets'}
                               ]}
                              ]
               }
    return render(request, "shop/index.html", context)

def search(request):
    context = {'cart': {'total': 25.0,
                        'count': 2}}
    return render(request, "shop/index.html", context)