import getpass
import resource as rc

username = getpass.getuser()

print("Windows MicroShell v0.0.1 alpha")

while True:
    cmd = input("microshell [" + username + "] ~ ")

    cmdBody = cmd.split(" ")[0]
    try:
        cmdAttr = cmd.split(" ")[1]
    except IndexError:
        continue

    if cmdBody == "echo":
        rc.echo(cmdAttr)

    # TODO: Add command execute engine
