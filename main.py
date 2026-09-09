import string
categorias_validas = frozenset(["Mini Motos", "Figuras", "Guantes"]) 
escalas_validas = frozenset(["1:18", "1:12" ])
menu_list = frozenset(["1 - Agregar Producto", 
             "2 - Modificar Producto", 
             "3 - Eliminar Producto", 
             "4 - Registrar Venta"])

def validar_atributo_estricto(atributo: str, opciones_validas: frozenset) -> str:
    mensaje_consola = f"Lista de valores válidos para el atributo {atributo}: {', '.join(sorted(opciones_validas))}\nIngresa el atributo {atributo}: "
    while True:
        verificar_categoria = input(mensaje_consola).strip().lower().title()
        if verificar_categoria not in opciones_validas: 
            mensaje_consola = f"Entrada inválida. Ingresa un atributo válido {atributo} de la lista: "
        else:
            return verificar_categoria    

def validar_atributo_alfabetico(atributo: str, caracteres_permitidos: frozenset) -> str:
    mensaje_consola = f"Ingresa el atributo {atributo} del producto: "
    while True:
        verificar_atributo = input(mensaje_consola).strip().lower().title()
        if any(caracter not in caracteres_permitidos for caracter in verificar_atributo):
            mensaje_consola = f"Error, ingresa un {atributo} válido: "
        else:
            return verificar_atributo

def validar_atributo_numerico(atributo: str, conversion_tipo: type = float):
    mensaje_consola = f"Ingresa el atributo {atributo} del producto: "
    while True:
        entrada_usuario = input(mensaje_consola).strip()
        try:
            valor = conversion_tipo(entrada_usuario)
            if valor <= 0:
                raise ValueError
            return round(valor,2)
        except ValueError:
            if conversion_tipo == int:
                mensaje_consola = f"Error, ingresa un numero entero para {atributo}: "
            else:
                mensaje_consola = f"Error, ingresa valor válido para {atributo}: "
def generar_atributos() -> dict:

    formato_atributos = {"categoría": "",
                         "nombre": "", 
                         "color": "", 
                         "escala": "", 
                         "precio": 0, 
                         "unidades": 0,}
    
    formato_atributos["categoría"] = validar_atributo_estricto("categoría", categorias_validas)
    if formato_atributos["categoría"] == "Mini Motos":
        formato_atributos["nombre"] = validar_atributo_alfabetico("nombre", frozenset(string.ascii_letters + string.digits + " -"))
        formato_atributos["escala"] = validar_atributo_estricto("escala", escalas_validas)
    else:
        formato_atributos["nombre"] = validar_atributo_alfabetico("nombre", frozenset(string.ascii_letters))
        formato_atributos["escala"] = "N/A"
    formato_atributos["color"] = validar_atributo_alfabetico("color", frozenset(string.ascii_letters + "/"))
    formato_atributos["precio"] = validar_atributo_numerico("precio")
    formato_atributos["unidades"] = validar_atributo_numerico("unidades", conversion_tipo = int)
    return formato_atributos

def generar_sku(atributos: dict) -> str:
    sku = (atributos["categoría"][:2] + atributos["nombre"][:2] + atributos["color"][:2]).upper()
    return sku

def crear_producto(sku: str, atributos: dict) -> dict:
    return {sku:atributos}

def menu(options: frozenset):
    message = "Ingresa una opción: "
    message_error = "ERROR: Opción inválida"
    valid_options = {val_opt.strip() for opt in options for val_opt in opt.split("-", maxsplit=1)}
    print("Menú de opciones:\n" + "\n".join(sorted(options)))
    while True:
            selection = input(message).strip().title()
            if selection in valid_options: return selection 
            print(message_error)

def formato():
    productos_existentes = []
    productos_nuevos = []
    while True:
        election = menu(menu_list)
        match election:
            case "1" | "Agregar Producto":
                crear_producto(generar_sku, generar_atributos)

        #atributos_articulo = generar_atributos()
        #sku = generar_sku(atributos_articulo)
        #nuevo_producto = producto_terminado(sku, atributos_articulo)
        print(election)
        print(productos_nuevos)
        pass
formato()
