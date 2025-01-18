import win32api
import win32con
import pyautogui as pag
import webbrowser
import keyboard
from time import sleep

def click(pos):
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

on_screen = False
path = '.\\img\\start_button.png'

box_1_center = (925, 328)
box_2_center = (991, 328)
box_3_center = (1057, 328)
box_4_center = (1123, 328)
box_color = (0, 0, 0)
delay = 0.5

webbrowser.open("https://gameforge.com/en-US/littlegames/magic-piano-tiles/")
sleep(delay)
pag.hotkey('command', 'right')
sleep(delay)

while not on_screen:
    try:
        position = pag.locateCenterOnScreen(path, confidence=0.9)
    except pag.ImageNotFoundException:
        pag.alert(text='Não foi possível localizar a tela inicial, por favor feche os anúncios e role a barra lateral se for necessário', title='Erro', button='Ok')
        sleep(delay * 20)
    else:
        start_button = (int(position.x), int(position.y))
        pag.click(start_button, duration=delay)
        on_screen = True

while keyboard.is_pressed('1') == False:
    if pag.pixelMatchesColor(box_1_center[0], box_1_center[1], box_color):
        click(box_1_center) 
    if pag.pixelMatchesColor(box_2_center[0], box_2_center[1], box_color):
        click(box_2_center)
    if pag.pixelMatchesColor(box_3_center[0], box_3_center[1], box_color):
        click(box_3_center)
    if pag.pixelMatchesColor(box_4_center[0], box_4_center[1], box_color):
        click(box_4_center)
