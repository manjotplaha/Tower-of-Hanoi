from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack= Stack("Left")
middle_stack= Stack("Middle")
right_stack= Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Gamepython3 script.py
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

# Now, we will add our disks. We will represent disks with numbers. Disk 3 is larger than Disk 1 etc.
for i in range(num_disks,0,-1):
  left_stack.push(i)

num_optimal_moves = 2**num_disks -1
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

# Get User Input #
# Now, let’s create a helper function that prompts users to choose a stack. We want to have users only enter the first letter. For instance:
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter{} for {}".format(letter,name))
    user_input = input("")

    # check if the user made a valid choice.
    if user_input in choices:
      for i in range(len(stacks)):
        return stacks[i]

#Play the Game
num_user_moves = 0

while right_stack.get_size != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    print(stack.print_items())

  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.get_size() == 0:
      print("\n\nInvalid Move. Try Again")
    elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))