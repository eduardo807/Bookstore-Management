# Módulo de Librería para Odoo

Este módulo proporciona funcionalidades para gestionar una librería dentro de Odoo, incluyendo la gestión de inventario de libros, autores, clientes, y un dashboard.

## Características

- **Gestión de Libros**: Añadir, editar y gestionar libros, incluyendo información como título, autor, fecha de publicación, ISBN, precio y cantidad en stock.
- **Gestión de Autores**: Añadir y editar detalles de autores, como nombre y biografía.
- **Gestión de Clientes**: Seguimiento de clientes, incluyendo detalles de contacto y historial de compras.
- **Gestión de Inventario**: Actualización automática de los niveles de existencias en caso de venta o devolución.
- **Dashboard**: Visualización de niveles de stock y ventas recientes.

## Requisitos

- Odoo 17.

## Instalación

1. Clona el repositorio del módulo en tu directorio de addons de Odoo:

   git clone <URL_del_repositorio> <ruta_a_tu_directorio_de_addons>

2. Reinicia el servidor de Odoo para que el módulo sea detectado

3. Navega a Aplicaciones en Odoo y busca "Bookstore Management". Haz clic en Instalar.

## Configuración

1. Configuración de Productos como Libros:

Accede a Inventario > Productos.
Edita o crea un nuevo producto y selecciona la casilla Is Book para marcar el producto como un libro.

2. Gestión de Autores:

Navega a Bookstore > Authors.
Aquí puedes crear y gestionar autores, añadiendo detalles como nombre y biografía.

3. Gestión de Clientes:

Navega a Bookstore > Customers.
Añade nuevos clientes o edita los existentes para gestionar detalles de contacto y seguimiento de compras.

## Uso

### Añadir un Nuevo Libro

1. Ve a Bookstore > Books.

2. Haz clic en Crear y completa los detalles del libro, como título, autor, fecha de publicación, ISBN, precio y cantidad en stock.

3. Guarda el registro para añadir el libro al inventario.

### Actualización Automática de Inventario

- **Cada vez que se realiza una venta o devolución de un libro, el módulo actualizará automáticamente los niveles de stock para reflejar los cambios.**

### Acceder al Dashboard

1. Ve a Bookstore

2. El dashboard mostrará niveles de stock actuales y ventas recientes, y podras filtar los productos marcados como libros.

## Seguridad

El módulo define diferentes grupos de acceso para gestionar la seguridad:

- **Gestores de Ventas**: Acceso a la gestión de ventas y clientes.
- **Gestores de Inventario**: Acceso a la gestión de inventario y productos.

Asegúrate de asignar los roles correctos a los usuarios en Configuración > Usuarios y Empresas > Usuarios.
