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
            if cmdAttr.strip() == "":
                print(cmdAttr)

            if not cmdAttr.strip() == "":
                print("")

        elif cmdBody == "echoconf":
            if cmdAttr == "on":
                prompt = "microshell [" + username + "] ~ "
            elif cmdAttr == "off":
                prompt = ""
            else:
                print("[Error] echoconf option incorrect")

        elif cmdBody == "clear":
            os.system("cls")

        elif cmd.strip() == "":
            pass

        else:
            print("[Error] Command is not found or incorrect")

    # TODO: Add command execute engine
