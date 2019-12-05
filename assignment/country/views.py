from django.http import JsonResponse
from .models import Country
from django.db.models import Q


# Search query
def get_searched(request,key_word):
    query = Country.objects.\
        filter(
                Q(name__contains=key_word) | Q(code__contains=key_word) |
                Q(city__name__contains=key_word) | Q(languages__language__contains=key_word)).\
        select_related('city','languages').\
        values('code','name','city__name','languages__language').all()

    output = []
    # ordering data
    for item in query:
        for val in item.values():
            try:
                if key_word.lower() in val.lower():
                    output.append(item)
                    break
            except AttributeError:
                pass
    return JsonResponse(output,safe=False)
    # return JsonResponse(list(query),safe=False)


# Getting details of a country
def details(request, code):
    fields = ['code','name','continent','region','surface_area','indep_year','population',
            'life_expectancy','gnp','gnp_old','local_name','government_form','head_of_state',
            'capital','code2']
    additional_fields = ['city__name','city__district','city__population',
            'languages__language','languages__is_official','languages__percentage']
    
    query = Country.objects.filter(code=code).\
        select_related('city','languages').\
        values(*fields,*additional_fields).all()
    
    
    output = dict(query[0])

    # Deleting the unwanted keys in main object
    for item in additional_fields:
        if item in output.keys():
            del output[item]
    
    output['city'] = dict()
    output['languages'] = dict()
    # Organizing/Struturing the output
    for q in query:
        output['city'].update({q['city__name']:{
                                'district': q['city__district'],
                                'population': q['city__population']
                                }
                            })
        output['languages'].update({q['languages__language']: {
                                'is_official': q['languages__is_official'],
                                'percentage': q['languages__percentage']
                                }
                            })
    return JsonResponse(output,safe=False)
