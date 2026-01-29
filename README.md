> Proyecto académico desarrollado como parte del Módulo 3 – Desarrollo con Python.

# 🗂️ Sistema de Gestión de Datos – Python

## 📌 Descripción del Proyecto

Este proyecto corresponde a la **Actividad Basada en Proyectos (ABP 2) – Módulo 3: Desarrollo con Python**, y consiste en el desarrollo de un **sistema de gestión de datos en consola**, orientado a la administración de **inventario, clientes y ventas**, utilizando Python y aplicando buenas prácticas de programación a nivel estudiante.

La aplicación funciona mediante un **menú principal interactivo**, desde el cual el usuario puede acceder a distintos módulos del sistema. Cada módulo está implementado de forma **modular y desacoplada**, permitiendo una navegación clara, controlada y segura entre las distintas funcionalidades.

El proyecto prioriza:
- Código limpio y legible
- Uso correcto de estructuras de control
- Modularización del código
- Manejo adecuado de datos
- Cumplimiento de estándares básicos de estilo (PEP 8)

Todo el sistema se ejecuta en entorno de **línea de comandos (CLI)** y simula un caso real de gestión administrativa.

---

## 🎯 Objetivo

El objetivo de este proyecto es desarrollar un sistema en Python que permita:

- Capturar y mostrar información ingresada por el usuario.
- Administrar datos utilizando estructuras como listas, diccionarios, tuplas y conjuntos.
- Implementar lógica de negocio mediante condicionales y bucles.
- Modularizar el código mediante funciones y archivos separados.
- Gestionar el flujo del sistema a través de menús interactivos.
- Validar entradas para evitar errores en la ejecución del programa.

El sistema busca demostrar la correcta aplicación de los contenidos del módulo, ofreciendo una solución funcional, estructurada y mantenible para la gestión de datos en un contexto simulado.

---

## 📁 Estructura del Proyecto

El proyecto está organizado de forma modular, separando claramente las responsabilidades de cada componente del sistema. La estructura de carpetas permite una fácil lectura, mantenimiento y escalabilidad del código.

```plaintext
📦 proyecto-gestion-datos/
│
├── main.py                     # Punto de entrada del sistema
│
├── menus/                      # Menús de navegación del sistema
│   ├── menu_principal.py       # Menú principal
│   ├── menu_inventario.py      # Menú del módulo Inventario
│   ├── menu_clientes.py        # Menú del módulo Clientes
│   ├── menu_ventas.py          # Menú del módulo Ventas
│   └── menu_reportes.py        # Menú del módulo Reportes
│
├── servicios/                  # Lógica de negocio del sistema
│   ├── inventario_service.py   # Gestión de productos y stock
│   ├── clientes_service.py     # Gestión de clientes
│   ├── ventas_service.py       # Gestión de ventas
│   └── reportes_service.py     # Generación de reportes
│
├── data/                       # Almacenamiento de datos (simulados)
│   ├── inventario.py           # Datos de productos
│   ├── clientes.py             # Datos de clientes
│   └── ventas.py               # Datos de ventas
│
├── utils/                      # Funciones utilitarias y validaciones
│   └── validaciones.py         # Validación de entradas y utilidades comunes
│
├── reportes/                   # Archivos de salida / reportes generados
│
├── tests/                      # Pruebas del sistema
│
├── docs/                       # Documentación adicional
│
└── README.md                   # Documentación principal del proyecto

...
```

Esta estructura permite una navegación clara del sistema y refuerza el principio de **separación de responsabilidades**, manteniendo el código ordenado y fácil de entender.

---

## ⚙️ Módulos y Funcionalidades

El sistema está organizado en módulos independientes, accesibles desde un menú principal. Cada módulo encapsula su propia lógica de negocio, favoreciendo la reutilización del código y una correcta separación de responsabilidades.

### 🧭 Menú Principal

