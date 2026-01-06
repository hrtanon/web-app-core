from pathlib import Path
import os


home=Path.home()
print(home)
p=home/"test_soubory"/"TEXT_SOUBORw"/"ouvejte.txt"/"rrraah"
p.touch()