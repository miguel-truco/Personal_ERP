import string
categorias_validas = ["Mini Motos", "Figuras", "Guantes"] 
escalas_validas = ["1:18", "1:12" ]
menu_list = ["1 - Agregar producto", "2 - Modificar producto", "3 - Eliminar producto", "4 - Registrar venta"]

def validar_atributo_estricto(atributo: str, opciones_validas: frozenset) -> str:
    mensaje_consola = f"Lista de valores válidos para el atributo {atributo}: {', '.join(opciones_validas)}\nIngresa el atributo {atributo}: "
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
    
    formato_atributos["categoría"] = validar_atributo_estricto("categoría", frozenset(categorias_validas))
    if formato_atributos["categoría"] == "Mini Motos":
        formato_atributos["nombre"] = validar_atributo_alfabetico("nombre", frozenset(string.ascii_letters + string.digits + " -"))
        formato_atributos["escala"] = validar_atributo_estricto("escala", frozenset(escalas_validas))
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

def producto_terminado(sku: str, atributos: dict) -> dict:
    return {sku:atributos}

def menu(options: frozenset):
    
    print("Menú de opciones:\n" + "\n".join(options))
    selection = input("Selecciona una opción del menú de opciones: ")
    if not selection in map(lambda v: options[v], options):
        while True:
            selection = input("Ingresa una opción válida: ")
            if selection in options: break
    pass

"""def formatear_pedido():
    productos_existentes = []
    productos_nuevos = []
    while True:

    atributos_articulo = generar_atributos()
    sku = generar_sku(atributos_articulo)
    nuevo_producto = producto_terminado(sku, atributos_articulo)
    print(productos_nuevos)
    pass"""

#formatear_pedido()
menu(menu_list)