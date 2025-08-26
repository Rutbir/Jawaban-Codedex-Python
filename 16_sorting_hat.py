# membuat program sorting hat seperti di film Harry Potter

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1) Do you like Dawn or Dusk? 1) Dawn 2) Dusk")
answer = int(input('Enter your answer (1-2): '))
if answer == 1:
  Gryffindor = Gryffindor + 1  
  Ravenclaw = Ravenclaw + 1
elif answer == 2:
  Hufflepuff = Hufflepuff + 1 
  Slytherin = Slytherin + 1
else:
  print("Wrong input")

print("Q2) When I’m dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold")
answer = int(input('Enter your answer (1-4): '))
if answer == 1:
  Hufflepuff = Hufflepuff + 2
elif answer == 2:
   Slytherin = Slytherin + 2
elif answer == 3:
  Ravenclaw = Ravenclaw + 2
elif answer == 4:
   Gryffindor = Gryffindor + 2
else:
  print("Wrong input")

print("Q3) Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum")
answer = int(input('Enter your answer (1-4): '))
if answer == 2:
  Hufflepuff = Hufflepuff + 4
elif answer == 1:
   Slytherin = Slytherin + 4
elif answer == 3:
  Ravenclaw = Ravenclaw + 4
elif answer == 4:
   Gryffindor = Gryffindor + 4
else:
  print("Wrong input")

print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin) 