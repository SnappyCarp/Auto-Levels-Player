import pygetwindow as Get
import pyautogui as Pyauto
from time import sleep as S

def main():
	Title = Get.getWindowsWithTitle('Geometry Dash')
	if Title == []:
		print('Geometry Dash is not opened')
		S(3)
		main()
	else:
		print(Title)


main()