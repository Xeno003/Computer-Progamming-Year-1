distance=float(input("Please the distance need to be covered: "))
mpg=float(input("Please the miles per gallon of the car: "))
CostGallon=float(input("Please the cost of a gallon of fuel: "))
consumption=distance/mpg
tripcost=consumption*CostGallon
print("The total consumption for the trip is:",consumption)
print("The cost for the trip is:",tripcost)