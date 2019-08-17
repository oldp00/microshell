import getpass
username = getpass.getuser()

print("Windows MicroShell v0.0.1 alpha")

while True:
    cmd = input("microshell [" + username + "] ~ ")

    cmdBody = cmd.split(" ")[0]
    cmdAttrs = cmd.split(" ")[1]

    # TODO: Add command execute engine
