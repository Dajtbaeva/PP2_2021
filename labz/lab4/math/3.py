from math import tan, pi, ceil
sides = int(input('Number of sides: '))
length = int(input('The length of a side: '))
print('The area of the polygaon is:', (ceil(pow(length, 2) * sides / 4 * (tan(pi/sides)))))