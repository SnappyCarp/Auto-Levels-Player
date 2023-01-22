import pygetwindow as Get
from time import sleep as S

def main():
	Title = Get.getWindowsWithTitle('Geometry Dash')
	if Title == '[Win32Window(hWnd=29821340)]':
		print(Title)
	else:
		print('Geometry Dash is not opened')
		S(3)
		main()


main()