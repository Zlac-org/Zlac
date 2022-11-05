# advance.py is a part of Zlac and is registered under the same license : Apache License, Version 2.0
# Intro screen in zlac
# Copyright 2022 Zlac-org

try:
    import time
    import vlc
    import os
except ImportError:
    print('\n[ERROR] Failed importing modules. Make sure the venv is activated or try running ''pip install -r recquirements.txt''')    
    # If any dependency is missing or venv not activated

cws = os.name
# Creating the player object

try:

    player = vlc.MediaPlayer()
    media = vlc.Media("scrT.mp4")
    player.set_media(media)

    # setting video to full screen 
    player.toggle_fullscreen()
    # start playing the videosss
    player.play()
    time.sleep(9)
    player.stop()
    if(cws == 'posix'):
        os.system('clear') # If unix or linux
    else:
        os.system('cls') # If windows

except Exception as err:
    print('\n[ERROR] Failed loading media .Make sure scrT.mp4 exists in > '+os.getcwd()+' .\nDetails : ',err)
