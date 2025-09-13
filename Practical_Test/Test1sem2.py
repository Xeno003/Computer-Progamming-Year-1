myProducts={}
class Product:
    def __init__(self, Barcode, Name, Price, ExpiryDate, QTY):
    
        self._Barcode = Barcode
        self._Name = Name
        self._Price = Price
        self._ExpiryDate = ExpiryDate
        self._QTY = QTY

    def __str__(self): 
        return (f"Barcode: {self._Barcode}\n Name: {self._Name}\nPrice: {self._Price}"
                f"\nExpiry Date: {self._ExpiryDate}\nQuantity: {self._QTY}")
    

    