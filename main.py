
print('Welcome to the jungle')
print('You find yourself lost in a jungle and cannot find your way out. As you walk further into the jungle you see')
print('three animals: a monkey, a sloth, and a toucan who each are holding a letter that reads “Choose correctly or')
print('you’ll be lost in the jungle forever!')
print()
number = int(input('What is your favorite number 0-50?'))
energy = number * 2
print()
if number < 10:
    print('Follow the monkey')
    print(f'you have {energy} % energy')
elif (number >= 10) and (number <= 20):
    print("Follow the sloth")
    print(f'you have {energy} % energy')
elif number > 20:
    print("Follow the toucan")
    print(f'you have {energy} % energy')
else:
    print('Invalid input, please enter a number between 0 and 50')
    print()
print('Your energy has decreased by a certain amount, and you will need to receive more to get out of the jungle.')
energy_needed = int(input('How much energy do you need to get to 100%?'))
print()
if energy_needed >= 25:
    print('Eat the banana')
elif energy_needed >= 30 or energy_needed >= 50:
    print('Eat the mango')
elif energy_needed > 50:
    print('Eat the papaya')
print()
print('A tree has fallen preventing you from going the right direction. Your animal leaves and the decision up to you.')
print('The decision contains climbing over the tree or under the tree, each decision leading to a different way')
print()
tree = (input('would you like to climb above the tree or below the tree?: '))
if tree == "above":
    print('You have found your way out of the jungle')
elif tree == "below":
    print('You must continue on your journey :(')



