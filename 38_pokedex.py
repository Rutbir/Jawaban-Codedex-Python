# Membuat program pokedex sederhana dengan metode class

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.desc = description
    self.ic = is_caught

  def speak(self):
    print(f'{self.name} {self.name}')

  def display_details(self):
    print('Entry Number: ' + str(self.entry))

    print('Name: ' + self.name)

    if len(self.types) == 1:
      print('Type: ' + self.types[0])
    else:
      print('Type: ' + self.types[0] + '/' + self.types[1])

    print('Description: ' + self.desc)

    if self.ic:
      print(self.name + ' has already been caught!')
    else:
      print(self.name + " hasn't been caught yet.")

ambamon = Pokemon(1, 'ambamon', 'dark', 'waspadalah terhadap pokemon ini', True)
rusdimon = Pokemon(2, 'rusdimon', ['dark', 'fighting'], 'waspadalah terhadap pokemon ini', False)
imutmon = Pokemon(3, 'imutmon', ['dark', 'psychic'], 'waspadalah terhadap pokemon ini', True)

ambamon.speak()
ambamon.display_details()

rusdimon.speak()
rusdimon.display_details()

imutmon.speak()
imutmon.display_details()