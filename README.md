# Guía de Instalación de App GYM
En este repositorio está lo que descargo en la compu para hacer la instalación.

Debe haber:

- [ ] Entorno virtual con versión de Python.
- [ ] Instalar SQLite3.
- [ ] Instalar mi paquete.
- [ ] Ejecutar el programa.

---

# Entornos Virtuales
Configuración y uso de entornos virtuales

## 1. Instalar "virtualenv" con pip.
    pip install virtualenv

## 2. Comando para crear el entorno virtual.
    virtualenv venv

## 3. Solucionar problema "SecurityError: PSSecurityException"
    Set-ExecutionPolicy Unrestricted -Force

## 4. Activamos el entorno virtual
Este comando si funcionó

    ./venv/Scripts/activate
    /venv/Scripts/activate.bat

o tambien probar estos 2

    ./venv/Scripts/Activate.ps1
    source venv/Scripts/activate

## 6. Ejecutar la aplicación
    python main.py

## 5. Para salir del entorno
    ./venv/Scripts/deactivate
    deactivate