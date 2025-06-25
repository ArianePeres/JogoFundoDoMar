from cx_Freeze import setup, Executable

executables = [Executable("main.py")]


setup(
    name="AventuraSubmarina",
    version="1.0",
    description="Aventura Submarina app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)
