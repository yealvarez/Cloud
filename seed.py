#!/bin/bash
python3 -c 'import pyotp; totp = pyotp.TOTP("<<<token seed here>>"); print(totp.now(), end="")' | clip.exe
powershell.exe -command "Get-Clipboard"
