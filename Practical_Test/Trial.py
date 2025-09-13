class Product:
    def __init__(self, barcode, name, price, ExpiryDate, QTY):
        self.barcode = barcode
        self.name = name
        self.price = price
        self._ExpiryDate = ExpiryDate
        self._QTY = QTY
    
    def __str__(self):
        return (f"Barcode: {self._Barcode}\n Name: {self._Name}\nPrice: {self._Price}"
                f"\nExpiry Date: {self._ExpiryDate}\nQuantity: {self._QTY}")

inventory = {}
file=open("d:\\University\\Coding\\Practical_Test\\barcode.txt", 'r')
products= file.read().split("\n\n")
for item in products:
    product=item.split()
    barcode=product[0]
    name = product[1]
    price = product[2]
    expirydate = product[3]
    quantity = product[4]
    
    one_product = Product(barcode, name, price, expirydate, quantity)
    inventory.update({barcode:one_product})
        


barcode = input("Enter barcode number to query: ")
        
if barcode in inventory:
    print(Product.barcode = barcode)
else:
    print("Error: Item not found in the database.")
