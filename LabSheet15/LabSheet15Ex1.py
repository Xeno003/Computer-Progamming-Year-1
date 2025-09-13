'''
A property agency performs the sales of both immovable and movable
properties. Immovable properties consist of land with or without a building.
Movable properties are vehicles.

It wishes to have a computerised system to manage its transactions.

For all properties on its sales list, it needs to store: Property Id, the surname,
first name and address of the owner and the cost of the property.

For immovable properties, it needs to store the location (name of the town
or village), the area of the land, whether it contains a building or not and area of the building (if any.

For movable properties, it should store the type (car, lorry, bus), the engine
capacity, model and the make.

(a)Develop a suitable base class (super class) and two suitable subclasses to
represent immovable and movable properties.

(b) Write a main() function that inputs data for five movable properties and
five immovable properties and stores the data in relevant lists.

(c) For each class of properties, the program should calculate the average
cost and display the details of all properties (of the class) which are above
the average cost.
'''

class Property:
    def __init__(self,Property_Id,surname,first_name,address,cost):
        self._Property_Id = Property_Id
        self._surname = surname
        self._first_name = first_name
        self._address = address
        self._cost = cost
    
    def __str__(self):
        return ("Property ID:", self._Property_Id , "\n", "Owner:" ,self._first_name , self._surname , "\n" , "Address:", self._address, "\n","Cost:", self._cost)

class Imovable(Property):
    def __init__(self,location,area_land,building,area_building):
        self._location = location
        self._area_land = area_land
        self._building = building
        if building==True:
            self._area_building = area_building
    
    def __str__(self):
        return("Location:",self._location, "\n", "Area of Land(m2):", self._area_land,"\n", "Contains a building:",self._building,"\n","Area of the building",self._area_building )

class Movable(Property):
    def __init__(self, type,engine_capacity,model,make):
        self._type = type
        self._engine_capacity = engine_capacity
        self._model = model
        self._make = make
    
    def __str__(self):
        return("Vehicle's type:",self._type, "\n", "Vehicle's engine capacity:",self._engine_capacity,"\n", "Vehicle's model:",self._model,"\n","Vehicle's make",self._make)

for i in range (10):
    Property_Id_main=input("Enter the property id: ")
    surname_main = input("Enter the surname of the owner: ")
    firstname_main = input("Enter the first name of the owner: ")
    address_main =  input("Enter the address of the owner: ")
    cost_main =  input("Enter the cost of the property: ")

    prop = Property(Property_Id_main,surname_main,firstname_main,address_main,cost_main)
    if i < 5:
        type_main=input("Enter the type of the vehicle(car/lorry/bus): ")
        engine_capacity_main=input("Enter the engine capacity of the vehicle: ")
        model_main=input("Enter the model of the vehicle: ")
        make_main=input("Enter the make of the vehicle: ")

        movable = Movable(type_main,engine_capacity_main,model_main,make_main)
    else:
        location_main=input("Enter the location of the property: ")
        area_land_main=input("Enter the area of the property: ")
        buildingchecker= input("Is the a building on the property?(Y/N) ")
        buildingchecker.lower()
        if buildingchecker=="y":
            building_main=True
            area_building_main=input("Enter the area covered by the building: ")
        else:
            building_main=False
            area_building_main="NA"
        immovable = Imovable(location_main,area_land_main, building_main,area_building_main)


