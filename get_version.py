Import("env")
import os
import shutil

def get_version():
    with open("version", "r") as f:
        return f.read().strip()

version = get_version()
env.Append(CPPDEFINES=[("VERSION", f'\\"{version}\\"')])

def copy_firmware(source, target, env):
    firmware_path = str(target[0])
    profile = env["PIOENV"]
    project_dir = env["PROJECT_DIR"]
    
    dest_dir = os.path.join(project_dir, "ota", version, profile)
    os.makedirs(dest_dir, exist_ok=True)
    
    dest_path = os.path.join(dest_dir, "firmware.bin")
    shutil.copy(firmware_path, dest_path)
    print(f"Copied firmware to {dest_path}")

env.AddPostAction("$BUILD_DIR/firmware.bin", copy_firmware)
