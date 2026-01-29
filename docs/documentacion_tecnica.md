# 📘 Documentación Técnica  
**Sistema de Gestión de Datos – Python**  
ABP 2 | Módulo 3 – Desarrollo con Python

---

## 1. Introducción

Este documento describe la **arquitectura técnica**, las **estructuras de datos** y las **decisiones de diseño** del proyecto *Sistema de Gestión de Datos*, desarrollado en Python como parte del Módulo 3.

El objetivo de esta documentación es explicar **cómo está construido el sistema**, cómo interactúan sus componentes y qué criterios técnicos se aplicaron durante su desarrollo.

---

## 2. Arquitectura General del Sistema

El sistema está diseñado bajo una **arquitectura modular**, separando claramente las responsabilidades de cada componente.

La aplicación se ejecuta en consola y se organiza en las siguientes capas lógicas:

- **Menús (`menus/`)**: Controlan la navegación y la interacción con el usuario.
- **Servicios (`servicios/`)**: Contienen la lógica de negocio del sistema.
- **Datos (`data/`)**: Simulan el almacenamiento de información en memoria.
- **Utilidades (`utils/`)**: Centralizan validaciones y funciones reutilizables.
- **Pruebas (`tests/`)**: Ejecutan validaciones manuales automatizadas.
- **Punto de entrada (`main.py`)**: Orquesta la ejecución general del sistema.

Este enfoque permite un código más ordenado, mantenible y fácil de extender.

---

## 3. Flujo General de Ejecución

1. El sistema inicia desde `main.py`.
2. Se despliega el **menú principal**.
3. El usuario selecciona un módulo.
4. El menú correspondiente invoca funciones del módulo de servicios.
5. Los servicios interactúan con los datos almacenados en memoria.
6. El sistema retorna resultados al usuario mediante la consola.
7. El flujo continúa hasta que el usuario decide salir.

---

## 4. Descripción de Módulos

### 4.1 Menús (`menus/`)

Cada menú se implementa como una función que utiliza un **diccionario de opciones**, donde:
- La clave representa la opción ingresada por el usuario.
- El valor asocia la descripción y la función a ejecutar.

Este diseño permite:
- Reducir el uso de condicionales extensos.
- Facilitar la extensión de opciones.
- Mantener una navegación clara y controlada.

Los menús incluyen manejo de errores mediante bloques `try / except`.

---

### 4.2 Servicios (`servicios/`)

Los servicios contienen la **lógica de negocio** del sistema.

#### Inventario
- Gestión de productos.
- Control de stock.
- Activación y desactivación lógica.
- Validaciones de existencia y estado.

#### Clientes
- Registro y modificación de clientes.
- Activación y desactivación.
- Validación de datos ingresados.

#### Ventas
- Creación de ventas mediante carrito de compras.
- Reserva y liberación de stock.
- Edición y eliminación de items del carrito.
- Confirmación y anulación de ventas.
- Uso de funciones internas para encapsular el flujo del carrito.

#### Reportes
- Resúmenes del inventario.
- Reportes de ventas.
- Rankings de productos y clientes.
- Uso de estructuras auxiliares para acumulación de datos.

---

## 5. Estructuras de Datos Utilizadas

### 5.1 Listas (`list`)
Utilizadas para almacenar:
- Productos
- Clientes
- Ventas
- Items del carrito

Permiten recorrer y modificar dinámicamente los datos.

---

### 5.2 Diccionarios (`dict`)
Utilizados para:
- Representar entidades (producto, cliente, venta).
- Asociar opciones de menú con funciones.
- Almacenar acumuladores en reportes.

---

### 5.3 Conjuntos (`set`)
Utilizados para:
- Garantizar unicidad en la generación de identificadores.
- Evitar duplicados en reportes.

---

### 5.4 Tuplas (`tuple`)
Utilizadas de forma implícita:
- En retornos múltiples de funciones.
- En estructuras inmutables de apoyo.

---

## 6. Carrito de Compras y Gestión de Stock

El módulo de ventas implementa un **carrito de compras** que funciona como una estructura temporal.

Características principales:
- Reserva de stock al agregar productos.
- Ajuste dinámico de stock al editar cantidades.
- Devolución de stock al eliminar items.
- Restauración completa al cancelar una venta.
- Confirmación final mantiene el stock reservado.

Este enfoque asegura **consistencia de datos** durante todo el flujo de ventas.

---

## 7. Validaciones y Manejo de Errores

### 7.1 Validaciones
- Validación de entradas numéricas.
- Control de valores mínimos.
- Verificación de existencia de entidades.
- Restricción de operaciones sobre registros inactivos.
- Prevención de ventas sin stock.

Las validaciones se centralizan en `utils/validaciones.py`.

---

### 7.2 Manejo de Errores
- Uso de `try / except` en menús.
- Mensajes de error controlados.
- Continuidad del sistema ante errores no críticos.

---

## 8. Recursividad

El sistema utiliza **funciones recursivas** en el módulo de ventas para:
- Calcular el total de una venta.
- Contar unidades en el carrito.

La recursividad se implementa de forma simple y didáctica, alineada con los contenidos del módulo.

---

## 9. Pruebas Manuales

Las pruebas se encuentran en `tests/pruebas_manual.py`.

Características:
- Simulación de entradas de usuario.
- Ejecución completa de todos los módulos.
- Validación de flujos críticos.
- Restauración del estado inicial de los datos.

Las pruebas permiten verificar el correcto funcionamiento del sistema de forma repetible.

---

## 10. Consideraciones Finales

El sistema fue diseñado priorizando:
- Claridad del código.
- Separación de responsabilidades.
- Robustez en el manejo de datos.
- Adecuación al nivel académico del módulo.

La arquitectura implementada permite futuras extensiones sin necesidad de reestructurar el sistema completo.

---
