# Trabajo Práctico Integrador (TPI)
# Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

# VARIABLES GLOBALES
paises = []
continentes_validos = ["América", "Asia", "Europa", "África", "Oceanía", "Antártida"]
archivo_csv = "paises.csv"


# ============= FUNCIONES DE CARGA Y GUARDADO =============


def cargar_csv():
    """Carga datos desde el archivo CSV al inicio del programa"""

    # Crear archivo vacío si no existe (modo "a" = append, crea si no existe)
    archivo_temp = open(archivo_csv, "a", encoding="utf-8")
    archivo_temp.close()

    # Ahora leer el archivo (ya existe garantizado)
    archivo = open(archivo_csv, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    # Si el archivo está vacío o solo tiene encabezado, llenar con datos iniciales
    if len(lineas) == 0 or len(lineas) == 1:
        print("⚠ Archivo CSV vacío. Creando datos iniciales...\n")
        archivo = open(archivo_csv, "w", encoding="utf-8")
        archivo.write("nombre,poblacion,superficie,continente\n")

        datos_iniciales = [
            "Argentina,45376763,2780400,América",
            "Japón,125800000,377975,Asia",
            "Brasil,213993437,8515767,América",
            "Alemania,83149300,357022,Europa",
            "India,1417173173,3287263,Asia",
            "Nigeria,223804632,923768,África",
            "Australia,26068792,7692024,Oceanía",
            "Rusia,144444359,17098242,Europa",
            "México,128932753,1964375,América",
            "China,1425887337,9596961,Asia",
        ]

        for dato in datos_iniciales:
            archivo.write(dato + "\n")

        archivo.close()
        print("✓ Archivo CSV creado exitosamente\n")

        # Releer el archivo
        archivo = open(archivo_csv, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

    contador_cargados = 0
    for i in range(1, len(lineas)):
        linea = lineas[i].strip()
        if linea:
            partes = linea.split(",")

            # Validar que tenga exactamente 4 campos
            if len(partes) != 4:
                print(f"⚠ Fila {i} ignorada: número de campos incorrecto")
                continue

            nombre, poblacion, superficie, continente = partes

            # Validar campos no vacíos
            if not nombre or not poblacion or not superficie or not continente:
                print(f"⚠ Fila {i} ignorada: campos vacíos")
                continue

            # Validar que población y superficie sean números
            poblacion_valida = True
            for caracter in poblacion:
                if caracter < "0" or caracter > "9":
                    poblacion_valida = False
                    break

            superficie_valida = True
            for caracter in superficie:
                if caracter < "0" or caracter > "9":
                    superficie_valida = False
                    break

            if not poblacion_valida or not superficie_valida:
                print(f"⚠ Fila {i} ignorada: población o superficie no son números")
                continue

            # Validar que sean mayores a 0
            if int(poblacion) <= 0 or int(superficie) <= 0:
                print(
                    f"⚠ Fila {i} ignorada: población o superficie deben ser mayores a 0"
                )
                continue

            # Validar duplicados en archivo CSV editado manualmente
            if any(p["nombre"].lower() == nombre.strip().lower() for p in paises):
                print(f"⚠ País duplicado en línea {i}: '{nombre}' ignorado.")
                continue

            paises.append(
                {
                    "nombre": nombre.strip(),
                    "poblacion": int(poblacion),
                    "superficie": int(superficie),
                    "continente": continente.strip(),
                }
            )
            contador_cargados += 1

    print(f"✓ Se cargaron {contador_cargados} países del archivo CSV\n")


def guardar_csv():
    """Guarda la lista de países actualizada al archivo CSV"""
    archivo = open(archivo_csv, "w", encoding="utf-8")
    archivo.write("nombre,poblacion,superficie,continente\n")

    for pais in paises:
        # Validar tipos antes de guardar
        nombre = str(pais["nombre"]).strip()
        poblacion = str(pais["poblacion"])
        superficie = str(pais["superficie"])
        continente = str(pais["continente"]).strip()

        linea = f"{nombre},{poblacion},{superficie},{continente}\n"
        archivo.write(linea)

    archivo.close()
    print("✓ Datos guardados en CSV\n")


# ============= FUNCIONES DE VALIDACIÓN =============


def validar_no_vacio(valor, nombre_campo):
    """Valida que un campo no esté vacío"""
    if not valor or valor.strip() == "":
        print(f"✗ Error: {nombre_campo} no puede estar vacío")
        return False
    return True


def validar_numero(valor, nombre_campo):
    """Valida que un valor sea un número positivo"""
    if not valor:
        print(f"✗ Error: {nombre_campo} no puede estar vacío")
        return False

    es_numero = True
    for caracter in valor:
        if caracter < "0" or caracter > "9":
            es_numero = False
            break

    if not es_numero:
        print(f"✗ Error: {nombre_campo} debe contener solo dígitos")
        return False

    numero = int(valor)
    if numero <= 0:
        print(f"✗ Error: {nombre_campo} debe ser mayor a 0")
        return False

    return True


def pais_existe(nombre):
    """Verifica si un país ya existe en la lista"""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return True
    return False


def buscar_pais_por_nombre(nombre):
    """Retorna el índice de un país si existe, sino retorna -1"""
    for i in range(len(paises)):
        if paises[i]["nombre"].lower() == nombre.lower():
            return i
    return -1

def seleccionar_continente():
    """Muestra la lista de continentes y pide una selección numérica al usuario."""
    print("\n--- SELECCIÓN DE CONTINENTE ---")
    
    for i in range(len(continentes_validos)):
        print(f"  {i + 1}. {continentes_validos[i]}")

    seleccion = input("Seleccione continente por número (1-6): ").strip()
    
    if seleccion.isdigit():
        indice = int(seleccion)
        if 1 <= indice <= len(continentes_validos):
            return continentes_validos[indice - 1]
    
    print("✗ Error: Selección de continente inválida.")
    return None

# ============= FUNCIONES DE GESTIÓN =============


def agregar_pais():
    """Agrega un nuevo país con validación de campos"""
    print("\n--- AGREGAR NUEVO PAÍS ---")

    nombre = input("Nombre del país: ").strip()
    if not validar_no_vacio(nombre, "Nombre"):
        return

    # Validar que nombre solo contenga letras, espacios y guiones (incluye acentos y ñ)
    nombre_valido = True
    for caracter in nombre:
        if not (
            (caracter.lower() >= "a" and caracter.lower() <= "z")
            or caracter in " áéíóúÁÉÍÓÚñÑ-"
        ):
            nombre_valido = False
            break

    if not nombre_valido:
        print("✗ Error: Nombre solo puede contener letras, espacios y guiones")
        return

    if pais_existe(nombre):
        print(f"✗ Error: El país '{nombre}' ya existe")
        return

    poblacion = input("Población: ").strip()
    if not validar_numero(poblacion, "Población"):
        return

    superficie = input("Superficie (km²): ").strip()
    if not validar_numero(superficie, "Superficie"):
        return

    continente = seleccionar_continente() 
    if continente is None: 
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente,
    }

    paises.append(nuevo_pais)
    guardar_csv()
    print(f"✓ País '{nombre}' agregado exitosamente\n")


def actualizar_pais():
    """Actualiza población y superficie de un país"""
    print("\n--- ACTUALIZAR PAÍS ---")

    nombre = input("Nombre del país a actualizar: ").strip()
    if not validar_no_vacio(nombre, "Nombre"):
        return

    indice = buscar_pais_por_nombre(nombre)
    if indice == -1:
        print(f"✗ Error: País '{nombre}' no encontrado\n")
        return

    print(f"\nDatos actuales: {paises[indice]}")

    poblacion = input("Nueva población (o Enter para mantener): ").strip()
    if poblacion and validar_numero(poblacion, "Población"):
        paises[indice]["poblacion"] = int(poblacion)
    elif poblacion:
        return

    superficie = input("Nueva superficie (o Enter para mantener): ").strip()
    if superficie and validar_numero(superficie, "Superficie"):
        paises[indice]["superficie"] = int(superficie)
    elif superficie:
        return

    guardar_csv()
    print(f"✓ País '{nombre}' actualizado\n")


def buscar_pais():
    """Busca países por nombre (coincidencia parcial o exacta)"""
    print("\n--- BUSCAR PAÍS ---")

    busqueda = input("Ingrese nombre (o parte de él): ").strip().lower()
    if not validar_no_vacio(busqueda, "Búsqueda"):
        return

    resultados = []
    for p in paises:
        if busqueda in p["nombre"].lower():
            resultados.append(p)

    if not resultados:
        print(f"✗ No se encontraron países con '{busqueda}'\n")
        return

    print(f"\n✓ Se encontraron {len(resultados)} resultado(s):")
    mostrar_tabla(resultados)


def filtrar_por_continente():
    """Filtra países por continente"""
    print("\n--- FILTRAR POR CONTINENTE ---")

     # Se usa la lista validada de continentes para evitar valores incorrectos
    print("\nContinentes disponibles:")
    for i in range(len(continentes_validos)):
        print(f"  {i + 1}. {continentes_validos[i]}")

    seleccion = input("Seleccione continente (número): ").strip()
    if (
        not seleccion.isdigit()
        or int(seleccion) < 1
        or int(seleccion) > len(continentes_validos)
    ):
        print("✗ Error: Selección inválida\n")
        return

    continente_filtro = continentes_validos[int(seleccion) - 1]
    resultados = []
    for p in paises:
        if p["continente"] == continente_filtro:
            resultados.append(p)

    print(f"\n✓ Países en {continente_filtro}: {len(resultados)}")
    mostrar_tabla(resultados)


def filtrar_por_poblacion():
    """Filtra países por rango de población"""
    print("\n--- FILTRAR POR POBLACIÓN ---")

    poblacion_min = input("Población mínima: ").strip()
    if not validar_numero(poblacion_min, "Población mínima"):
        return

    poblacion_max = input("Población máxima: ").strip()
    if not validar_numero(poblacion_max, "Población máxima"):
        return

    p_min = int(poblacion_min)
    p_max = int(poblacion_max)

    if p_min > p_max:
        print("✗ Error: Mínimo no puede ser mayor que máximo\n")
        return

    resultados = []
    for p in paises:
        if p_min <= p["poblacion"] <= p_max:
            resultados.append(p)

    if not resultados:
        print(f"✗ No hay países en el rango {p_min:,} - {p_max:,}\n")
        return

    print(f"\n✓ Se encontraron {len(resultados)} país(es):")
    mostrar_tabla(resultados)


def filtrar_por_superficie():
    """Filtra países por rango de superficie"""
    print("\n--- FILTRAR POR SUPERFICIE ---")

    superficie_min = input("Superficie mínima (km²): ").strip()
    if not validar_numero(superficie_min, "Superficie mínima"):
        return

    superficie_max = input("Superficie máxima (km²): ").strip()
    if not validar_numero(superficie_max, "Superficie máxima"):
        return

    s_min = int(superficie_min)
    s_max = int(superficie_max)

    if s_min > s_max:
        print("✗ Error: Mínimo no puede ser mayor que máximo\n")
        return

    resultados = []
    for p in paises:
        if s_min <= p["superficie"] <= s_max:
            resultados.append(p)

    if not resultados:
        print(f"✗ No hay países en el rango {s_min:,} - {s_max:,}\n")
        return

    print(f"\n✓ Se encontraron {len(resultados)} país(es):")
    mostrar_tabla(resultados)


# ============= FUNCIONES DE ORDENAMIENTO =============


def ordenar_por_nombre():
    """Ordena países alfabéticamente por nombre"""
    print("\n--- ORDENAR POR NOMBRE ---")

    # Verificación de lista vacía antes de ordenar
    if not paises:
        print("✗ No hay países para ordenar.\n")
        return

    orden = input("¿Ascendente (A) o Descendente (D)?: ").upper().strip()
    if orden not in ["A", "D"]:
        print("✗ Error: Ingrese 'A' o 'D'\n")
        return

    resultados = paises.copy()

    for i in range(len(resultados)):
        for j in range(len(resultados) - 1):
            if orden == "A":
                if resultados[j]["nombre"] > resultados[j + 1]["nombre"]:
                    resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
            else:
                if resultados[j]["nombre"] < resultados[j + 1]["nombre"]:
                    resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]

    print(f"\n✓ Países ordenados por nombre ({orden}):")
    mostrar_tabla(resultados)