El menú principal es el punto de entrada del sistema y permite al usuario navegar entre los distintos módulos disponibles.

Funcionalidades:
- Acceso al módulo de Inventario.
- Acceso al módulo de Clientes.
- Acceso al módulo de Ventas.
- Acceso al módulo de Reportes.
- Salida segura del sistema.

La navegación se implementa mediante un diccionario de opciones que asocia cada alternativa a una función específica, facilitando la extensibilidad del sistema.

### 📦 Módulo Inventario

Este módulo permite la gestión completa del inventario de productos.

Funcionalidades:
- Listar productos disponibles.
- Agregar nuevos productos al sistema.
- Actualizar el stock de productos existentes.
- Activar y desactivar productos.

Los productos se gestionan utilizando estructuras de datos como listas y diccionarios, permitiendo almacenar atributos como nombre, categoría, stock y estado.

### 👥 Módulo Clientes

El módulo de clientes administra la información de los clientes registrados en el sistema.

Funcionalidades:
- Listar clientes.
- Registrar nuevos clientes.
- Modificar datos de clientes existentes.
- Activar y desactivar clientes.

La información de los clientes se maneja mediante listas y diccionarios, asegurando una estructura clara y un acceso eficiente a los datos.

### 💰 Módulo Ventas

Este módulo gestiona las operaciones de venta realizadas en el sistema, integrando clientes y productos del inventario.

Funcionalidades:
- Crear una nueva venta.
- Listar todas las ventas registradas.
- Visualizar el detalle de una venta específica.
- Anular una venta existente.

Las ventas se almacenan utilizando estructuras de datos como listas y diccionarios, permitiendo registrar información como productos vendidos, cliente asociado, monto total y estado de la venta.

Este módulo implementa internamente un flujo de venta basado en un carrito de compras, el cual se detalla en una sección posterior del documento.

### 📊 Módulo Reportes

El módulo de reportes permite analizar la información del sistema mediante distintos resúmenes y rankings.

Funcionalidades:
- Resumen general del inventario.
- Inventario agrupado por categoría.
- Resumen de ventas realizadas.
- Top de productos más vendidos.
- Top de clientes según monto de compras.
- Reporte de clientes activos e inactivos.

Este módulo utiliza estructuras de datos como listas, diccionarios y conjuntos (set) para procesar información sin duplicados y generar estadísticas relevantes para la toma de decisiones.

---

## 🛒 Flujo de Venta y Carrito de Compras

Este sistema implementa un **flujo de venta basado en un carrito de compras**, que permite gestionar de forma controlada la selección de productos, validación de stock y confirmación final de la venta.

El carrito funciona como una estructura temporal que **reserva stock del inventario** mientras la venta está en proceso, asegurando consistencia de datos y evitando sobreventa de productos.

### 🔁 Flujo General de una Venta

El proceso de venta sigue las siguientes etapas:

1. Selección de un cliente activo desde el módulo de clientes.
2. Creación de un carrito de compras vacío asociado a la venta.
3. Agregado de productos al carrito con validación de stock disponible.
4. Reserva de stock en tiempo real al agregar productos al carrito.
5. Visualización y edición del contenido del carrito.
6. Confirmación o cancelación de la venta.
7. Registro final de la venta o devolución del stock reservado.

### 🧺 Estructura del Carrito de Compras

El carrito de compras se implementa como una **lista de diccionarios**, donde cada elemento representa un producto agregado a la venta.

Cada item del carrito contiene la siguiente información:
- ID del producto
- Nombre del producto
- Precio unitario
- Cantidad seleccionada
- Subtotal calculado

Esta estructura permite recorrer, modificar y calcular fácilmente el total de la venta.

### 📦 Gestión de Stock y Reservas

El sistema implementa un mecanismo de **reserva de stock** durante el proceso de venta:

