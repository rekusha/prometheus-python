import math


class Sphere(object):

    def __init__(self, radius = 1, x = 0, y = 0, z = 0):
		self.radius = radius
                self.x = x
                self.y = y
                self.z = z

    def get_volume(self):
        return (4.0 / 3.0) * (math.pi * (self.radius**3))

    def get_square(self):
        return 4.0 * (math.pi * (self.radius * self.radius))

    def get_radius(self):
        return self.radius

    def get_center(self):
        return float(self.x), float(self.y), float(self.z)

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x1, y1, z1):
            self.x = x1
            self.y = y1
            self.z = z1

    def is_point_inside(self, x, y, z):
         if math.sqrt((self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2) <= self.radius**2:
             return True
         else:
             return False