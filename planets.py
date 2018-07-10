#   DONE    Use append() to add Jupiter and Saturn at the end of the list.
#   DONE    Use the extend() method to add another list of the last two planets
#                in our solar system to the end of the list.
#   DONE    Use insert() to add Earth, and Venus in the correct order.
#   DONE    Use append() again to add Pluto to the end of the list.
#   DONE    Now that all the planets are in the list, slice the list in order
#                to get the rocky planets into a new list called rocky_planets.
#   DONE    Being good amateur astronomers, we know that Pluto is now a dwarf planet,
#                so use the del operation to remove it from the end of planet_list.
#           Iterating over planets
#   DONE       Create another list containing tuples. Each tuple will hold the name
#               of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
#           Iterate over your list of planets, and inside that loop, iterate over
#               the list of tuples. Print, for each planet, which sattelites have visited.

planet_list = ["Mercury", "Mars"]
launches = [('Minecraft', 'Saturn'), ('Aircraft', 'Earth'), ('Watercraft', 'Mars'), ('Aircraft', 'Saturn'), ('Watercraft', 'Venus'), ('Aircraft','Venus')]

planet_list.append('Jupister')
planet_list.append('Saturn')

more_planets = ["Earth", "Uranus"]
planet_list.extend(more_planets)
planet_list.insert(3, 'Venus')
planet_list.append('Pluto')
rocky_planets = planet_list[0:4]
del(planet_list[7])

planet_launches = {}

for launch in launches:
     if launch[0] in planet_launches:
         planet_launches[launch[0]]+= (launch[1],)
     else:
         planet_launches[launch[0]] = (launch[1],)


for planet, launch in planet_launches.items():
    print(f'{planet}, {launch}')
# def get_spacecraft():

#     for planet in planet_list:
#         for launch in launches:
#             if (planet == launch[1]):
#                 print(f'{planet}, {launch[0]}')


# get_spacecraft()

# def get_launches():
#     planet_launches = {}
#     planets = list()
#     for launch in launches:
#         planet_launches[launch] = launch

# print(planet_list)
# print(rocky_planets)
# print(launches)



