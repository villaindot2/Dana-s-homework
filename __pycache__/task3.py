class Country:

	def __init__(self, name, pop, area):
		self.name = name
		self.population = pop
		self.area = area
		if self.population > 250000000 or self.area > 3000000:
			self.is_big = True
		else:
			self.is_big = False
		self.dens = pop/area
		
	def compare_pd(self, other):
		compare = "{} has a {} population density than {}"
		print(compare.format(self.name,("smaller" if self.dens<other.dens else "larger"), other.name))

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(andorra.is_big)
print(australia.is_big)
print(andorra.compare_pd(australia))