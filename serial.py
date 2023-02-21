"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        self.start = start
        self.next = start

    def __refr__(self):
        return f'SerialGenerator start={self.start} next={self.next}'

    def generate(self):
        "increments and returns serial number"
        
        self.next += 1
        return self.next - 1

    def reset(self):
        "resets to starting serial number"
        self.next = self.start