- Al agregar un producto al carrito, el stock se descuenta inmediatamente del inventario.
- Si se edita la cantidad de un producto, el stock se ajusta según la diferencia.
- Si se elimina un item del carrito, el stock reservado se devuelve al inventario.
- Si la venta se cancela antes de confirmarse, todo el stock reservado es restaurado.
- Solo al confirmar la venta, el stock queda definitivamente descontado.

### ✅ Confirmación y Registro de la Venta

Al finalizar el proceso, el sistema solicita confirmación al usuario:

- Si la venta es confirmada, se genera un identificador único y se registra la venta con su detalle completo.
- Si la venta no es confirmada, el carrito se limpia y el stock reservado se devuelve al inventario.

Las ventas se almacenan con información del cliente, los productos vendidos, el total de la operación y su estado (activa o anulada).

### ❌ Anulación de Ventas

El sistema permite realizar una **anulación lógica de ventas** ya registradas.

Al anular una venta:
- El estado de la venta cambia a inactiva.
- El stock de los productos asociados es devuelto al inventario.
- La venta se mantiene registrada para efectos de consulta y reportes.

---

## 🔍 Supuestos, Alcance y Restricciones

Para el desarrollo del sistema se definieron los siguientes supuestos y criterios de diseño, con el objetivo de simplificar la implementación y enfocarse en los conceptos clave del módulo:

- El sistema funciona en **memoria**, utilizando estructuras de datos de Python (listas, diccionarios, conjuntos), sin persistencia en bases de datos.
- Los datos iniciales de productos, clientes y ventas se cargan desde archivos del módulo `data/`.
- Cada producto, cliente y venta posee un **identificador único**.
- Los estados de productos, clientes y ventas se gestionan mediante **activación y desactivación lógica**, evitando eliminaciones físicas.
- El sistema asume un **único usuario** operando la aplicación en consola.
- No se consideran permisos ni roles de usuario.
- La validación de entradas se realiza de forma preventiva para evitar errores de ejecución.
- El stock de productos se controla estrictamente durante el proceso de venta, mediante reservas temporales.
- El sistema prioriza **claridad, legibilidad y modularización** por sobre optimizaciones avanzadas.

---

## 🧩 Decisiones de Diseño y Arquitectura

Durante el desarrollo del sistema se tomaron diversas decisiones de diseño con el fin de mantener una estructura clara, modular y fácil de mantener:

- Separación del sistema en **capas lógicas**:
  - Menús (`menus/`) para la navegación.
  - Servicios (`servicios/`) para la lógica de negocio.
  - Datos (`data/`) para la simulación de almacenamiento.
  - Utilidades (`utils/`) para validaciones y funciones reutilizables.
- Uso de **diccionarios de opciones** para construir menús dinámicos y extensibles.
- Implementación de **funciones pequeñas y específicas**, siguiendo el principio de responsabilidad única.
- Uso de **estructuras de control claras** (if, while, for) para garantizar un flujo predecible.
- Manejo explícito del flujo de ventas mediante un **carrito de compras**, con reserva y devolución de stock.
- Preferencia por claridad y legibilidad del código por sobre optimizaciones prematuras.

Estas decisiones permiten que el sistema sea fácil de comprender, probar y extender, manteniendo un nivel adecuado al contexto académico del proyecto.

---

## 🛠️ Tecnologías y Conceptos Aplicados

El proyecto fue desarrollado utilizando **Python** como lenguaje principal, aplicando los conceptos fundamentales abordados en el Módulo 3 del bootcamp. A continuación, se detallan las tecnologías y principios utilizados:

### 🐍 Lenguaje de Programación

- **Python 3**
  - Desarrollo de una aplicación de consola (CLI).
  - Uso de sintaxis clara y legible, siguiendo las recomendaciones básicas de **PEP 8**.
  - Ejecución secuencial controlada mediante un punto de entrada (`main.py`).

### 🔁 Estructuras de Control

- Uso de **condicionales** (`if`, `elif`, `else`) para:
  - Validar estados (activo / inactivo).
  - Controlar flujos de navegación.
  - Confirmar acciones críticas (ventas, anulaciones).
