import pyautogui
import time
import os
import sys

archivo = "aseprite.exe"
ruta = "C:\\"

width, height = pyautogui.size()
print(f"La resolución de pantalla actual es {width} x {height} píxeles.")

for root, dirs, files in os.walk(ruta):
    if archivo in files:
        print(f"El archivo {archivo} fue encontrado en {os.path.join(root, archivo)}")
        if width == 1920 and height == 1080:
            # Abre Aseprite
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite('as')
            time.sleep(1)
            pyautogui.typewrite('ep')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(2)  # Espera a que Aseprite se abra

            # crear nuevo archivo
            print("File creation")
            pyautogui.moveTo(20, 50, duration=0.25)
            time.sleep(1) 
            pyautogui.click()

            print("File enter")
            time.sleep(1) 
            pyautogui.moveTo(20, 60, duration=0.25)
            time.sleep(1) 
            pyautogui.click()

            print("Ancho")
            time.sleep(1) 
            pyautogui.moveTo(960, 400, duration=0.25)
            time.sleep(1) 
            pyautogui.typewrite('16')

            print("Largo")
            time.sleep(1) 
            pyautogui.moveTo(960, 435, duration=0.25)
            time.sleep(1) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.press('Backspace')
            pyautogui.press('Backspace')
            pyautogui.press('Backspace')
            pyautogui.press('Backspace')
            time.sleep(1)
            pyautogui.typewrite('16')

            print("Crear")
            time.sleep(1) 
            pyautogui.moveTo(930, 699, duration=0.25)
            time.sleep(1) 
            pyautogui.click()

            print("Posicion Zoom")
            time.sleep(1) 
            pyautogui.moveTo(1040, 429, duration=0.25)
            pyautogui.scroll(1)
            pyautogui.scroll(1)
            pyautogui.scroll(1)
            pyautogui.scroll(1)
            pyautogui.scroll(1)
            pyautogui.scroll(1)
            pyautogui.scroll(1)

            print("CrearKirby")
            time.sleep(1)
            pyautogui.moveTo(92, 877, duration=0.25)
            pyautogui.click()
            # Fila 1 
            pyautogui.moveTo(849, 665, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(849, 498, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(849, 473, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(849, 449, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(849, 408, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(849, 384, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(849, 430, duration=0.25)
            pyautogui.click()

            #Fila 2
            pyautogui.moveTo(872, 695, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(872, 646, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(872, 571, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(872, 547, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(872, 529, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(872, 357, duration=0.25)
            pyautogui.click()

            #Fila 3
            pyautogui.moveTo(896, 694, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(896, 623, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(896, 600, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(896, 331, duration=0.25)
            pyautogui.click()

            #Fila 4
            pyautogui.moveTo(918, 332, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(918, 377, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(918, 620, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(918, 694, duration=0.25)
            pyautogui.click()

            #Fila 5
            pyautogui.moveTo(951, 359, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(951, 646, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(951, 696, duration=0.25)
            pyautogui.click()

            #Fila 6
            pyautogui.moveTo(967, 334, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(967, 646, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(967, 688, duration=0.25)
            pyautogui.click()

            #Fila 7
            pyautogui.moveTo(999,337, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(999, 405, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(999, 431, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(999, 450, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(999, 663, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(999, 696, duration=0.25)
            pyautogui.click()

            #Fila 8
            pyautogui.moveTo(1019, 329, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1019, 500, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1019, 526, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1019, 667, duration=0.25)
            pyautogui.click()

            #Fila 9
            pyautogui.moveTo(1045, 334, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1045, 408, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1045, 436, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1045, 455, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1045, 666, duration=0.25)
            pyautogui.click()

            #Fila 10
            pyautogui.moveTo(1067, 331, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1067, 646, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1067, 668, duration=0.25)
            pyautogui.click()

            #Fila 11
            pyautogui.moveTo(1090, 357, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1090, 597, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1090, 624, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1090, 672, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1090, 693, duration=0.25)
            pyautogui.click()

            #Fila 12
            pyautogui.moveTo(1116, 357, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1116, 576, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1116, 694, duration=0.25)
            pyautogui.click()

            #Fila 13
            pyautogui.moveTo(1137, 382, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1137, 550, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1137, 691, duration=0.25)
            pyautogui.click()

            #Fila 14
            pyautogui.moveTo(1162, 406, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1162, 430, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1162, 548, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1162, 668, duration=0.25)
            pyautogui.click()

            #Fila 15
            pyautogui.moveTo(1187, 455, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1187, 550, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1187, 645, duration=0.25)
            pyautogui.click()

            #Fila 16
            pyautogui.moveTo(1211, 478, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1211, 501, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1211, 525, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1211, 572, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1211, 600, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(1211, 622, duration=0.25)
            pyautogui.click() 


            print("Pintando")
            #Pintar
            time.sleep(1)
            pyautogui.moveTo(172, 891, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(117, 776, duration=0.25)
            pyautogui.click()
            pyautogui.press('G')


            pyautogui.moveTo(927, 526, duration=0.25)
            pyautogui.click()


            pyautogui.moveTo(193, 890, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(182, 776, duration=0.25)
            pyautogui.click()

            pyautogui.moveTo(913, 662, duration=0.25)
            pyautogui.click()

            pyautogui.moveTo(1151, 602, duration=0.25)
            pyautogui.click()

            print("Es Kirby!")
            sys.exit("Byw bye")
        else:
            print("Tu resolucion a de ser de 1920 x 1080 !")
    

"""

moveTo(x, y, duration=0.0): Mueve el cursor del ratón a las coordenadas (x, y) en la pantalla. Puede especificarse una duración en segundos para hacer que el movimiento sea más lento.

click(x=None, y=None, clicks=1, button='left'): Hace clic en las coordenadas (x, y) con el botón especificado ('left', 'right', 'middle'). Si no se especifican las coordenadas, el clic se realiza en la posición actual del cursor. Se puede especificar un número de clics.

scroll(clicks=0, x=None, y=None, pause=None, _pause=True, horiz=False): Realiza un desplazamiento de scroll en la posición actual del cursor o en las coordenadas (x, y). Puede especificarse el número de clics, la duración de pausa entre clics, y si el desplazamiento debe ser horizontal o vertical.

typewrite(message, interval=0.0): Escribe el mensaje en el teclado. Puede especificarse un intervalo en segundos entre las pulsaciones de teclas para simular la escritura más humana.

press(keys, presses=1, interval=0.0): Presiona una o varias teclas en el teclado. Se pueden especificar varias teclas separadas por comas. Se puede especificar el número de pulsaciones y la duración de pausa entre ellas.

hotkey(*args, **kwargs): Simula la pulsación de una combinación de teclas, como ctrl+c, alt+tab, etc.

screenshot(region=None): Toma una captura de pantalla de toda la pantalla o de una región específica.

alert(text='', title='', button='OK'): Muestra una alerta con el mensaje especificado y el botón especificado.

prompt(text='', title='', default=''): Muestra un cuadro de diálogo de entrada que solicita al usuario que escriba una respuesta.
"""
