import shutil, os


if os.geteuid() != 0:
    print("This script requires root privileges.")
    exit()
else:
    print("Running with root privileges.")


def patch_sublime4143():
    shutil.copyfile("/opt/sublime_text/sublime_text", "./sublime_text")

    with open("sublime_text", "r+b") as crack:
        crack.seek(0x003A31F2)
        crack.write(b"\x48\x31\xC0\xC3")

        crack.seek(0x00399387)
        crack.write(b"\x90\x90\x90\x9090")

        crack.seek(0x0039939D)
        crack.write(b"\x90\x90\x90\x90\x90")

        crack.seek(0x003A4E30)
        crack.write(b"\x48\x31\xC0\x48\xFF\xC0\xC3")

        crack.seek(0x003A2E82)
        crack.write(b"\xC3")

        crack.seek(0x0038C9F0)
        crack.write(b"\xC3")

    shutil.move("sublime_text", "/opt/sublime_text/sublime_text")
    os.system("chmod 755 /opt/sublime_text/sublime_text")
    print("done")
patch_sublime4143()
