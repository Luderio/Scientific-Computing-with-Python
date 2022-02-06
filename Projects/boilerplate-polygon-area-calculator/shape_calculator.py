class Rectangle:

  def __init__(self, width, height) :
    self.width = width
    self.height = height
  
  def __str__(self) :
    return "Rectangle(width=" + str(self.width) + ", " + "height=" + str(self.height) + ")"
  
  def set_width(self, width) :
    self.width = width
    return self.width
  
  def set_height(self, height) :
    self.height = height
    return self.height
  
  def get_area(self) :
    width = self.width
    height = self.height
    area = width * height
    return area

  def get_perimeter(self) :
    width = self.width
    height = self.height
    perimeter = 2 * width + 2 * height
    return perimeter
  
  def get_diagonal(self) :
    width = self.width
    height = self.height
    diagonal = ((width ** 2 + height ** 2) ** .5)
    return diagonal
  
  def get_picture(self) :
    if self.width > 50 or self.height > 50 :
      return "Too big for picture."
    string = (('*' * self.width + '\n') * self.height)

    return string
  
  def get_amount_inside(self, shape) :
    output = int(self.get_area() / shape.get_area())
    return output
  

class Square(Rectangle):

  def __init__(self, side) :
    self.side = side
    self.width = side
    self.height = side
  
  def __str__(self) :
    return "Square(side=" + str(self.side) + ")"
  
  def set_side(self, side) :
    self.side = side
    self.width = self.set_width(side)
    self.height = self.set_height(side)

