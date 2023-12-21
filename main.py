from composition import Composition
from produit import Produit
from elementaire import Elementaire
from compose import Compose

# Creating instances of Elementaire and Composition
p1 = Elementaire("i5", "4a5s44a", 65)
p2 = Elementaire("ram", "dfy4fdt33", 35)
co1 = Composition(p1, 20)
co2 = Composition(p2, 100)

# Creating an instance of Compose
c1 = Compose("HP", "4f3tfy", 56, 18, [co1, co2])

# Displaying information using __str__ method and other operations
print(p1)     # String representation of p1
print(p2)     # String representation of p2
print(co1)    # String representation of co1
print(co2)    # String representation of co2
print(co1 == co2)       # Equality comparison between co1 and co2
print(c1)     # String representation of c1

# Displaying the total price excluding tax for the composed product
print("Price excluding tax : ", c1.GetprixHT, "DH")
