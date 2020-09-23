# sample-cross-platform-wxpython
A sample application written using wxpython.
Should work in Windows, MacOS, and Linux.


## What it does
The application erform simple JSON validation, and CRC32 checksum of JSON in formatted form.

## Installation
You can use this application as an executable, or as python code.

### As an executable
Install packages.
```
pip3 install -r requirements/dev.txt
```
Use [PyInstaller](https://www.pyinstaller.org/) directly (modifying .spec file not needed).
```
pyinstaller --windowed app.py
```
Execute the executable, click to run.
```
dist/app/app    # Linux
or
dist/app.app    # MacOS
or
dist\app\app.exe    # Windows
```

### As code
Install packages.
```
pip3 install -r requirements/common.txt
```
Run code.
```
python3 app.py
```

## Notes
If you are using [PyInstaller](https://www.pyinstaller.org/) inside [pyenv](https://github.com/pyenv/pyenv), the following links is worth reading:
* [How to build CPython with `--enable-shared`](https://github.com/pyenv/pyenv/wiki#how-to-build-cpython-with---enable-shared)
* [pyenv and PyInstaller](https://pyinstaller.readthedocs.io/en/stable/development/venv.html)