- Uso de **bucles** (`while`, `for`) para:
  - Menús interactivos.
  - Recorridos de listas y diccionarios.
  - Procesamiento de colecciones de datos.
- Aplicación de **`break` y `continue`** para mejorar la legibilidad y control del flujo del programa.

### 🧩 Funciones

- Definición de **funciones personalizadas** para encapsular lógica específica.
- Uso de **parámetros** y **valores de retorno** (`return`) para comunicación entre funciones.
- Implementación de **funciones anidadas** dentro del módulo de ventas para manejar el flujo del carrito.
- Uso de **funciones recursivas**, como:
  - Cálculo del total de una venta mediante acumulación recursiva de subtotales.

### 🗃️ Estructuras de Datos

- **Listas (`list`)**
  - Almacenamiento de productos, clientes, ventas e items del carrito.
- **Diccionarios (`dict`)**
  - Representación estructurada de entidades (producto, cliente, venta).
  - Asociación de opciones de menú con funciones ejecutables.
- **Conjuntos (`set`)**
  - Garantizar unicidad de identificadores, como en la generación de IDs de ventas.
- **Tuplas (`tuple`)**
  - Uso implícito en retornos múltiples y estructuras inmutables (cuando aplica).

### 🧱 Modularización

- Separación del sistema en **módulos independientes**:
  - `menus/`: navegación del sistema.
  - `servicios/`: lógica de negocio.
  - `data/`: datos simulados en memoria.
  - `utils/`: validaciones reutilizables.
- Uso de **imports explícitos** para reutilizar funciones entre módulos.
- Organización del código en archivos `.py` con responsabilidades bien definidas.

### 💻 Entrada y Salida de Datos (I/O)

- Captura de datos mediante `input()`.
- Visualización de información con `print()` y **f-strings** para formateo claro de salidas.
- Interacción continua con el usuario a través de menús en consola.

Este conjunto de tecnologías y conceptos permite construir un sistema funcional, coherente y alineado con los objetivos de aprendizaje del módulo, manteniendo un enfoque académico pero realista.

---

## ✅ Validaciones y Manejo de Errores

Para asegurar el correcto funcionamiento del sistema y evitar errores durante la ejecución, se implementaron distintos mecanismos de validación y control de errores en toda la aplicación.

### 🧩 Validación de Entradas del Usuario
- Se valida que las entradas numéricas correspondan a valores enteros válidos.
- Se controla que los valores ingresados sean mayores a cero cuando la lógica del negocio lo requiere (por ejemplo, cantidades y stock).
- Se evita la selección de opciones inexistentes en los menús.
- Se valida la existencia de entidades antes de operar sobre ellas (productos, clientes, ventas).

Estas validaciones permiten prevenir errores comunes como:
- Ingreso de texto cuando se espera un número.
- Selección de IDs inexistentes.
- Operaciones inválidas sobre registros inactivos.

### 🛠️ Funciones de Validación Centralizadas
- Las validaciones se encuentran encapsuladas en el módulo `utils/validaciones.py`.
- Se reutilizan funciones como:
  - Validación de números enteros.
  - Formateo de valores monetarios en pesos chilenos (CLP).
- Este enfoque mejora la legibilidad y evita la duplicación de lógica.

### 🧯 Manejo de Errores con try / except
- Se utilizan bloques `try / except` en los menús para capturar errores inesperados.
- En caso de excepción:
  - El sistema informa al usuario que ocurrió un error.
  - Se muestra un mensaje técnico controlado para facilitar la depuración durante el desarrollo.
- El programa continúa en ejecución sin interrumpirse abruptamente.

### 🔄 Control de Flujo Seguro
- El sistema impide acciones inválidas, como:
  - Generar ventas con clientes inactivos.
  - Vender productos sin stock disponible.
  - Finalizar ventas con un carrito vacío.
  - No se permite agregar al carrito cantidades superiores al stock disponible.
