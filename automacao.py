import pyautogui;
import time;

#Abertura do chrome
#Abrir programa via botão do windows
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#procurar algo no google
time.sleep(1)
pyautogui.hotkey("ctrl","t")
time.sleep(1)
pyautogui.doubleClick(x=-910,y=387)
pyautogui.write("hltv")
pyautogui.press("enter")