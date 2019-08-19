import getpass
import os

username = getpass.getuser()

print("Windows MicroShell")

while True:
    cmd = input("microshell [" + username + "] ~ ")

    cmdBody = cmd.split(" ")[0]
    try:
        cmdAttr = cmd.split(" ")[1]
    except IndexError:
        continue

    if cmdBody == "echo":
        print(cmdAttr)

    # TODO: Add command execute engine
