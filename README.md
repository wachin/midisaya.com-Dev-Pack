# Tutorial: Reproducción y Edición de Secuencias MIDI de Alabanza y Adoración (MIDISAYA)

En este tutorial aprenderás a reproducir secuencias MIDI de Alabanza y Adoración (MIDISAYA). Además, podrás ajustar el tono, velocidad y seleccionar los instrumentos que deseas escuchar mientras reproduces un archivo MIDI.

## **¿De dónde provienen las secuencias MIDI?**
Las secuencias MIDI utilizadas en este tutorial provienen de **MIDISAYA**, creadas y compartidas originalmente por **Edgar A. Franco**. Antes, estas secuencias estaban disponibles en una página web, pero ahora pueden descargarse desde una publicación en el grupo de Facebook de Edgar A. Franco:  
[**Ver publicación en Facebook**](https://www.facebook.com/groups/midisaya/permalink/2873074299431938/).

He organizado estas secuencias en GitHub para facilitar su acceso y manejo:  

## Descarga
[**Secuencias MIDISAYA en GitHub**](https://github.com/wachin/midisaya.com-Dev-Pack/).

---
# Reproducción de MIDISAYA en Celular Android

## **Paso 1: Descarga e instala las herramientas necesarias**
### **1. App para reproducir MIDI: MIDI File Player**
Descarga la aplicación **MIDI File Player** desde la Google Play Store:  
[**Descargar MIDI File Player**](https://play.google.com/store/apps/details?id=net.volcanomobile.midifileplayer)

Esta aplicación te permite:  
- Leer archivos MIDI.  
- Cambiar la velocidad y el tono.  
- Filtrar canales para elegir qué instrumentos se reproducen.  
- Usar marcadores de bucle para practicar partes específicas.  
- Visualizar notas y tonalidades en tiempo real.  
- Activar un metrónomo para mayor precisión.  

### **2. Fuentes de sonido (SoundFonts)**
Para mejorar la calidad del sonido, necesitarás instalar **SoundFonts** (fuentes de sonido). Aquí tienes algunas opciones gratuitas:  
- [Fuentes de sonido gratis y cómo usarlas en Linux](https://facilitarelsoftwarelibre.blogspot.com/2023/06/fuentes-de-sonido-soundfonts-gratis-desde-varios-sitios.html)  
- [SoundFonts gratuitos desde paquetes de Ubuntu, Debian, Deepin Linux y TuxGuitar](https://facilitarelsoftwarelibre.blogspot.com/2019/11/fuentes-de-sonido-soundfonts-gratuitas.html)

---

## **Paso 2: Configura y utiliza las herramientas**
1. **Carga las secuencias MIDI**  
   Descarga los archivos desde el repositorio de GitHub:  
   [**Secuencias MIDISAYA en GitHub**](https://github.com/wachin/midisaya.com-Dev-Pack/).  
   Guarda las secuencias en tu celular.

2. **Abre MIDI File Player**  
   - Importa los archivos MIDI que descargaste.  
   - Selecciona el archivo MIDI que deseas reproducir.

3. **Ajusta el MIDI a tus necesidades**  
   - **Sube o baja el tono** según sea necesario para adaptarlo a tu voz o instrumento.  
   - **Filtra los canales** para silenciar instrumentos o destacar sonidos específicos.  
   - **Configura la velocidad** para practicar a tu ritmo.  
   - **Activa el bucle** para repetir una sección específica.

4. **Aplica un SoundFont**  
   Descarga e importa un SoundFont de alta calidad para mejorar el sonido. Configura el SoundFont en las opciones de la app.

---

## **¿Por qué usar este método?**
Este enfoque te permite personalizar y practicar las secuencias MIDI de Alabanza y Adoración según tus necesidades, ya sea para ensayos, presentaciones o devocionales. Además, aprovechas herramientas gratuitas y fácilmente accesibles.

---


# TUTORIALES QUE ME FALTAN POR HACER 

# Reproducción de MIDISAYA en WINDOWS

# Reproducción de MIDISAYA en LINUX


# Formación de los nombres de los archivos midi de midisaya.com
Scripts para crear los nombres de los archivos de midisaya.com

---

# 🧠 script renombrar_midis.py

## ✅ Objetivo:
El script se llama: **`renombrar_midis.py`** y su objetivo es renombrar archivos MIDI (.mid o .MID) en la carpeta:

/midisaya.com-Dev-Pack/midisaya.com/MIDIS/

usando como base la información del archivo Markdown (`.md`)

**"midisaya-tabla.md"**

/home/wachin/Dev/midisaya.com-Dev-Pack/midisaya.com/midisaya-tabla.md

que contiene una tabla con los datos de cada archivo MIDI.

Cada archivo MIDI es renombrado siguiendo este formato:

```
[Número][M] Título - Autor (MIDI Secuenciador)(Estilo).mid
```

Donde:
- `[Número]`: Número del MIDI según la tabla.
- `[M]`: Opcional, indica que tiene melodía (si existe tal archivo).
- `Título`: Nombre de la canción.
- `Autor`: Persona u organización que escribió/compuso la canción.
- `Secuenciador`: Persona que creó el archivo MIDI.
- `Estilo`: Género musical de la canción.
- La extensión final siempre será `.mid` en minúscula.

---

## 📁 Ejemplo

Dado un archivo llamado:
```
3M.MID
```

Y basándose en esta línea de la tabla:

| MIDI | TITLE                 | AUTHOR OR ARTIST           | SEQUENCER     | STYLE   |
|------|-----------------------|----------------------------|---------------|---------|
| 3    | A Dios sea la gloria  | Andrae Crouch (autor)      | Edgar Franco  | Balada  |

El script lo renombrará a:

```
3M A Dios sea la gloria - Andrae Crouch (autor) (MIDI Edgar Franco)(Balada).mid
```

---

## 🔍 Estructura del archivo Markdown

El archivo `midisaya-tabla.md` debe contener una tabla como esta:

```markdown
| MIDI | TITLE                  | AUTHOR OR ARTIST        | SEQUENCER     | STYLE       |
|------|------------------------|--------------------------|---------------|-------------|
| 1    | A Cristo Coronad       | Matthew Bridges & ...    | Edgar Franco  | Pop         |
| 2    | A Cristo solo a Cristo | Marcos Witt              | Edgar Franco  | Balada      |
| ...
```

Este archivo le dice al script cómo debe renombrarse cada archivo MIDI.

---

## 🐍 Funcionamiento interno

### 1. **Interfaz gráfica con Tkinter**
- Muestra una ventana con un botón para seleccionar la carpeta donde están tus archivos MIDI.
- También busca automáticamente el archivo `midisaya-tabla.md` dentro de esa carpeta o te permite seleccionarlo manualmente.

### 2. **Lectura del archivo Markdown**
- El script lee el archivo `midisaya-tabla.md`.
- Extrae los datos de la tabla: número, título, autor, secuenciador y estilo.

### 3. **Escaneo de archivos MIDI**
- Busca todos los archivos con extensión `.mid` o `.MID` en la carpeta seleccionada.

### 4. **Extracción del número y si tiene "M"**
- Usa una expresión regular para extraer el número y si tiene la letra `"M"` (ej: `123M.mid` → número=123, M=True).

### 5. **Generación del nuevo nombre**
- Basándose en los datos de la tabla, genera el nuevo nombre del archivo.

### 6. **Renombrado de archivos**
- Muestra una ventana de confirmación con una lista de cambios.
- Si aceptas, renombra los archivos.

---

## ▶️ Cómo hacerlo funcionar

### Paso 1: Guarda el script

Guarda el siguiente código como `renombrar_midis.py`:

```python
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
```

---

### Paso 2: Instala dependencias necesarias

```bash
sudo apt install python3 python3-pip python3.*-venv python3-dev python3-tk
```

Vea a más profundidad el siguiente tutorial (opcional):

**pip no me deja instalar paquetes de python en Debian 12 OK.md**
[https://github.com/wachin/Facilitar-el-Software-Libre/tree/main/Tutoriales/pip/pip%20no%20me%20deja%20instalar%20paquetes%20de%20python%20en%20Debian%2012](https://github.com/wachin/Facilitar-el-Software-Libre/tree/main/Tutoriales/pip/pip%20no%20me%20deja%20instalar%20paquetes%20de%20python%20en%20Debian%2012)


1. Clona el repositorio de xinput-gui

   ```bash
   git clone https://github.com/wachin/formacion-de-los-nombres-de-los-archivos-midi-de-midisaya.com
   ```

1. **Navega al directorio de tu proyecto**
   pon:

   ```bash
   cd formacion-de-los-nombres-de-los-archivos-midi-de-midisaya.com
   ```

2. **Crea allí un entorno virtual**
   Para evitar conflictos con otras instalaciones de Python, crea un entorno virtual:

   ```bash
   python3 -m venv venv
   ```

esto creará la carpeta:

venv

   >**Nota**: Este paso sólo se lo hace la primera vez.

3. **Activa el entorno virtual**
   y actívalo:

   ```
   source venv/bin/activate
   ```

   Esto activará el entorno virtual. Verás algo como `(venv)` al principio de tu línea de terminal.

   >**Nota**: Este paso hay que hacerlo cada vez que usted apague y encienda el ordenador y quiera usar el programa.

4. **instala allí el paquete pip**:

   ```bash
   pip install markdownify.
   ```

---

### Paso 3: Ejecuta el script

```bash
python3 renombrar_midis.py
```

Te aparecerá una ventana con un botón: **"Seleccionar Carpeta"**.

Haz clic, selecciona la carpeta donde están tus archivos MIDI, y el programa hará el resto.

---

## 🛠️ Notas importantes

- El script intenta encontrar automáticamente el archivo `midisaya-tabla.md` en la carpeta padre de la carpeta seleccionada. Si no está, te pedirá que lo selecciones tú mismo.
- Todos los archivos serán renombrados con extensión `.mid` en minúscula.
- Puedes probar primero con una copia de seguridad de tus archivos para evitar errores.

---

## 📝 Conclusión

Este script es ideal para **renombrar grandes colecciones de archivos MIDI**, dándoles nombres descriptivos basados en una tabla Markdown. Es muy útil si tienes muchos archivos sin nombres claros o difíciles de identificar manualmente.

---

# 🧠  script organizar_midis_por_autor.py

## ✅ Objetivo:
El script se llama: **`organizar_midis_por_autor.py`** y su objetivo es organizar los archivos MIDI renombrados en carpetas por **autor**, moviendo cada archivo a la carpeta correspondiente.

Si ya existe una carpeta con ese nombre, simplemente **mueve el archivo dentro de ella**.

---

## 📁 Ejemplo de estructura final

```
/MIDIS/
├── "Matthew Bridges & George J. Elvey"
│   └── 1M A Cristo Coronad - Matthew Bridges & George J. Elvey (MIDI Edgar Franco)(Pop).mid
├── "Marcos Witt"
│   ├── 2 A Cristo solo a Cristo - Marcos Witt (MIDI Edgar Franco)(Balada).mid
│   └── 995 Cristo Es Mi Senor - Marcos Witt (MIDI Edgar Franco)(Rock).mid
├── "Jesus Adrian Romero"
│   ├── 4M A sus pies - Jesus Adrian Romero (MIDI Edgar Franco)(Pop).mid
│   └── 762 Cada manana - Jesus Adrian Romero (MIDI Leonardo Puerto)(Pop).mid
└── ...
```

---

## 🔧 ¿Cómo funciona internamente?

### 1. **Interfaz gráfica con Tkinter**
- Muestra una ventana con un botón para seleccionar la carpeta donde están tus archivos MIDI.
- No necesitas escribir rutas ni usar consola si no quieres.

### 2. **Selección de carpeta**
- Al hacer clic en el botón, te abre un diálogo para elegir la carpeta con tus archivos MIDI.

### 3. **Extracción del autor**
- Lee el nombre de cada archivo y extrae el **nombre del autor** que está entre el guion `" - "` y el primer paréntesis `"("`.
- Ejemplo:
  ```
  5 Al estar aqui - Danilo Montero (MIDI Edgar Franco)(Pop).mid
  → Autor = Danilo Montero
  ```

### 4. **Creación de carpetas**
- Si no existe una carpeta con el nombre del autor, la crea.
- Si ya existe, simplemente mueve el archivo allí.

### 5. **Movimiento de archivos**
- Mueve cada archivo a su carpeta correspondiente.
- Puedes cambiar esto a **copiar** en lugar de mover, si lo prefieres.

### 6. **Mensaje de confirmación**
- Al final, muestra cuántos archivos se han movido por cada autor.

---

## 🐍 Requisitos técnicos

### 💾 Instalación previa:

Este script necesita las siguientes herramientas instaladas:

```bash
pip install tk
```

> En Debian, normalmente `tk` viene preinstalado, pero puedes instalarlo con:
```bash
sudo apt install python3-tk
```

---

## ▶️ Cómo hacerlo funcionar

### Paso 1: Guarda el script

Guarda el siguiente código como `organizar_midis_por_autor.py` en tu computadora:

```python
import os
import re
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para extraer SOLO el nombre del autor del archivo
def extraer_autor(nombre_archivo):
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
```

---

### Paso 2: Ejecuta el script

Desde la terminal:

```bash
python3 organizar_midis_por_autor.py
```

Te aparecerá una ventana con un botón: **"Seleccionar Carpeta"**.

Haz clic, selecciona la carpeta donde están tus archivos MIDI ya renombrados, y el programa hará el resto.

---

## 🛠️ Opciones adicionales (opcional)

### ➕ Cambiar "mover" por "copiar"

Busca esta línea:

```python
shutil.move(ruta_original, ruta_destino)
```

Y cámbiala por:

```python
shutil.copy(ruta_original, ruta_destino)
```

Así no borra los archivos originales.

---

## 📝 Conclusión

Este script es ideal para **organizar una gran colección de archivos MIDI** de forma automática, creando carpetas por **autor** basándose en el nombre del archivo. Es muy útil después de haber usado el primer script para renombrar los archivos según el archivo `midisaya-tabla.md`.