- En el módulo de ventas, se implementa la **reserva y devolución de stock**, asegurando la consistencia de los datos incluso cuando una venta se cancela.

Este enfoque garantiza una experiencia de usuario controlada, previene estados inconsistentes en los datos y refuerza la robustez general del sistema.

---

## 🚀 Cómo Ejecutar el Proyecto

El sistema se ejecuta completamente desde la **línea de comandos (CLI)** y no requiere dependencias externas ni configuraciones adicionales.

### 📋 Requisitos Previos
- Tener **Python 3.8 o superior** instalado.
- Acceso a una terminal o consola (CMD, PowerShell, Terminal, etc.).

### ▶️ Pasos para Ejecutar

1. Clonar el repositorio o descargar el proyecto.
2. Acceder al directorio del proyecto.
3. Ejecutar el archivo principal.

```powershell
git clone https://github.com/marechek/Sistema_Gestion.git
cd Sistema_Gestion
python main.py
```

4. El sistema mostrará el menú principal, desde donde podrás navegar por los distintos módulos:
    - Inventario
    - Clientes
    - Ventas
    - Reportes

### 🧭 Uso General del Sistema

La navegación se realiza ingresando el número de la opción deseada.
El sistema valida cada entrada antes de continuar.
En cualquier menú, es posible volver al menú anterior o salir del sistema de forma segura.

### 🔁 Persistencia de Datos

Los datos se almacenan en memoria utilizando estructuras como listas y diccionarios.
Al reiniciar el programa, los datos vuelven a su estado inicial.
Este comportamiento es intencional y forma parte del alcance del proyecto académico.

---

## 🧪 Evidencia de Pruebas Manuales

A continuación se presentan capturas de pruebas manuales realizadas en la terminal, que evidencian el correcto funcionamiento de los principales módulos del sistema.
Las capturas completas de las pruebas manuales se encuentran organizadas en el directorio `docs/capturas/`.

### 📦 Módulo Inventario
Prueba de listado y registro de productos desde el menú de inventario.
![Inventario](docs/capturas/1_INVENTARIO_1_Listar_y_Agregar_Producto.png)

### 👥 Módulo Clientes
Registro y visualización de clientes, junto con validaciones de estado.
![Clientes](docs/capturas/2_CLIENTES_1_Listar_y_Registrar_cliente.png)

### 🛒 Módulo Ventas – Carrito de Compras
Flujo de creación de una venta utilizando el carrito de compras, incluyendo reserva de stock y cálculo de totales.
![Ventas](docs/capturas/3_VENTAS_2_2_Crear_ventas_Carrito.png)

> Debido a la extensión del flujo de ventas, la prueba completa del carrito se documenta en múltiples capturas disponibles en el directorio `docs/capturas/`.

### 📊 Módulo Reportes
Generación de distintos reportes consolidados desde el sistema.
![Reportes](docs/capturas/4_REPORTES_1_Varios.png)

Las capturas adicionales de pruebas (edición, anulación de ventas, activación/desactivación de entidades, validaciones y reportes adicionales) se encuentran organizadas en el directorio `docs/capturas/`.

---

## 📘 Documentación Técnica

La documentación técnica detallada del sistema, incluyendo arquitectura, estructuras de datos, decisiones de diseño y pruebas, se encuentra disponible en:

`docs/documentacion_tecnica.md`

---

## 🧪 Informe de Validación

El informe de validación documenta las pruebas realizadas sobre el sistema, incluyendo casos de prueba, resultados y evidencias gráficas del funcionamiento de los distintos módulos.  
Este documento se encuentra disponible en:

`docs/informe_validacion.md`

---

## 🏁 Conclusiones Finales

El desarrollo de este sistema de gestión de datos permitió aplicar de forma práctica los principales conceptos abordados en el Módulo 3: Desarrollo con Python, integrándolos en una solución funcional y coherente.

