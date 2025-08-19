from django.template.defaultfilters import length

str_ ="selenium"

length=0
for i in str_:
    length +=1
print(length)