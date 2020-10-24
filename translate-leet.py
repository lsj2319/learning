# translate-leet.py
# will take user text and convert it to leetspeak [a=4, b=8, e=3, l = 1 0=0]

# take user input
yourtext = input("Enter some text: ")
# print("")
print(f"You entered: {yourtext}")
# use .replace() to convert text into leetspeak (lowercase letters)
## We don't know what someone will enter.
# looping is more efficient. Will refactor later.
## step one  - replace one letter, one time
new_text = yourtext.replace("a", "4")
new_text = new_text.replace("b", "8")
new_text = new_text.replace("e", "3")
new_text = new_text.replace("l", "1")
new_text = new_text.replace("o", "0")
new_text = new_text.replace("s", "5")
new_text = new_text.replace("t", "7")
# display resulting string as output.
print(f"You are so leet! {new_text}")

# but first some practice with find
#text = "some of the stuff"
# new_text = text.replace("some of", "all")
# new_text = new_text.replace("stuff", "things")
# new_text  / 'all the things'

