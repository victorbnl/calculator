all: build_forms

build_forms:
	@echo "Building UI forms"
	pyside6-uic ui/mainwindow.ui > ui/mainwindow.py