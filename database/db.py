

class DB:
    from models.clientModel import Client

    def __init__(self):
        self.cuentas = []
        self.load_from_db()

        

    def agregar_cuenta(self, cliente: 'Client'):
        if self.buscar_por_identificacion(cliente.identificationNumber):
            raise ValueError(f"Ya existe una cuenta con el número de identificación {cliente.identificationNumber}")
        else:
            #actualizar la base de datos con la nueva cuenta
            with open("StoreHistory.txt", "a") as file:
                self.cuentas.append(cliente)
                file.write(f"{cliente.identificationNumber},{cliente.name},{';'.join(cliente.billHistory)}\n")

    def mostrar_cuentas(self):
        for cuenta in self.cuentas:
            productos = []
            if cuenta.billHistory == [] :
                productos_str=[]
            else:
                for bill in cuenta.billHistory:
                    print(type(cuenta.billHistory))
                    productos.append(';'.join(bill._billProductList))
                productos_str = ';'.join(productos)
            print(f"Nombre: {cuenta.name}, Identificación: {cuenta.identificationNumber}, Historial de Facturas: {productos_str}")
            print("-" * 30)


    def agregar_factura(self, identificationNumber, facturas):
        cuenta = self.buscar_por_identificacion(int(identificationNumber))
        #guardar la factura en la BD en la cuenta del cliente
        if cuenta:
            self.actualizar_en_archivo(cuenta, facturas)
        else:
            raise ValueError(f"No se encontró la cuenta con número de identificación {identificationNumber}")

    def ver_historial_facturas(self, identificationNumber):
        cuenta = self.buscar_por_identificacion(identificationNumber)
        if cuenta:
            return cuenta.billHistory
        else:
            return []

    def buscar_por_identificacion(self, identificationNumber):
        for cuenta in self.cuentas:
            if cuenta.identificationNumber == identificationNumber:
                return cuenta
        return False

    def load_from_db(self):
        from models.clientModel import Client
        try:
            with open("StoreHistory.txt", "r") as file:
                for line in file:
                        identificationNumber, name, billHistory = line.strip().split(",")
                        billHistory = billHistory 
                        self.cuentas.append(Client(name, identificationNumber, billHistory))
        except FileNotFoundError:
            print("No se encontró la base de datos. Se creará una nueva.")
            open("StoreHistory.txt", "w").close()

        return self.cuentas
    
    def ver_facturas_de_cliente(self, identificationNumber):
        cuenta = self.buscar_por_identificacion(identificationNumber)
        if cuenta:
            factura="["
            for bill in cuenta.billHistory:
               factura=factura+"["+";".join(bill._billProductList)+","+"]"
            return factura
        else:
            return []
    
    def actualizar_en_archivo(self, cuenta: 'Client', billHistory):
        with open("StoreHistory.txt", "w") as file:
            for cuenta in self.cuentas:
                cuenta.billHistory = billHistory
                file.write(f"{cuenta.identificationNumber},{cuenta.name},{cuenta.billHistory}\n")