A través de este proyecto se logró:

- Aplicar estructuras de datos fundamentales de Python (listas, diccionarios y conjuntos) para modelar información real de un sistema administrativo.
- Diseñar un sistema modular y desacoplado, separando menús, lógica de negocio, validaciones y datos, lo que mejora la legibilidad y el mantenimiento del código.
- Implementar menús interactivos en consola, controlando el flujo del programa de manera segura y clara para el usuario.
- Desarrollar reglas de negocio consistentes, especialmente en el módulo de ventas, asegurando el control de stock y la integridad de los datos.
- Incorporar validaciones preventivas y manejo básico de errores para evitar fallos en la ejecución y mejorar la experiencia de uso.
- Priorizar la claridad y comprensión del código por sobre optimizaciones avanzadas, acorde al nivel y objetivos del módulo.

En conclusión, el proyecto cumple con los objetivos planteados, demostrando una correcta aplicación de los contenidos vistos en el módulo y sentando una base sólida para futuras mejoras, como la incorporación de persistencia de datos, interfaces gráficas o bases de datos.

---

## 🔄 Control de Versiones

El proyecto fue versionado utilizando **Git** como sistema de control de versiones y **GitHub** como repositorio remoto.

Durante el desarrollo se utilizó una estrategia basada en **ramas**, lo que permitió trabajar de forma ordenada y controlada sobre cada módulo del sistema. Cada funcionalidad principal fue desarrollada en su propia rama y posteriormente integrada a la rama principal (`master`) mediante merges controlados.

Principales prácticas aplicadas:
- Uso de la rama `master` como rama estable del proyecto.
- Creación de ramas específicas para el desarrollo de funcionalidades (por ejemplo, módulo de ventas).
- Commits frecuentes y descriptivos.
- Integración final de funcionalidades mediante merge controlado.
- Respaldo permanente del proyecto en GitHub.

Este enfoque permitió mantener un historial claro de cambios, facilitar la detección de errores y asegurar la estabilidad del proyecto en cada etapa de desarrollo.

---

## 👤 Autor

Proyecto académico desarrollado como parte del **Módulo 3 – Desarrollo con Python**, en el marco de la **Actividad Basada en Proyectos (ABP 2)**.

El proyecto fue diseñado, desarrollado, probado y documentado íntegramente por **Marcos Elias**, aplicando los contenidos y buenas prácticas abordadas durante el módulo.

---

## 🔮 Posibles Mejoras Futuras

Si bien el sistema cumple con los objetivos definidos para el módulo, existen múltiples mejoras que podrían implementarse en una versión futura para aumentar su robustez, escalabilidad y usabilidad:

- Persistencia de datos
Incorporar almacenamiento permanente mediante archivos (CSV/JSON) o una base de datos relacional (por ejemplo, SQLite), evitando la pérdida de información al reiniciar el sistema.

- Gestión de usuarios y roles
Implementar autenticación y distintos niveles de permisos (administrador, vendedor, consulta), permitiendo un uso más cercano a un sistema real.

- Mayor cobertura de pruebas
Ampliar el módulo tests/ con pruebas unitarias automatizadas para validar la lógica de negocio y reducir errores en futuras modificaciones.

- Mejoras en reportes
Exportar reportes a formatos externos (CSV, PDF) y agregar nuevos indicadores de análisis, como tendencias de ventas o rotación de inventario.

- Optimización de estructuras de datos
Evaluar el uso de clases y programación orientada a objetos para modelar entidades como productos, clientes y ventas de forma más estructurada.

- Manejo avanzado de errores y logging
Incorporar un sistema de registro de eventos (logging) para facilitar la auditoría y depuración del sistema.

Estas mejoras permitirían evolucionar el proyecto desde un sistema académico hacia una solución más cercana a un entorno productivo, manteniendo la base modular y estructurada desarrollada en esta versión.

