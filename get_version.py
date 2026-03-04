Import("env")
import os
import shutil
import atexit

def get_version():
    with open("version", "r") as f:
        return f.read().strip()

version = get_version()
env.Append(CPPDEFINES=[("VERSION", f'\\"{version}\\"')])

def copy_firmware_on_exit():
    project_dir = env["PROJECT_DIR"]
    profile = env["PIOENV"]
    firmware_path = os.path.join(project_dir, ".pio", "build", profile, "firmware.bin")
    
    if os.path.exists(firmware_path):
        dest_dir = os.path.join(project_dir, "ota", version, profile)
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, "firmware.bin")
        shutil.copy(firmware_path, dest_path)
        print(f"Copied firmware to {dest_path}")

atexit.register(copy_firmware_on_exit)
