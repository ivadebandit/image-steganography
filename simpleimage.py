import os
from PIL import Image

class SimpleImage:
    def __init__(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Could not find file: {filename}")
        self.image = Image.open(filename).convert('RGB')
        self.width, self.height = self.image.size
        self.pixels = self.image.load()

    @classmethod
    def blank(cls, width, height):
        self = cls.__new__(cls)
        self.image = Image.new('RGB', (width, height), 'white')
        self.width = width
        self.height = height
        self.pixels = self.image.load()
        return self

    def get_pixel(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return Pixel(self, x, y)
        raise IndexError(f"Pixel coordinate out of bounds: ({x}, {y})")

    def show(self):
        self.image.show()

    def save(self, filename):
        self.image.save(filename)

    def __iter__(self):
        for y in range(self.height):
            for x in range(self.width):
                yield Pixel(self, x, y)

class Pixel:
    def __init__(self, simple_image, x, y):
        self.simple_image = simple_image
        self.x = x
        self.y = y

    @property
    def red(self):
        return self.simple_image.pixels[self.x, self.y][0]

    @red.setter
    def red(self, value):
        g = self.simple_image.pixels[self.x, self.y][1]
        b = self.simple_image.pixels[self.x, self.y][2]
        self.simple_image.pixels[self.x, self.y] = (int(value), g, b)

    @property
    def green(self):
        return self.simple_image.pixels[self.x, self.y][1]

    @green.setter
    def green(self, value):
        r = self.simple_image.pixels[self.x, self.y][0]
        b = self.simple_image.pixels[self.x, self.y][2]
        self.simple_image.pixels[self.x, self.y] = (r, int(value), b)

    @property
    def blue(self):
        return self.simple_image.pixels[self.x, self.y][2]

    @blue.setter
    def blue(self, value):
        r = self.simple_image.pixels[self.x, self.y][0]
        g = self.simple_image.pixels[self.x, self.y][1]
        self.simple_image.pixels[self.x, self.y] = (r, g, int(value))