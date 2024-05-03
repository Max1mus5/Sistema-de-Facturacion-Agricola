from app.app import Crud 

#crear productos de para la tienda
store = []
#productos de control de plagas:
store.append(Crud.Store.create_product("plague", "herbicida", 123456, 5, 150000.3))
store.append(Crud.Store.create_product("plague", "fungicida", 123457, 3, 12000.5))
store.append(Crud.Store.create_product("plague", "insecticida", 123458, 4, 5000.2))
store.append(Crud.Store.create_product("plague", "acaricida", 123459, 12, 10000.1))
store.append(Crud.Store.create_product("plague", "nematicida", 123460, 7, 20000.4))

#productos de control de fertilizantes:
store.append(Crud.Store.create_product("fertilizer", "nitrogeno", 123461, 5, 150000.3))
store.append(Crud.Store.create_product("fertilizer", "fosforo", 123462, 3, 12000.5))
store.append(Crud.Store.create_product("fertilizer", "potasio", 123463, 4, 5000.2))
store.append(Crud.Store.create_product("fertilizer", "calcio", 123464, 12, 10000.1))
store.append(Crud.Store.create_product("fertilizer", "magnesio", 123465,  7, 20000.4))

storeAntibiotics = []
#productos de antibioticos:
storeAntibiotics.append(Crud.Store.create_antibiotic("penicilina", "Bovinos", 150000.3, 402))
storeAntibiotics.append(Crud.Store.create_antibiotic("amoxicilina", "Caprinos", 12000.5, 500))
storeAntibiotics.append(Crud.Store.create_antibiotic("cefalosporina", "Porcinos", 5000.2, 599))
storeAntibiotics.append(Crud.Store.create_antibiotic("tetraciclina", "Bovinos", 10000.1, 505))

clientlist = []
options = Crud.Menu()
op = options

while op!= 10:
    op = options.show_menu()
    options.seleccionar_opcion(opcion=op, store=store, storeAntibiotics=storeAntibiotics)


""" tests for  the app: python -m unittest testing.appTest """
