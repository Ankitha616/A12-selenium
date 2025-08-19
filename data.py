from django.template.defaultfilters import length
from numpy.lib.function_base import iterable

str_ ="selenium"

def finding_length(iterable):
    length=0
    for i in iterable():
        length +=1
    print(length)

finding_length(str_)
finding_length([1,2,3,4,5,6,7,8])
finding_length("akshitha")