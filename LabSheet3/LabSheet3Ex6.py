pi=3.142
CylinderRadius=float(input("Please enter the radius of the cylinder: "))
CylinderHeight=float(input("Please enter the height of the cylinder: "))
AreaCylinder=(2*(pi*(CylinderRadius**2)))+(2*pi*CylinderHeight*CylinderRadius)
print("The total surface area of the cylinder:",AreaCylinder)