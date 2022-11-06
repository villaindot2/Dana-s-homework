class Country:

	def __init__(self, name, popu, area):
		self.name = name
		self.population = popu
		self.area = area
		if self.population > 250000000 or self.area > 3000000:
			self.is_big = True
		else:
			self.is_big = False
		self.dens = popu/area
		
	def compare_pd(self, other):
		compare = "{} has  {} popul than {}"
		print(compare.format(self.name,("small" if self.dens<other.dens else "large"), other.name))

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(andorra.is_big)
print(australia.is_big)
print(andorra.compare_pd(australia))