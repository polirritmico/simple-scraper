#!/usr/bin/env python
# -*- coding: utf-8 -*-

def short_usage():
    print("Utilice la opción --help para obtener ayuda.")

def usage():
    print("""Modo de empleo: simple-scraper.py [OPCIÓN] [MODO] [ARCHIVO/URL] [SALIDA]
Busca y descarga las páginas especificadas en el ARCHIVO/URL y devuelve
los resultados dentro del archivo de texto SALIDA.

Opciones:
  -h, --help        Muestra este texto y cierra el programa.
  -v, --verbose     Para activar la salida en consola.
  -d, --delay[=SEG] Para añadir un tiempo en segundos de espera entre
                    cada url. No funciona en el modo JavaScript.
  -j, --javascript  Obtiene el HTML a través de un "navegador virtual".
                    Se debe configurar en <config.py>.

Modo:
  -l, --list        Para procesar un archivo de lista.
  -u, --url         Para procesar una lista.
  -f, --file        Para procesar un HTML descargado.

Ejemplo de uso:
./simple-scraper.py -vj -d 2 --url http://www.pagina.com salida.txt

Archivo de entrada:
Un archivo txt con una url por línea. El programa respeta las líneas 
vacías para que se alinee la salida con bases de datos o tablas.

Archivo de salida:
El archivo contendrá por cada línea las coincidencias de la búsqueda
separadas por un tabulador (\\t). Las líneas vacías coincidirán con las
líneas vacías del archivo de entrada.

Archivo de Configuración:
Dentro de <config.py> se puede configurar para que funcione el modo
javascript y los parámetros de búsqueda (RegEx). Dentro del archivo hay
más información.

Más información en https://github.com/polirritmico/simple-scraper
""")