def ordenar_por_poblacion():
    """Ordena países por población"""
    print("\n--- ORDENAR POR POBLACIÓN ---")

    orden = input("¿Ascendente (A) o Descendente (D)?: ").upper().strip()
    if orden not in ["A", "D"]:
        print("✗ Error: Ingrese 'A' o 'D'\n")
        return

    resultados = paises.copy()

    for i in range(len(resultados)):
        for j in range(len(resultados) - 1):
            if orden == "A":
                if resultados[j]["poblacion"] > resultados[j + 1]["poblacion"]:
                    resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
            else:
                if resultados[j]["poblacion"] < resultados[j + 1]["poblacion"]:
                    resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]

    print(f"\n✓ Países ordenados por población ({orden}):")
    mostrar_tabla(resultados)


def ordenar_por_superficie():
    """Ordena países por superficie"""
    print("\n--- ORDENAR POR SUPERFICIE ---")

    orden = input("¿Ascendente (A) o Descendente (D)?: ").upper().strip()
    if orden not in ["A", "D"]:
        print("✗ Error: Ingrese 'A' o 'D'\n")
        return

    resultados = paises.copy()

    for i in range(len(resultados)):
        for j in range(len(resultados) - 1):
            if orden == "A":
                if resultados[j]["superficie"] > resultados[j + 1]["superficie"]:
                    resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
            else:
                if resultados[j]["superficie"] < resultados[j + 1]["superficie"]:
                    resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]

    print(f"\n✓ Países ordenados por superficie ({orden}):")
    mostrar_tabla(resultados)


