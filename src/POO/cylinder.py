class Cylinder: 

  def __init__(self, height=1, radius=1):
    self.coor1 = height
    self.coor2 = radius
  
  def volume(self):
    return self.height * 3.14 * (self.radius)**2
  
  def surface_area(self):
    top = 3.14 * (self.radius**2)
    return (2*top) + (2*3.14*self.radius*self.height)
  