import PyPDF2
import pyttsx3

def audiobook ():
    #INGRESO EL NOMBRE DEL PDF
    nombre_pdf = input("Ingrese el nombre del pdf a leer:")
    pdf = nombre_pdf + ".pdf" #CONCATENO

    #ABRO EL ARCHIVO
    try:
        archivo_pdf =  open(pdf, 'rb')
        pdf_leido = PyPDF2.PdfFileReader(archivo_pdf)

    except FileNotFoundError:
        print("El archivo ingresado no existe, intente nuevamente.")

    num_paginas = pdf_leido.numPages #EXTRAIGO LAS PAGINAS EN ESTA VARIABLE

    texto_completo = "" #CREO UNA VARIABLE QUE ALMACENA LOS STRINGS DE CADA PAGINA 

    voz = pyttsx3.init()
    voz.setProperty("rate", 170)
    voces = voz.getProperty('voices')

    print('LEYENDO PDF...')

    #INDICO CON QUE VOZ QUIERO QUE SE LEA MI PDF
    for voice in voces:
        if voice.name == "Microsoft Sabina Desktop - Spanish (Mexico)":
            voz.setProperty('voice', voice.id)

    # EMPIEZO A RECORRER CADA PAGINA 
    for pagina in range(5, num_paginas):
        pag_sig = pdf_leido.getPage(pagina)
        leido = pag_sig.extractText()
        texto_completo += leido #VOY ALMACENANDO EN LA VARIABLE 'texto_completo' LOS STRINGS DE CADA PAGINA
        x = pagina + 1 #CUENTO LA CANTIDAD DE PAGINAS
        print(f"LEYENDO PAGINA {x}/{num_paginas}.")
    
    nombre_audio = input("\nIngrese el nombre con que desea guardar su AudioBook:")
    mp3 = nombre_audio + ".mp3"

    print("\n\tCREANDO AUNDIOBOOK, ESPERE POR FAVOR...")

    voz.save_to_file(texto_completo, mp3)
    voz.runAndWait()

    print("\nAUDIOBOOK CREADO CON ÉXITO")

audiobook()