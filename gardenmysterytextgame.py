# gardenmysterytextgame.py

# a text adventure to practice python

def player_health():
    health = 10
    return health

def health_score(ac):
    current_health = 10 - ac
    return current_health

# fuctions
def player_choices():
    health = 10
    print("You wake up in the clearing of a mysterious forest. There is a dirt path to your left /"
          "and trees with a grassy path to your right. ")
    left_or_right = input("First choice...Left or Right? (left/right)? ").lower()
    if left_or_right == "left":
        answer = input("You follow the path and reach a field of flowers. Do you cross the field or go around? (across/around)? ").lower()
        if answer == "around":
            print("You walk the long way around the field. There is a river in front of you.")
        elif answer == "across":
            lost_health = 3
            print(f"You cross the field and start to feel very sleepy. You lose {lost_health} health.")
            health_score(lost_health)
            print(f"Your current health is {health_score(lost_health)}")


    else:
        print("You are in a dark forest.")

# player input
print("Welcome to Garden Mystery, a text adventure game!")

player_name = input("What is your name? ")
player_age = int(input("What is your age? "))

print(f"Hello {player_name} you are {player_age} years old.")

# is user old enough to play?
check_age = int(player_age) >= 5
if player_age >=5:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let the adventure begin!")
        print(f"You are starting with {player_health()} health.")
        player_choices()

    else:
        print("Some other time...")
else:
    print("You are too young!")

