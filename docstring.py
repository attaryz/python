def population_density(population, land_area):
    """Calculate the population density of an area.
    INPUT: 
    population: int. The population of the area.
    land_area: int or float. This function is unit-agnostic,
    if you pass in values in terms of squares km or square miles the function will return 
    a density in those units.
    OUTPUT:
    population_density: population/land_area. The population density of a particular area.
    """
    return population / land_area 