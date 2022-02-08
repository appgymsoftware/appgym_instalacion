# ===========================
# Importamos paquetes basicos
# ===========================
import os
import sys
import traceback
from datetime import datetime as dt
import json

# ==========================
# Importamos paquetes de gui
# ==========================
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb

# =========================================
# Preparamos las rutas de trabajo de la app
# =========================================

print("Welcome to App Gym Updater")
APP_MAIN_FOLDER_PATH = os.getcwd()
print("Working dir:", APP_MAIN_FOLDER_PATH)

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_UI = os.path.join(PROJECT_PATH, "probando.ui")

# os.chdir(PROJECT_PATH)
PROJECT_PATH = APP_MAIN_FOLDER_PATH


# =====================================
# Bucle principal que lanza toda la app
# =====================================

if __name__ == '__main__':
    # Creo el appManager que tiene todas las configuraciones
    mb.showinfo("Path",PROJECT_PATH)

    try:
        # My main code
        
        # ====================================
        # Importamos paquetes para la conexión
        # ====================================
        import pyrebase

        # Levantamos los json (si existen), sino los creamos y vamos a la pantalla de bienvenida
        try:
            # import appgym_package
            pass
        except:
            mb.showerror("Error Librería!","Por favor instale el paquete de la aplicación.")

        # Cargamos los json
        USR_CONFIG_PATH = PROJECT_PATH+"/user_configs.json"
        try:
            with open(USR_CONFIG_PATH,"r") as json_file:
                user_configs = json.load(json_file)
                print(user_configs)
        except:
            # Directly from dictionary
            with open(USR_CONFIG_PATH,"r") as output_json_file:
                user_configs = {
                    
                }
                json.dump(user_configs, output_json_file)

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
            mb.showerror("Error!",f"La aplicación se cerrará:\n\n{logText.replace('================= END_ERROR =================','')}")
    exit()