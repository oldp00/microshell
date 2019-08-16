import getpass
username = getpass.getuser()

print("Windows MicroShell v0.0.1 alpha")

while True:
    cmd = input("microshell [" + username + "] ~ ")

    cmdBody = cmd.split(" ")[2]
    cmdAttr = cmd.split(" ")[1]
    
    # TODO: Add command execute engine
