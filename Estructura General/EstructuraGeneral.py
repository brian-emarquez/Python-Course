#############################################
# Estructura General
############################################

class bantotal():

    def __init__(self, productoCliente, ProdTipo): 
        
        self.productoCliente = productoCliente 
        self.ProdTipo = ProdTipo
        
        #Creación de un nuevo método
    def Clientes(self):
        
        NroDocTit = (47133933, 71253247)
        ClienteID = (1,2)
        EsComp = ("N","S")
        NroDocComp = (" ",47133933)

        ClienteID = int(input("Dígite su Numero de Documento: "))
        if ClienteID > 0:
            if ClienteID:
                print(NroDocTit[0])
            else: 
                print("Error! Vuelva a digitar Oatra ves")
        else:
                print("Error! Numerop Negativo")   

        
    def Productos(self):

        ProductoID = ("CA12", "PR14", "CA13", "PR16", "CA34")
        ProdTipo = (1,2,1,2,1)

        ProdTipo = int(input("Dígite su Numero de Documento: "))
        if ProdTipo > 0:
            if ProdTipo:
                print(ProductoID[0])
            else: 
                print("Error! Vuelva a digitar Oatra ves")
        else:
                print("Error! Numerop Negativo")   

    def Producto_cliente(self):
        ClienteID
        ProductoID


ProductoClientes = bantotal("productoCliente", "ProdTipo")
ProductoClientes.Clientes()
#ProductoClientes2 = bantotal("productoCliente", "ProdTipo")
#ProductoClientes2.Productos()
