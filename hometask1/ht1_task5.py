import random

words = ["Heads", "Tails"]
pc_input = random.choice(words)
custom_input = input('Enter Heads or Tails: ')
if custom_input.capitalize() == words[0] or custom_input.capitalize() == words[1]:
    if pc_input == custom_input.capitalize():
        print("Congratulation! You win! PC chose", pc_input, "as well")
    else:
        print("Sorry. You lost. PC chose: ", pc_input)
else:
    print("No valid enter")





