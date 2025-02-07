name = input("Enter your name: ")
print("Hello " + name +  " Welcome to my game!")

should_we_play = input("Do you want to play a game? (yes/no): ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("Great! Let's get started!")

    direction = input("Do you want to go left or right? (left/right): ").lower()
    if direction == 'left' or direction == 'l':
        print("you went left and fell of a cliff, game over, try again!")

    elif direction == "right" or direction == 'r':
        choice = input("You have come to a lake, do you want to swim or go around? (swim/around): ").lower()
        if choice == "around" or choice == "a":
            print("you went around and reached the other side of the lake, you won!")
        elif choice == "swim" or choice == "s":
            print("you swam across the lake and were eaten by a shark, you lost!")

        else:
            print("invaild input, you lo")

else:
    print("we are not playing a game today!")