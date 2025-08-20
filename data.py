from django.template.defaultfilters import length
from numpy.lib.function_base import iterable

str_ ="selenium"

class Sample:

    def finding_length(self,iterable):
        length=0
        for i in iterable():
            length +=1
        print(length)