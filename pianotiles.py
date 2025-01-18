import pyautogui as pag
import webbrowser
from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep

def on_release(key):
    global esc_pressed
    if key == keyboard.Key.esc:
        esc_pressed = True
        return False

def click(position):
    mouse.position = position
    mouse.press(Button.left)
    sleep(0.05)
    mouse.release(Button.left)

mouse = Controller()
kbd = keyboard.Controller()

esc_pressed = False
on_screen = False
path = "./img/start_button.png"

box_1_center = (925, 328)
box_2_center = (991, 328)
box_3_center = (1057, 328)
box_4_center = (1123, 328)
box_color = (0, 0, 0)
delay = 0.5

with keyboard.Listener(on_release=on_release) as listener:
    # Posiciona o terminal à esquerda
    kbd.press(keyboard.Key.cmd_l)
    sleep(0.1)
    kbd.press(keyboard.Key.left)
    sleep(0.1)
    kbd.release(keyboard.Key.left)
    sleep(0.1)
    kbd.release(keyboard.Key.cmd_l)
    sleep(0.1)

    # Abre a página do jogo
    webbrowser.open("https://gameforge.com/en-US/littlegames/magic-piano-tiles/")
    sleep(delay)
    
    # Posiciona a página à direita
    kbd.press(keyboard.Key.cmd_l)
    sleep(0.1)
    kbd.press(keyboard.Key.right)
    sleep(0.1)
    kbd.release(keyboard.Key.right)
    sleep(0.1)
    kbd.release(keyboard.Key.cmd_l)
    sleep(0.1)

    while not on_screen and not esc_pressed:
        try:
            position = pag.locateCenterOnScreen(path, confidence=0.9)
        except pag.ImageNotFoundException:
            sleep(delay * 15)
            pag.alert(text='Não foi possível localizar a tela inicial, por favor feche os anúncios e role a barra lateral se for necessário', title='Erro', button='Ok')
        else:
            start_button = (int(position.x), int(position.y))
            pag.click(start_button, duration=delay)
            on_screen = True

    while not esc_pressed:
        if pag.pixelMatchesColor(box_1_center[0], box_1_center[1], box_color):
            click(box_1_center) 
        if pag.pixelMatchesColor(box_2_center[0], box_2_center[1], box_color):
            click(box_2_center)
        if pag.pixelMatchesColor(box_3_center[0], box_3_center[1], box_color):
            click(box_3_center)
        if pag.pixelMatchesColor(box_4_center[0], box_4_center[1], box_color):
            click(box_4_center)
    listener.join()