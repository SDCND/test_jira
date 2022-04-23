# Dr. Kaputa
# hello world via a class
# simple argument passing

class Printer():
  def __init__(self):
    self.runCode()
      
  def runCode(self): 
    print ("Hello World\n")
    
class Complex:
  def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart
  
def main():
  data = Complex(3.0,-4.5)
  print(data.r)
  print(data.i)
  printer = Printer()
  
if __name__ == '__main__':
  main()