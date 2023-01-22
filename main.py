import pygetwindow as Get
import pyautogui as pyauto
from time import sleep as S

def main():
	Title = Get.getWindowsWithTitle('Geometry Dash')
	if Title == []:
		print('Geometry Dash is not opened')
		S(3)
		main()
	else:
		print('Window Found')
		button()
		

def button():
	img = pyauto.locateCenterOnScreen('CreateButton.png', grayscale=False)
	if img == None:
		print('Button not Found')
		S(1)
		button()
	else:
		print('Button Found')
		



main()