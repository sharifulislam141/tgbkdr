import platform

system = platform.system()

if system == "Windows":
    print("Windows operating system detected.")
elif system == "Linux":
    if "TERMUX" in platform.uname()[2]:
        print("Android operating system detected in Termux.")
    else:
        print("Linux operating system detected.")
elif system == "Darwin":
    print("macOS operating system detected.")
else:
    print("Unknown operating system detected.")
