# Gestión de Datos de Países en Python

## 📋 Descripción del Programa

Sistema interactivo desarrollado en **Python 3.x** que permite gestionar información sobre países de todo el mundo. La aplicación ofrece funcionalidades completas para filtrar, ordenar y generar estadísticas sobre una base de datos de países con información sobre población, superficie y continente.

### Objetivo Principal

Afianzar el uso de estructuras de datos fundamentales (listas y diccionarios), funciones modularizadas, validaciones de entrada y técnicas de filtrado/ordenamiento, aplicando conceptos clave de Programación 1.

### Características Principales

✅ **Gestión de Datos**: Agregar, actualizar y buscar países  
✅ **Filtrado Avanzado**: Por continente, rango de población y rango de superficie  
✅ **Ordenamientos**: Por nombre, población y superficie (ascendente/descendente)  
✅ **Estadísticas**: Análisis de población, superficie y distribución por continente  
✅ **Persistencia**: Los datos se guardan automáticamente en archivo CSV  
✅ **Validaciones Robustas**: Control de tipos de dato y formato de entrada  
✅ **Interfaz Amigable**: Menú interactivo en consola

---

## 🚀 Instrucciones de Uso

### Requisitos Previos

- **Python 3.x** instalado en tu sistema
- Sistema operativo: Windows, macOS o Linux
- Terminal/Command Prompt accesible

### Instalación

1. **Clonar o descargar el repositorio**

```bash
git clone https://github.com/tuusuario/programacion_1_tp_integrador.git
cd programacion_1_tp_integrador
```

2. **Ejecutar el programa**

```bash
python3 main.py
```

O en Windows:

```bash
python main.py
```

### Uso del Programa

Al ejecutar el programa, aparecerá un **menú interactivo** con 14 opciones:

```
==================================================
   GESTIÓN DE DATOS DE PAÍSES
==================================================
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar por continente
5. Filtrar por población
6. Filtrar por superficie
7. Ordenar por nombre
8. Ordenar por población
9. Ordenar por superficie
10. Estadísticas de población
11. Estadísticas de superficie
12. Estadísticas de continentes
13. Ver todos los países
14. Salir
==================================================
```

### Descripción de Cada Opción

| Opción                              | Descripción                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| **1. Agregar país**                 | Ingresa un nuevo país con población, superficie y continente |
| **2. Actualizar país**              | Modifica la población y/o superficie de un país existente    |
| **3. Buscar país**                  | Busca países por nombre (búsqueda parcial)                   |
| **4. Filtrar por continente**       | Muestra todos los países de un continente específico         |
| **5. Filtrar por población**        | Muestra países en un rango de población determinado          |
| **6. Filtrar por superficie**       | Muestra países en un rango de superficie determinado         |
| **7. Ordenar por nombre**           | Ordena alfabéticamente (A→Z o Z→A)                           |
| **8. Ordenar por población**        | Ordena por cantidad de habitantes                            |
| **9. Ordenar por superficie**       | Ordena por km²                                               |
| **10. Estadísticas de población**   | Muestra país con mayor/menor población y promedio            |
| **11. Estadísticas de superficie**  | Calcula superficie promedio                                  |
| **12. Estadísticas de continentes** | Cuenta cuántos países hay por continente                     |
| **13. Ver todos los países**        | Muestra toda la base de datos en formato tabla               |
| **14. Salir**                       | Cierra el programa guardando los cambios                     |

---

## 📊 Ejemplos de Entradas y Salidas

### Ejemplo 1: Agregar un País

**Entrada del Usuario:**

```
Seleccione una opción (1-14): 1

--- AGREGAR NUEVO PAÍS ---
Nombre del país: Canadá
Población: 39742826
Superficie (km²): 9984670
Continente: América
```

**Salida esperada:**

```
✓ País 'Canadá' agregado exitosamente

Datos guardados en CSV
```

---

### Ejemplo 2: Buscar un País

**Entrada del Usuario:**

```
Seleccione una opción (1-14): 3

--- BUSCAR PAÍS ---
Ingrese nombre (o parte de él): Japó
```

**Salida esperada:**

```
✓ Se encontraron 1 resultado(s):

Nombre                    Población       Superficie      Continente
----------------------------------------------------------------------
Japón                     125,800,000     377,975         Asia

```

---

### Ejemplo 3: Filtrar por Población

**Entrada del Usuario:**

```
Seleccione una opción (1-14): 5

--- FILTRAR POR POBLACIÓN ---
Población mínima: 100000000
Población máxima: 500000000
```

**Salida esperada:**

```
✓ Se encontraron 3 país(es):

Nombre                    Población       Superficie      Continente
----------------------------------------------------------------------
India                     1,417,173,173   3,287,263       Asia
Brasil                    213,993,437     8,515,767       América
China                     1,425,887,337   9,596,961       Asia

```

---

### Ejemplo 4: Ordenar por Nombre (Descendente)

**Entrada del Usuario:**

```
Seleccione una opción (1-14): 7

--- ORDENAR POR NOMBRE ---
¿Ascendente (A) o Descendente (D)?: D
```

**Salida esperada:**

