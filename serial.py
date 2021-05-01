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
      """ initiates serial generator at a number, defauled to 100
        start: starting number
        curr_num: tracker for current generated number
      """
      self.start = start
      self.curr_num = ''
    
    def generate(self):
      """indexes and returns a number, starting from self.start"""
      if isinstance(self.curr_num, int):
        self.curr_num += 1 
      else:
        self.curr_num = self.start
      return self.curr_num
    
    def reset(self):
      """resets the curr_num so that obj generates the start number next"""
      self.curr_num = ''

    def __repr__(self):
      var = self.start if self.start == '' else self.start + 1
      return f"<SerialGenerator start={self.start} next={var}>"
