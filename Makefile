.DEFAULT: all

all: windows

windows: forms
	@echo Building for Windows
	cxfreeze app.py --target-dir dist/windows --base-name Win32GUI --include-files qss/

forms:
	@echo Building UI forms
	pyside6-uic ui/mainwindow.ui > ui/mainwindow.py
