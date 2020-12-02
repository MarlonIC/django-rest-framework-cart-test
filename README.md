* Crear ambiente virtual
> `python3 -m venv venv`

* Instalar dependencias
> `pip install -r requirements.txt`

* Posicionarse dentro del directorio mycart y ejecutar migraciones
> `cd mycart && python manage.py migrate`

NOTA: Considerar que se tenga una base de datos mysql configurado con las siguientes credenciales:
- Database: drf
- Usuario: root
- Password: root

Ejecutar las siguientes querys para las pruebas de apis:

> insert into services_category values(null, 'Categoria 1');
>
> insert into services_category values(null, 'Categoria 2');
>
> insert into services_product values(null, 'caramelo', 5, 1, 20.5);
>
> insert into services_product values(null, 'gaseosa', 2, 1, 13.5);
>
> insert into services_product values(null, 'galleta', 12, 1, 6.5);
>
> insert into services_cart values(null, 2, 1);
>
> insert into services_cart values(null, 3, 2);
>
> insert into services_order values(null, 'Nombre usuario', 'Apellido usuario', 'emailtest@gmail.com', 1);