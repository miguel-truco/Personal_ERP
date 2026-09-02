import string
categorias_validas = ["Mini Motos", "Figuras", "Guantes"] 
escalas_validas = ["1:18", "1:12" ]

def validar_atributo_estricto(atributo: str, opciones_validas: frozenset) -> str:
    mensaje_consola = f"Lista de valores válidos para el atributo {atributo}: {', '.join(opciones_validas)}\nIngresa el atributo {atributo}: "
    while True:
        verificar_categoria = input(mensaje_consola).strip().lower().title()
        if verificar_categoria not in opciones_validas: 
            mensaje_consola = f"Entrada inválida. Ingresa un atributo válido {atributo} de la lista: "
        else:
            return verificar_categoria    

def validar_atributo_alfabetico(atributo: str, caracteres_permitidos : frozenset) -> str:
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
def crear_producto() -> dict:

    formato_producto = {"categoría": "",
                         "nombre": "", 
                         "color": "", 
                         "escala": "", 
                         "precio": 0, 
                         "unidades": 0,}
    
    formato_producto["categoría"] = validar_atributo_estricto("categoría", frozenset(categorias_validas))
    if formato_producto["categoría"] == "Mini Motos":
        formato_producto["nombre"] = validar_atributo_alfabetico("nombre", frozenset(string.ascii_letters + string.digits + " -"))
        formato_producto["escala"] = validar_atributo_estricto("escala", frozenset(escalas_validas))
    else:
        formato_producto["nombre"] = validar_atributo_alfabetico("nombre", frozenset(string.ascii_letters))
        formato_producto["escala"] = "N/A"
    formato_producto["color"] = validar_atributo_alfabetico("color", frozenset(string.ascii_letters + "/"))
    formato_producto["precio"] = validar_atributo_numerico("precio")
    formato_producto["unidades"] = validar_atributo_numerico("unidades", conversion_tipo = int)
    return formato_producto

def generar_sku(atributos: dict) -> str:
    sku = (atributos["categoría"][:2] + atributos["nombre"][:2] + atributos["color"][:2]).upper()
    return sku

def formatear_pedido():
    productos_existentes = {}
    productos_nuevos = {}
    atributos_articulo = crear_producto()
    sku = generar_sku(atributos_articulo)
    productos_nuevos[sku] = atributos_articulo
    print(productos_nuevos)
    pass

formatear_pedido()