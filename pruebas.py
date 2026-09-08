
menu_list = frozenset(["1 - Agregar Producto", 
             "2 - Modificar Producto", 
             "3 - Eliminar Producto", 
             "4 - Registrar Venta"])

def test_menu_1(options: frozenset):
    message = "Ingresa una opción: "
    message_error = "Ingresa una opción válida del menú: "
    print("Menú de opciones:\n" + "\n".join(options))
    selection = input(message).strip().title()
    while True:
        for opt in options:
            if selection == "1" or selection == "Agregar producto" in opt: return 1
            if selection == "2" or selection == "Modificar producto" in opt: return 2
            if selection == "3" or selection == "Eliminar producto" in opt: return 3
            if selection == "4" or selection == "Registrar venta" in opt: return 4
        else:
            selection = input(message_error).strip().title()

def test_menu_2(options: frozenset):
    message = "Ingresa una opción: "
    message_error = "Ingresa una opción válida del menú: "
    print("Menú de opciones:\n" + "\n".join(options))
    selection = input(message).strip().title()
    valid_digits = [digit[:1] for digit in options]
    valid_text = [text[4:]for text in options]
    while True:
            if selection in valid_digits or selection in valid_text: return selection
            else:
                selection = input(message_error).strip().title()

def test_menu_3(options: frozenset):
    message = "Ingresa una opción: "
    message_error = "ERROR: Opción inválida"
    valid_options = {val_opt.strip() for opt in options for val_opt in opt.split("-", maxsplit=1)}
    print("Menú de opciones:\n" + "\n".join(sorted(options)))
    while True:
            selection = input(message).strip().title()
            if selection in valid_options: return selection 
            print(message_error)

#print(test_menu_1(menu_list))
#print(test_menu_2(menu_list))
print(test_menu_3(menu_list))