import cv2, pyautogui, threading, os, sys
from pynput import keyboard
import numpy as np

recording = False
out = None
video_count = 1
screenshot_count = 1
u=os.getlogin()
alm1=f'C:\\Users\\{u}\\Videos\\Screenrecorder'
alm2=f'C:\\Users\\{u}\\Pictures\\Screenshot'

if not os.path.exists(alm1) or not os.path.exists(alm2):
 os.makedirs(alm1)
 os.makedirs(alm2)

def grabar():
 global recording, out, video_count
 fps = 10.0
 resolucion = pyautogui.size()
 fourcc = cv2.VideoWriter_fourcc(*'mp4v')
 video_name = f'{alm1}\\screenrecorder_{video_count}.mp4'
 out = cv2.VideoWriter(video_name, fourcc, fps, resolucion)
 recording = True
 while recording:
  frame = np.array(pyautogui.screenshot())
  frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
  out.write(frame)
 out.release()
 try:
  os.system(f"MSG * CAPTURA DE VIDEO ALMACENADO EN {alm1}")
 except OSError:
  pass
 video_count += 1

def on_press(key):
 global recording, screenshot_count
 if key == keyboard.Key.f5:
  try:
   os.system(f"MSG * CAPTURANDO VIDEO, PARA FINALIZAR EL VIDEO PRESIONE [F6]")
  except OSError:
   pass
  if not recording:
   threading.Thread(target=grabar).start()
 elif key == keyboard.Key.f6:
  if recording:
   recording = False
 elif key == keyboard.Key.f7:
  screenshot_name = f'{alm2}\\screenshot_{screenshot_count}.png'
  img = pyautogui.screenshot()
  img.save(screenshot_name)
  try:
   os.system(f"MSG * CAPTURA DE PANTALLA ALMACENADO CON EXITO EN {alm2}")
  except OSError:
   pass
  screenshot_count += 1
 elif key == keyboard.Key.pause:
  sys.exit()

with keyboard.Listener(on_press=on_press) as listener:
 listener.join()
