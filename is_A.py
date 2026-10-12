class a:
 def f1(self):
  print("a class method")

class b(a):
 def f2(self):
  print("b class method")

b1=b()
b1.f1()
b1.f2()