# Inventario SPL — Práctica 4
Proyecto académico Django. Python 3.10 o superior. Solo desarrollo local.

## Windows / PowerShell
Descomprimir y abrir la carpeta que contiene manage.py en VS Code.
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
$env:PRODUCT_VARIANT="A"
python manage.py runserver
```
Abrir http://127.0.0.1:8000/ e iniciar sesión con el usuario creado.
Para B, detener con Ctrl+C y ejecutar:
```powershell
$env:PRODUCT_VARIANT="B"
python manage.py runserver
```
Las variantes comparten SQLite. Administración de usuarios y categorías completas en /admin/ con superusuario. Las alertas son internas, no correos. El reporte se descarga en PDF.

## Pruebas
```powershell
$env:PRODUCT_VARIANT="A"
python manage.py test
$env:PRODUCT_VARIANT="B"
python manage.py test
```
## Sesiones
1. Reutilizables: usuarios (auth Django), plantilla base, módulo de exportación (adaptando origen de datos). Específicos: modelos de inventario y alertas de stock. Arquitectura: usuario → URLs → vistas → modelos → SQLite; configuración → módulos opcionales.
2. Apps reportes y notificaciones independientes, registradas condicionalmente. Plantilla base oculta enlaces y URLconf no registra rutas desactivadas.
3. config/config_product.py define A (ambas banderas False) y B (ambas True). settings.py lee PRODUCT_VARIANT. Reiniciar servidor tras cambios.
4. Patrón: modularización por componentes y feature toggles; plantilla base usa herencia de plantillas. Para reutilizar una app, copiarla, registrar sus dependencias, adaptar interfaces y ejecutar pruebas.

## Evidencias a obtener realmente
Capturar dashboard A, dashboard B, PDF descargado, alertas, config_product.py y ejecución de pruebas. Elaborar manual PDF y diagramas; cada integrante debe escribir su conclusión y recomendación propias.
