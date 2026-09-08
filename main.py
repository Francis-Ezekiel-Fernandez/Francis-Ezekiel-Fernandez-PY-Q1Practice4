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
display(type(awards), target = "output1")
display(type(b))
display(b)

#join() - method that combines the list back into a string

