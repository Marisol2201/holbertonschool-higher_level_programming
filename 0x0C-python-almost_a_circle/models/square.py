#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns formatted information display"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width)

    @property
    def size(self):
        """Getter and setter methods for the instance attribute __size
        Validation of the input is done by the Rectangle superclass update"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates square values"""
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            valid_args = args[:4]
            args_list = ['id', 'size', 'x', 'y']
            for index in range(len(valid_args)):
                setattr(self, args_list[index], valid_args[index])

    def to_dictionary(self):
        """Returns a dict representation"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
