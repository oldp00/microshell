import getpass
import os

username = getpass.getuser()

print("Windows MicroShell")

prompt = "microshell [" + username + "] ~ "
while True:
    cmd = input(prompt)

    cmdBody = cmd.split(" ")[0]
    try:
        cmdAttr = cmd.split(" ")[1]
    except IndexError:
        continue
    finally:
        if cmdBody == "echo":
            print(cmdAttr)

        if cmdBody == "clear":
            os.system("cls")

    # TODO: Add command execute engine
