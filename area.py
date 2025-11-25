from graphics.rectFunctions import*
from graphics.cirFunction import*
from graphics.DGraphics.sphere import*
from graphics.DGraphics.cuboid import*

l=int(input("Enter lenght:"))
b=int(input("Enter breadth:"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))

r=int(input("Enter radius of circle:"))
print("circle Area=",CirArea(r))
print("circle volume=",CirPerimeter(r))

r=int(input("Enter radius of sphere:"))
print("sphere Area=",SpArea(r))
print("sphere volume=",SpPerimeter(r))


l=int(input("Enter cuboid lenght:"))
b=int(input("Enter cuboid breadth:"))
h=int(input("Enter cuboid height:"))
print("cuboid Area=",CubArea(l,b,h))
print("cuboid Perimeter=",CubPerimeter(l,b,h))
