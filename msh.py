import getpass
import os

username = getpass.getuser()

print("Windows MicroShell\n")

prompt = "microshell [" + username + "] ~ "

while True:
    cmd = input(prompt)

    cmdBody = cmd.split(" ")[0]
    try:
        cmdAttr = cmd.split(" ")[1]
        cmdAttrs = cmdAttr.split(" ")
    except IndexError:
        continue
    finally:
        if cmdBody == "echo":
            print(cmdAttr)

        elif cmdBody == "echoconf":
            if cmdAttr == "on":
                prompt = "microshell [" + username + "] ~ "
            elif cmdAttr == "off":
                prompt = ""
            else:
                print("[Error] echoconf option incorrect")

        elif cmdBody == "clear":
            os.system("cls")

        elif cmdBody == "getcd":
            os.system("echo %cd%")

        elif cmdBody == "poweroff":
            os.system("shutdown -s -t %s" % cmdAttr)

        elif cmdBody == "reboot":
            os.system("shutdown -r -t %s" % cmdAttr)

        elif cmdBody == "setcolor":
            os.system("color %s" % cmdAttr)

        elif cmdBody == "cmd":
            os.system("cmd")

        elif cmdBody == "psh":
            os.system("powershell")

        elif cmdBody == "cmdls":
            print("\necho  echoconf  clear  getcd  poweroff\nsetcolor  cmd  psh\n")
            print("More info:\n   help [object]\n")

        elif cmdBody == "help":
            if cmdAttr == "echo":
                print("\nOutputing message\n\nUsage:\n  echo [message]\n")

        elif cmd.strip() == "":
            pass

        else:
            print("[Error] Command is not found or incorrect")

    # TODO: Add command execute engine
