# Importamos paquetes basicos
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb

print("Welcome to App Gym Updater")
APP_ABS_PATH = os.getcwd()
print("Working dir:", APP_ABS_PATH)

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_UI = os.path.join(PROJECT_PATH, "probando.ui")

# os.chdir(PROJECT_PATH)
PROJECT_PATH = APP_ABS_PATH

if __name__ == '__main__':
    # Creo el appManager que tiene todas las configuraciones
    mb.showinfo("Path",PROJECT_PATH)
    
    exit()