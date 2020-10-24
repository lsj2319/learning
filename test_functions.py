# test_functions.py
# testing functions / added a docstring for greet

#def greet(name):
#    """Return string Hello and a person name assigned to variable name"""
#    print(f"Hello, {name}!")

#greet("Dave")
#### a set of temperature conversion functions ####
def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return float(F)
your_cel = int(input("Enter a temparature in degrees C: "))
new_far = convert_cel_to_far(your_cel)
print(f"{your_cel} degrees C = {new_far:.2f} degrees F")

def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    return float(C)

your_far = int(input("Enter a temparature in degrees F: "))
new_cel = convert_far_to_cel(your_far)
print(f"{your_far} degrees C = {new_cel:.2f} degrees F")


