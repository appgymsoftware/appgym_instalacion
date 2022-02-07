# ===========================
# Importamos paquetes basicos
# ===========================
import os
import sys
import traceback
from datetime import datetime as dt

# ==========================
# Importamos paquetes de gui
# ==========================
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb

# ====================================
# Importamos paquetes para la conexión
# ====================================
import pyrebase



# =========================================
# Preparamos las rutas de trabajo de la app
# =========================================

print("Welcome to App Gym Updater")
APP_ABS_PATH = os.getcwd()
print("Working dir:", APP_ABS_PATH)

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_UI = os.path.join(PROJECT_PATH, "probando.ui")

# os.chdir(PROJECT_PATH)
PROJECT_PATH = APP_ABS_PATH


# =====================================
# Bucle principal que lanza toda la app
# =====================================

if __name__ == '__main__':
    # Creo el appManager que tiene todas las configuraciones
    # mb.showinfo("Path",PROJECT_PATH)

    try:
        pass
        # My main code

        
    except Exception as err:

        try:
            exc_info = sys.exc_info()

            # do you usefull stuff here
            # (potentially raising an exception)
            # try:
            #     raise TypeError("Again !?!")
            # except:
            #     pass
            # end of useful stuff
            pass
        finally:
            # Display the *original* exception
            # traceback.print_exception(*exc_info)
            tracebackText = traceback.format_exc()
            print("Error: ",tracebackText)
            with open("tmp/mylogs.log","a") as logf:
                logText = f"ERROR {dt.now()}\n{tracebackText}================= END_ERROR =================\n"
                logf.write(logText)
            del exc_info
    exit()