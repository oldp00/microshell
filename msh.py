import getpass
import resource
username = getpass.getuser()

print("Windows MicroShell v0.0.1 alpha")

while True:
    cmd = input("microshell [" + username + "] ~ ")

    cmdBody = cmd.split(" ")[0]
    cmdAttr = cmd.split(" ")[1]

    if cmdBody == "echo":
        print(cmdAttr)

    # TODO: Add command execute engine
