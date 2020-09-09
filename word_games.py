file = open("words.txt", "r")
word_list = []
for line in file:
    word_list += line.lower().split()

word = ""
player = 0
while word.lower() not in word_list:
    player = player % 2 + 1
    print("Enter next letter: ")
    letter = input()
    word += letter
    print("The current fragment is: " + word)
if player == 1:
    print("player 2 won")
else:
    print("player 1 won")
