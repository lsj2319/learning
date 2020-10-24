# create a class called Dog to start. each dog obj will have unique name and age values
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method (I know it's obvious, I'm practicing)
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    #another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

molly = Dog("Molly", 9)
print("")
print(molly)

talk = molly.speak("mOhhh Rowr mOhmm mm")

hi_dog = molly.speak("Ruof Wuroof")

print(talk)
print("")
print(hi_dog)