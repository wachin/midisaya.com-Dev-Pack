import os
import re
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para extraer SOLO el nombre del autor del archivo
def extraer_autor(nombre_archivo):
    # Busca desde después del " - " hasta el primer "("
    match = re.search(r'-\s*([^()]+)', nombre_archivo)
    if match:
        return match.group(1).strip()
    else:
        print(f"No se pudo identificar el autor en: {nombre_archivo}")
        return None

# Función principal para organizar los archivos
def organizar_midis_por_autor(directorio):
    archivos = [f for f in os.listdir(directorio) if f.lower().endswith('.mid')]
    autores_dict = {}

    for archivo in archivos:
        ruta_original = os.path.join(directorio, archivo)

        autor = extraer_autor(archivo)
        if not autor:
            continue

        # Limpiar caracteres inválidos para nombres de carpetas
        autor_limpio = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', autor)

        # Crear carpeta si no existe
        carpeta_autor = os.path.join(directorio, autor_limpio)
        if not os.path.exists(carpeta_autor):
            os.makedirs(carpeta_autor)

        # Mover archivo
        ruta_destino = os.path.join(carpeta_autor, archivo)
        try:
            shutil.move(ruta_original, ruta_destino)
            autores_dict.setdefault(autor_limpio, []).append(archivo)
        except Exception as e:
            print(f"Error moviendo {archivo}: {e}")

    # Mostrar resumen
    resumen = "\n".join([f"{autor}: {len(files)} archivos" for autor, files in autores_dict.items()])
    messagebox.showinfo("Organización completada", f"Archivos organizados por autor:\n\n{resumen}")

# Función para seleccionar carpeta
def seleccionar_carpeta():
    directorio = filedialog.askdirectory(title="Selecciona la carpeta con archivos MIDI")
    if directorio:
        organizar_midis_por_autor(directorio)

# Interfaz gráfica
def main():
    root = tk.Tk()
    root.title("Organizador de MIDI por Autor")
    root.geometry("400x200")

    label = tk.Label(root, text="Selecciona la carpeta donde están los archivos MIDI")
    label.pack(pady=20)

    boton = tk.Button(root, text="Seleccionar Carpeta", command=seleccionar_carpeta)
    boton.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
