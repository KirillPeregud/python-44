# task №5_3 by Kirill Peregud
import random

print('The program calculates the distance between points in N-dimensional space.')

def validation_dim(arg):
    print('----------')
    num = 0
    while num not in range(1, 11):
        try:
            num = int(input(f'\nEnter the size of the space for the {arg}:\n'))
        except:
            print('\nUnfortunately, the argument is not an integer :(\n')
        else:
            if num in range(1, 11):
                break
            else:
                print('\nPlease, enter a positive integer number from 1 to 10.')
    print('----------\n')    
    return num

def get_coordinates(n):
    coord = tuple([random.randint(0, 100) for _ in range(n)])
    return coord


class Point:
    
    def __init__(self, coords):
        self.coords = coords

    def __iter__(self):
        self.val = 0
        return self

    def __next__(self):
        if self.val < len(self.coords):
            x = self.val
            self.val += 1
            return self.coords[x]
        else:
            raise StopIteration

    def __abs__(self):
        return sum([x ** 2 for x in self.coords]) ** 0.5

    def __repr__(self):
        text1 = f'Point coordinates -> {self.coords}\n'
        text2 = 'Distance from point to origin -> %.2f\n' % abs(self)
        return text1 + text2


class StraightLine:

    def __init__(self, first_point, second_point):
        self.point_a = Point(first_point)
        self.point_b = Point(second_point)

    def __abs__(self):
        return sum(
            [
                (x - y) ** 2
                for x, y in zip(
                    self.point_a, self.point_b
                )
            ]
        ) ** 0.5

    def __repr__(self):
        text1 = f'Straight coordinates -> {self.point_a.coords}, {self.point_b.coords}\n'
        text2 = 'Distance between points -> %.2f\n' % abs(self)
        return text1 + text2

    def go_to_origin(self):
        self.new_point_a = []
        self.new_point_b = []
        for x, y in zip(self.point_a, self.point_b):
            delta = x
            self.new_point_a.append(x - delta)
            self.new_point_b.append(y - delta)
        self.point_a.coords = tuple(self.new_point_a)
        self.point_b.coords = tuple(self.new_point_b)

        print(f'Straight new coordinates -> {self.point_a.coords}, {self.point_b.coords}')
        print('Distance between new points -> %.2f\n' % abs(self))


# Start of the program
n_point = validation_dim('point')

point_1 = Point(get_coordinates(n_point))
print(point_1)

point_2 = Point(get_coordinates(n_point))
print(point_2)


n_line = validation_dim('line')

straight_1 = StraightLine(get_coordinates(n_line), get_coordinates(n_line))
print(straight_1)

straight_2 = StraightLine(get_coordinates(n_line), get_coordinates(n_line))
print(straight_2)
print('----------\n')


straight_1.go_to_origin()
straight_2.go_to_origin()
print('----------\n')
