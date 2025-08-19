from django.template.defaultfilters import length
from numpy.lib.function_base import iterable

str_ ="selenium"

def finding_length(iterable):
    length=0
    for i in iterable():
        length +=1
    print(length)

finding_length(str_)



