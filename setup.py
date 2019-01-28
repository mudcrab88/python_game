from cx_Freeze import setup, Executable

setup(
    name = "AlienInvasion",
    version = "1.0",
    description = "Alien Invasion Game",
    executables = [Executable("alien_invasion.py")]
)
