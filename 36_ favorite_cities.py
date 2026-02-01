class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

rutbir = City('Rutbir', 'Indonesia', 2000000, 'gk ada')
print(vars(rutbir))