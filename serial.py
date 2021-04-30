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
    def __init__(self,start):
      self.start = start
      self.curr_num = ''
    
    def generate(self):
      if isinstance(self.curr_num, int):
        self.curr_num += 1 
      else:
        self.curr_num = self.start
      return self.curr_num
    
    def reset(self):
      self.curr_num = ''
