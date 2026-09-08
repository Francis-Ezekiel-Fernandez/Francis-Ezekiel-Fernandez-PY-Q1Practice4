from pyscript import document, display

a = "Age: "
b = "45"
z = "- "
display(f"{a} + {b}")
display(f"{a}{b}")
display(f"{a},{b}")
display(a + b)
display(z*178)
#offset indexing
#checking of index
d = "Seipsum Facit Persona"
#    123456789
display(d[-4])

#checking of index
#length = lrn() - function that counts the number of characters and returns the result as an integer

e ="Seipsum Facit Persona"
f = (10,20,30,45,75) #tuple
g = ["apple", "banana", "mango", "avocado"]
h = {"Color": "purple", "Subject": "ict"}

#   0123456789
display(len(e))
display(len(f))
display(len(g))
display(len(h))

#split() - method that turns string into a list

# "" --> []

awards = 'Gold, Silver, Bronze'
display(awards.split(","))
display(type(b))
display(b)

#join() - method that combines the list back into a string

months = ["January", "February", "April"]#list
sample_string = "My favorite months are: "

display(sample_string + ",".join(months))

#replace() - method that replaces all occurences of old with new inside a string

food = "My favorite food/s is/are: Yabu Mozzarella Sticks, Jollibee Cheesy Yumburger, Steak"
display(food.replace('Steak', 'Ribs'))

#CASE - chance case of characters
#title() - capitalizes the letter of EACH WORD
#capitalize - capitalizes the first word
#upper() - capitalizes all
#lower() - lower cases all
#swapcase () - changes upper to lower and vice versa
name ="zeek"
display(name.capitalize())

Name = "i am zeek"
display(Name.capitalize())

naame = "whats goody my gang get your money up not your funny up"
display(naame.title())

Naame = "No, no, no, don't do that! I thought we were having a nice day!"
display(Naame.upper())

Naame = "No, no, no, don't do that! I thought we were having a nice day!"
display(Naame.lower())

naaame = "Uh CmOn"
display(naaame.swapcase())


