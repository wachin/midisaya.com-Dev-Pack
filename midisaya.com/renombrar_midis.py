import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import markdownify
from pathlib import Path

# Función para limpiar nombres de archivos
def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', name)

# Función para parsear el archivo markdown y obtener los datos
def extraer_datos_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Buscar línea de inicio de tabla (la que tiene "| MIDI | TITLE |...")
    table_started = False
    data = []

    for line in lines:
        if not table_started and line.strip().startswith('| MIDI |'):
            table_started = True
            continue
        if table_started and line.strip().startswith('|---'):
            continue
        if table_started and '|' in line:
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 5:
                midi_num = parts[0]
                title = parts[1]
                author = parts[2]
                sequencer = parts[3]
                style = parts[4].strip()
                data.append({
                    "numero": midi_num,
                    "titulo": title,
                    "autor": author,
                    "secuenciador": sequencer,
                    "estilo": style
                })
        elif table_started:
            # Fin de la tabla
            break

    return data

# Función principal que renombra los archivos
def renombrar_archivos_midi(directorio, tabla_datos):
    tabla_dict = {item['numero']: item for item in tabla_datos}
    archivos = [f for f in os.listdir(directorio) if f.lower().endswith('.mid')]
    cambios = []

    for archivo in archivos:
        base = Path(archivo).stem
        ext = ".mid"  # Extensión final siempre minúscula
        match = re.match(r'^(\d+)(M?)\.MID$', archivo, re.IGNORECASE)
        if not match:
            continue
        numero = match.group(1)
        m = match.group(2)

        if numero not in tabla_dict:
            print(f"No hay datos para el número {numero}")
            continue

        fila = tabla_dict[numero]
        titulo = sanitize_filename(fila["titulo"])
        autor = sanitize_filename(fila["autor"])
        secuenciador = sanitize_filename(fila["secuenciador"])
        estilo = sanitize_filename(fila["estilo"])

        nuevo_nombre = f"{numero}{m} {titulo} - {autor} (MIDI {secuenciador})({estilo}){ext}"
        nuevo_nombre = nuevo_nombre.replace("()", "").replace("( )", "").strip()
        cambios.append((archivo, nuevo_nombre))

    # Confirmar e imprimir resultados antes de renombrar
    confirmacion = "\n".join([f"{a} -> {b}" for a, b in cambios[:20]])
    if len(cambios) > 20:
        confirmacion += "\n... y otros archivos."

    confirmar = messagebox.askyesno("Confirmación", f"¿Realmente quieres renombrar estos archivos?\n\n{confirmacion}")
    if confirmar:
        for original, nuevo in cambios:
            ruta_original = os.path.join(directorio, original)
            ruta_nuevo = os.path.join(directorio, nuevo)
            try:
                os.rename(ruta_original, ruta_nuevo)
            except Exception as e:
                print(f"Error al renombrar {original}: {e}")
        messagebox.showinfo("Éxito", "Los archivos han sido renombrados correctamente.")
    else:
        messagebox.showinfo("Cancelado", "No se ha realizado ningún cambio.")

# Función para seleccionar carpeta
def seleccionar_carpeta():
    directorio = filedialog.askdirectory(title="Selecciona la carpeta con archivos MIDI")
    if directorio:
        tabla_path = os.path.join(os.path.dirname(directorio), "midisaya-tabla.md")
        if not os.path.isfile(tabla_path):
            tabla_path = filedialog.askopenfilename(title="Selecciona el archivo midisaya-tabla.md",
                                                    filetypes=[("Markdown files", "*.md")])
        if os.path.isfile(tabla_path):
            datos = extraer_datos_markdown(tabla_path)
            renombrar_archivos_midi(directorio, datos)
        else:
            messagebox.showerror("Error", "Archivo midisaya-tabla.md no encontrado.")

# Crear interfaz gráfica
def main():
    root = tk.Tk()
    root.title("Renombrador de Archivos MIDI")
    root.geometry("400x200")

    label = tk.Label(root, text="Selecciona la carpeta donde están los archivos MIDI")
    label.pack(pady=20)

    boton = tk.Button(root, text="Seleccionar Carpeta", command=seleccionar_carpeta)
    boton.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
