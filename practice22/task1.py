#Пункт 1
from pathlib import Path

cwd = Path.cwd()
script = Path(__file__).resolve()
script_dir = script.parent
home = Path.home()

print("cwd:", cwd)
print("script:", script)
print("script dir:", script_dir)
print("home:", home)

#Пункт 2
data_dir = script_dir / "data"
reports_dir = script_dir / "reports"
backups_dir = script_dir / "backups"

data_dir.mkdir(exist_ok=True)
reports_dir.mkdir(exist_ok=True)
backups_dir.mkdir(exist_ok=True)

#Пункт 3
profile_path = data_dir / "profile.txt"

with profile_path.open("w", encoding="utf-8") as file:
    file.write("name: Nikita\n")
    file.write("surname: Krilovets\n")
    file.write("group: IT-31\n")
    file.write("year: 2009\n")
    file.write("language: Python\n")

#Пункт 4
print("profile path:", profile_path.resolve())
print("relative:", profile_path.relative_to(script_dir))
print("name:", profile_path.name)
print("stem:", profile_path.stem)
print("suffix:", profile_path.suffix)
print("parent:", profile_path.parent.name)
print("size:", profile_path.stat().st_size, "bytes")

#Пункт 5
print("\nproject tree:")

for path in sorted(script_dir.rglob("*")):
    relative = path.relative_to(script_dir)
    indent = "  " * (len(relative.parts) - 1)

    if path.is_dir():
        print(f"{indent}{path.name}/")
    else:
        print(f"{indent}{path.name}")