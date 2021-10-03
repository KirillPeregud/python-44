# task №5_3 by Kirill Peregud
import random
import math

print('The program calculates the distance between points in N-dimensional space.')

def validation_dim():
    num = 0
    while num not in range(1, 11):
        try:
            num = int(input('\nEnter measure of dimensional:\n'))
        except:
            print('\nUnfortunately, the argument is not an integer :(\n')
        else:
            if num in range(1, 11):
                break
            else:
                print('\nPlease, enter a positive integer number from 1 to 10.')
    return num

def get_coordinates(n):
    coord = [random.randint(0, 100) for _ in range(n)]
    return tuple(coord)

class Point:
    
    def __init__(self, n, coord_a):
        self.n = n
        self.coord_a = coord_a


    def distance(self):
        sum = 0
        for x in self.coord_a:
            sum += x ** 2
        return math.sqrt(sum)


class StraightLine(Point):
    def __init__(self, n, coord_a, coord_b):
        super().__init__(n, coord_a)
        self.coord_b = coord_b


    def distance(self):
        sum = 0
        for x, y in zip(self.coord_a, self.coord_b):
            sum += (x - y) ** 2
        return math.sqrt(sum)


    def go_to_origin(self):
        self.new_coord_a = []
        self.new_coord_b = []
        for x, y in zip(self.coord_a, self.coord_b):
            delta = x
            self.new_coord_a.append(x - delta)
            self.new_coord_b.append(y - delta)
        self.coord_a = tuple(self.new_coord_a)
        self.coord_b = tuple(self.new_coord_b)


n = validation_dim()

point_1 = Point(n, get_coordinates(n))
point_2 = Point(n, get_coordinates(n))

print('----------\n')
print(f'Point coordinates -> {point_1.coord_a}')
print('Distance from point to origin -> %.2f\n' % point_1.distance())

print(f'Point coordinates -> {point_2.coord_a}')
print('Distance from point to origin -> %.2f\n' % point_2.distance())
print('----------\n')


straight_1 = StraightLine(n, get_coordinates(n), get_coordinates(n))
straight_2 = StraightLine(n, get_coordinates(n), get_coordinates(n))

print(f'Straight coordinates -> {straight_1.coord_a}, {straight_1.coord_b}')
print('Distance between points -> %.2f\n' % straight_1.distance())

print(f'Straight coordinates -> {straight_2.coord_a}, {straight_2.coord_b}')
print('Distance between points -> %.2f\n' % straight_2.distance())
print('----------\n')


straight_1.go_to_origin()
straight_2.go_to_origin()

print(f'Straight new coordinates -> {straight_1.coord_a}, {straight_1.coord_b}')
print('Distance between new points -> %.2f\n' % straight_1.distance())

print(f'Straight new coordinates -> {straight_2.coord_a}, {straight_2.coord_b}')
print('Distance between new points -> %.2f\n' % straight_2.distance())
print('----------')