```
✓ Países ordenados por nombre (D):

Nombre                    Población       Superficie      Continente
----------------------------------------------------------------------
Rusia                     144,444,359     17,098,242      Europa
Nigeria                   223,804,632     923,768         África
México                    128,932,753     1,964,375       América
Japón                     125,800,000     377,975         Asia
India                     1,417,173,173   3,287,263       Asia
Alemania                  83,149,300      357,022         Europa
China                     1,425,887,337   9,596,961       Asia
Brasil                    213,993,437     8,515,767       América
Australia                 26,068,792      7,692,024       Oceanía
Argentina                 45,376,763      2,780,400       América

```

---

### Ejemplo 5: Estadísticas de Población

**Entrada del Usuario:**

```
Seleccione una opción (1-14): 10
```

**Salida esperada:**

```
--- ESTADÍSTICAS DE POBLACIÓN ---
País con MAYOR población: China (1,425,887,337 habitantes)
País con MENOR población: Australia (26,068,792 habitantes)
Población PROMEDIO: 449,622,025 habitantes
```

---

### Ejemplo 6: Estadísticas de Continentes

**Entrada del Usuario:**

```
Seleccione una opción (1-14): 12
```

**Salida esperada:**

```
--- CANTIDAD DE PAÍSES POR CONTINENTE ---
  África: 1 país(es)
  América: 3 país(es)
  Asia: 4 país(es)
  Europa: 2 país(es)
  Oceanía: 1 país(es)
```

---

### Ejemplo 7: Validación de Errores

**Entrada del Usuario (inválida):**

```
Seleccione una opción (1-14): 1

--- AGREGAR NUEVO PAÍS ---
Nombre del país:
```

**Salida esperada:**

```
✗ Error: Nombre no puede estar vacío
```

---

## 👥 Participación de los Integrantes

### Equipo de Desarrollo

Este proyecto fue desarrollado por un equipo de **2 integrantes** en el contexto de la asignatura **Programación 1** de la Tecnicatura Universitaria en Programación (modalidad a distancia).

#### Responsabilidades Distribuidas

| Integrante                 | Rol Principal               | Contribuciones                                                                                                                                                        |
| -------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gerardo Martin Dalesio** | Diseño y Estructura         | • Diseño general del programa<br>• Funciones de gestión (agregar, actualizar, buscar)<br>• Funciones de filtrado<br>• Manejo de archivos CSV<br>• Testing y debugging |
| **Francisco Urrea**        | Implementación y Validación | • Funciones de ordenamiento<br>• Funciones de estadísticas<br>• Sistema de validaciones<br>• Manejo de errores<br>• Documentación y README                            |

### Competencias Desarrolladas

✅ **Programación Estructurada**: Uso de funciones, listas y diccionarios  
✅ **Manejo de Datos**: Lectura/escritura de archivos CSV  
✅ **Validación de Entrada**: Control de tipos y formatos  
✅ **Algoritmos**: Ordenamientos (Bubble Sort) y búsquedas  
✅ **Colaboración**: Trabajo en equipo y distribución de tareas  
✅ **Documentación**: Código comentado y documentación clara  
✅ **Control de Versiones**: Uso de Git y GitHub

### Proceso de Desarrollo

1. **Análisis de Requerimientos** (Semana 1)

   - Definición de funcionalidades
   - Diseño de estructura de datos

2. **Implementación** (Semana 2-3)

   - Desarrollo modular por integrante
   - Testing constante

3. **Integración y Testing** (Semana 4)

   - Unificación de código
   - Pruebas de todas las funcionalidades

4. **Documentación** (Semana 4-5)
   - Documentación del código
   - Creación del README
   - Preparación de video explicativo

### Commits Principales

```
Inicial: Sistema de gestión de países en Python
Agregar funciones de filtrado y ordenamiento
Implementar sistema de validaciones
Agregar estadísticas y análisis
Documentación final y README
```

---

## 📁 Estructura del Proyecto

```
programacion_1_tp_integrador/
├── main.py                 # Programa principal
├── paises.csv              # Base de datos (se crea automáticamente)
└── README.md               # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Estructuras de Datos**: Listas, Diccionarios
- **Manejo de Archivos**: Lectura/Escritura CSV nativo
- **Control de Versiones**: Git y GitHub
- **Documentación**: Markdown

---

## 📝 Notas Técnicas

- El programa **NO utiliza módulos externos**
- Los datos se **guardan automáticamente** en `paises.csv` después de cada operación
- Las validaciones se realizan **sin excepciones** (try-except)
- La **búsqueda de países es case-insensitive** (mayúsculas/minúsculas)
- El programa incluye **10 países iniciales** de ejemplo

---

## 🎓 Conclusiones del Proyecto

Este trabajo permitió consolidar conocimientos fundamentales de programación, especialmente en:

- Estructuras de datos y su aplicación práctica
- Modularización y diseño de funciones
- Manejo robusto de entradas de usuario
- Persistencia de datos en archivos
- Trabajo colaborativo en equipo

---

🎥 Video del Proyecto

Mirá la presentación completa del sistema en YouTube:

➡️ https://youtu.be/x_wAbWeC0cc

---

## 📧 Contacto

Para preguntas o sugerencias sobre el proyecto, contactar a los integrantes del equipo.

---

**Última actualización**: Noviembre 2025  
**Estado**: Completado ✅  
**Calificación esperada**: Proyecto integral con todas las funcionalidades requeridas
