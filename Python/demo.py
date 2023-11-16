

# Variables

## Simple Variables

### Integers

i = 1
n = 5

x = i * n

# print(x)

### Strings

greeting1 = "Hello"
greeting2 = "world!"

greeting = greeting1 + greeting2
# print(greeting1+greeting2)

# for i in range(1,100):
#     print(i)
### Boolean

water_is_wet = True
sky_is_purple = False


## Complex Variables

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# for item in planets:
#     print(item, "is a planet")

ships = {'1701': 'Kirk',
        '74656': 'Janeway', 
        '1701-D': 'Picard', 
        '1864': 'Khan'}

for item in ships:
    print("The captain of NCC-"+item, "is", ships[item])