# ============= FUNCIONES DE ESTADÍSTICAS =============


def estadisticas_poblacion():
    """Calcula estadísticas de población"""
    if not paises:
        print("✗ No hay países en la base de datos\n")
        return

    mayor = paises[0]["poblacion"]
    menor = paises[0]["poblacion"]
    suma_poblacion = 0
    pais_mayor = paises[0]
    pais_menor = paises[0]

    for p in paises:
        suma_poblacion += p["poblacion"]
        if p["poblacion"] > mayor:
            mayor = p["poblacion"]
            pais_mayor = p
        if p["poblacion"] < menor:
            menor = p["poblacion"]
            pais_menor = p

    promedio = suma_poblacion // len(paises)

    print("\n--- ESTADÍSTICAS DE POBLACIÓN ---")
    print(f"País con MAYOR población: {pais_mayor['nombre']} ({mayor:,} habitantes)")
    print(f"País con MENOR población: {pais_menor['nombre']} ({menor:,} habitantes)")
    print(f"Población PROMEDIO: {promedio:,} habitantes\n")


def estadisticas_superficie():
    """Calcula estadísticas de superficie"""
    if not paises:
        print("✗ No hay países en la base de datos\n")
        return

    suma_superficie = 0
    for p in paises:
        suma_superficie += p["superficie"]

    promedio = suma_superficie // len(paises)

    print("\n--- ESTADÍSTICAS DE SUPERFICIE ---")
    print(f"Superficie PROMEDIO: {promedio:,} km²\n")


