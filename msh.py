import getpass
username = getpass.getuser()

print("Windows MicroShell v0.0.1 alpha")

while True:
    cmd = input("microshell [" + username + "] ~ ")

    # TODO: Add command execute engine
