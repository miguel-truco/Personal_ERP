
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

class GestorArchivos:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return print("Cerrando recursos")

with GestorArchivos() as test:
     print(test)



#print(test_menu_1(menu_list))
#print(test_menu_2(menu_list))
#print(test_menu_3(menu_list))


def isolate_and_deduplicate(records: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
  """Filter duplicate dictionaries by key, preserving order and isolating elements.

  Parameters
  ----------
  records : List[Dict[str, Any]]
      Collection of dictionaries to process.
  key : str
      Dictionary key to evaluate for uniqueness.

  Returns
  -------
  List[Dict[str, Any]]
      New list containing unique records based on the first occurrence of key.
      Each dictionary in the output must be an independent copy.
  """
  viewed = set()
  result = []
  for record in records:
      if record[key] not in viewed:
          viewed.add(record[key])
          result.append(record.copy())
  return result

if __name__ == "__main__":
  input_data = [
      {"id": 101, "sku": "JACKET-01", "stock": 5},
      {"id": 102, "sku": "VEST-02", "stock": 3},
      {"id": 101, "sku": "JACKET-01-DUP", "stock": 99},
      {"id": 103, "sku": "BACKPACK-03", "stock": 8},
  ]

  # Test 1: Deduplication & Order
  result = isolate_and_deduplicate(input_data, "id")
  assert len(result) == 3, f"Expected 3 records, got {len(result)}"
  assert [r["id"] for r in result] == [101, 102, 103], "Order or IDs incorrect"
  assert result[0]["sku"] == "JACKET-01", "Did not retain first occurrence"

  # Test 2: Mutation Isolation
  result[0]["stock"] = 999
  assert input_data[0]["stock"] == 5, (
      "Memory leak detected: mutation affected original data"
  )

  # Test 3: Missing Key Handled Safely
  empty_result = isolate_and_deduplicate([], "id")
  assert empty_result == [], "Empty input should return empty list"

  print("GIMNASIO CASA: ALL ASSERTIONS PASSED (PASS)")