def estadisticas_continentes():
    """Cuenta países por continente"""
    if not paises:
        print("✗ No hay países en la base de datos\n")
        return

    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente not in continentes:
            continentes[continente] = 0
        continentes[continente] += 1

    continentes_ordenados = []
    for continente in continentes:
        continentes_ordenados.append(continente)
    continentes_ordenados.sort()

    print("\n--- CANTIDAD DE PAÍSES POR CONTINENTE ---")
    for continente in continentes_ordenados:
        print(f"  {continente}: {continentes[continente]} país(es)")
    print()


# ============= FUNCIÓN DE VISUALIZACIÓN =============


def mostrar_tabla(lista_paises):
    """Muestra países en formato tabla"""
    if not lista_paises:
        print("(Lista vacía)\n")
        return

    print(
        "\n{:<25} {:<15} {:<15} {:<15}".format(
            "Nombre", "Población", "Superficie", "Continente"
        )
    )
    print("-" * 70)

    for pais in lista_paises:
        nombre = pais["nombre"]
        poblacion = f"{pais['poblacion']:,}"
        superficie = f"{pais['superficie']:,}"
        continente = pais["continente"]

        print(
            "{:<25} {:<15} {:<15} {:<15}".format(
                nombre, poblacion, superficie, continente
            )
        )
    print()


# ============= MENÚ PRINCIPAL =============


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "=" * 50)
    print("   GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 50)
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar por continente")
    print("5. Filtrar por población")
    print("6. Filtrar por superficie")
    print("7. Ordenar por nombre")
    print("8. Ordenar por población")
    print("9. Ordenar por superficie")
    print("10. Estadísticas de población")
    print("11. Estadísticas de superficie")
    print("12. Estadísticas de continentes")
    print("13. Ver todos los países")
    print("14. Salir")
    print("=" * 50)


def menu():
    """Ejecuta el menú principal del programa"""
    cargar_csv()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-14): ").strip()

        if opcion == "1":
            agregar_pais()
        elif opcion == "2":
            actualizar_pais()
        elif opcion == "3":
            buscar_pais()
        elif opcion == "4":
            filtrar_por_continente()
        elif opcion == "5":
            filtrar_por_poblacion()
        elif opcion == "6":
            filtrar_por_superficie()
        elif opcion == "7":
            ordenar_por_nombre()
        elif opcion == "8":
            ordenar_por_poblacion()
        elif opcion == "9":
            ordenar_por_superficie()
        elif opcion == "10":
            estadisticas_poblacion()
        elif opcion == "11":
            estadisticas_superficie()
        elif opcion == "12":
            estadisticas_continentes()
        elif opcion == "13":
            print("\n--- TODOS LOS PAÍSES ---")
            mostrar_tabla(paises)
        elif opcion == "14":
            print("\n✓ ¡Hasta luego!\n")
            break
        else:
            print("✗ Error: Opción no válida. Intente nuevamente.\n")


# ============= PUNTO DE ENTRADA =============

menu()
