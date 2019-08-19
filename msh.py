import getpass
import os

username = getpass.getuser()

def cmd(command):
    os.system(str(command))

print("Windows MicroShell")

prompt = "microshell [" + username + "] ~ "
while True:
    cmd = input(prompt)

    cmdBody = cmd.split(" ")[0]
    try:
        cmdAttr = cmd.split(" ")[1]
    except IndexError:
        continue

    if cmdBody == "echo":
        print(cmdAttr)

    # TODO: Add command execute engine
