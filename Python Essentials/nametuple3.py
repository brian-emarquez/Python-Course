from collections import namedtuple

Color = namedtuple('color', ['red', 'green', 'blue'])

dict_color = {'red': 55, 'green': 155, 'blue': 255}

color = Color(55, 155, 255)
white = Color(255, 255, 255)

print(white.blue)