#***************по строчно считывем из файла с помощью генератора****************

# def my_generator():
#      with open("text", 'r') as file:
#           for i in file.readlines():
#                yield i
# for i in my_generator():
#      print(i)

#*******из кемл кейса в стиль пайтон***********

def from_camel_case(camel_string):
    new_string = camel_string[0].lower()
    for letter in camel_string[1:]:
        if letter.isupper():
            new_string += f'_{letter.lower()}'
        else:
            new_string += letter
    return new_string
print(from_camel_case("theCamelString"))

#***************полиндром********

def polindrom(polindrom_string):
     new_string = ''.join(reversed(polindrom_string))
     if new_string == polindrom_string:
          return True
     else:
          return False
print(polindrom('pol'))



