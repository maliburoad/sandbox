del /S /F /Q .\dist\*
del /S /F /Q .\build\*

pyinstaller -F -y --clean^
	--onefile^
	--icon=Key.ico^
    --hidden-import="pkg_resources"^
    Autoserial.py^