all: windows

windows: build_forms
	cxfreeze app.py --target-dir dist/windows --base-name Win32GUI

build_forms:
	@echo "Building UI forms"
	pyside6-uic ui/mainwindow.ui > ui/mainwindow.py