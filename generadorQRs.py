# GENERADOR DE CODIGOS QR EN PYTHON
# Creado el 20-1-2024 por Unai Romero Santos
# Version: 0.1

## Importamos la libreria qrcode y os para generar el codigo QR y para poder guardar la imagen.
import qrcode;
import os;

## Funcion para generar un codigo QR y guardarlo en una carpeta.
def generarQR():
    enlace = input("Introduce el enlace que quieres convertir en QR:");
    nombreArchiv=input("Introduce el nombre del archivo QR: ");
    carpeta = "QRs";
    
    ## Comprobamos si la carpeta existe, si no existe la creamos.
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"Carpeta '{carpeta}' creada.")
    
     # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta, nombreArchiv + ".png")
    
    ## Creamos el objero QR y le añadimos el enlace, tamaño, color y borde.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(enlace)
    qr.make(fit=True)
    imagenQR = qr.make_image(fill_color="black", back_color="white")
    
    ## Guardamos la imagen en la carpeta con el nombre introducido.
    imagenQR.save(ruta_archivo)
    print("El codigo QR ha sido generado con exito");

## Bienvenida y menu de opciones.
print("Bienvenido al generador de codigos QR en Python, por favor, selecciona una opcion:");
print("1.- Generar QR");
print("2.- Salir");

## Seleccion de opcion.
selec = input();
if selec != "1":
    exit();
else:
    generarQR();