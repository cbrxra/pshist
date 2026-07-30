from config.paths import APP_DIR, PROFILES_DIR, CONFIG_FILE, TEMP_DIR, Path

import sys
import os
import json

from utils.windows import is_hidden, hide

from services.PowershellService import PowerShellService
from repositories.ProfileRepository import ProfileRepository
from repositories.ConfigRepository import ConfigRepository


class StartupService:
    
    def initialize(self):
        APP_DIR.mkdir(exist_ok = True)
        PROFILES_DIR.mkdir(parents = True, exist_ok = True)
        TEMP_DIR.mkdir(parents = True, exist_ok = True)

        self.__init__funpws1()

        if not CONFIG_FILE.exists():
            self.__init_config_file()

        self.__load_default_profile()

        try:
            if not is_hidden(APP_DIR):    
                hide(APP_DIR)
            
            if not is_hidden(TEMP_DIR):    
                hide(TEMP_DIR)
                
        except FileNotFoundError as e:
            print(f"[WARN] No se pudo ocultar: {e}")
            
    
    
    def __init_config_file(self):    
        config_data = {
            "settings" : {
                "currentProfile": "default",
                "defaultProfile": "default",
            }
        }

        with open(CONFIG_FILE, "w", encoding = "utf-8") as file:
            json.dump(config_data, file, indent = 4)
    
    def __init__funpws1(self):
        
        pathProfile = PowerShellService().ensure_profile_path()
        
        pathScript = Path.cwd() / sys.argv[0]
        
        
        if ".exe" in pathScript.name:
            exec = f'& "{pathScript}" @args'
        else:
            exec = f'py "{pathScript}" @args'

        fun = f"""
function pshist {{
    
    {exec}

    if ($LASTEXITCODE -ne 0) {{
        return
    }}

    if ($args.Count -ge 2 -and $args[0] -eq "profile" -and $args[1] -in @("use", "exit")) {{
        
        $historyPath = (Get-PSReadLineOption).HistorySavePath
        
        if (Test-Path $historyPath) {{
            
            [Microsoft.PowerShell.PSConsoleReadLine]::ClearHistory()
            
            (Get-Content $historyPath -Raw) -split "`r?`n" | Where-Object {{ $_ }} | ForEach-Object {{
                [Microsoft.PowerShell.PSConsoleReadLine]::AddToHistory($_)
            }}
        }}
    }}
}}
"""
        data = pathProfile.read_text(encoding = "utf-8")

        if not (fun in data):
            with open(pathProfile, "a", encoding = "utf-8") as file:
                file.write("\n" + fun)

    def __load_default_profile(self):

        name_defaultprofile = ConfigRepository().get_default_profile()

        path_default = PROFILES_DIR / "default"
        path_history = path_default / "History.txt"
        path_default.mkdir(parents = True, exist_ok = True)
        path_history.touch(exist_ok = True)

        name_profile = path_default.name

        if not ProfileRepository().exists(name_defaultprofile):
            ConfigRepository().set_default_profile(name_profile)

        if name_defaultprofile == "default" and os.path.getsize(path_history) == 0:  
            history_powershell = PowerShellService().get_history()
            ProfileRepository().append_history(name_profile, history_powershell)


          

            

            


        


        


        
    

        





        

    

        

        

        



  