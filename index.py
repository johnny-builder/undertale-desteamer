#
#   Undertale De-Steamer
#
#   Brought to you by:
#   johnny-builder (aka dance2)
#

#   Set this to true if you are unsure, after that, set it to False
autoUpdate = False



#! If you are unsure, do not touch the code after this.
#! I cannot be responsible for problems in modified versions of this code.
#* If you are looking for typos, please do not hesitate to tell me the ones that you find.
#? ;)
#? And yes i do like blue.

import os

print("")
print("Undertale De-Steamer")
print("")
print("Brought to you by:")
print("johnny-builder (aka dance2)")
print("")

if autoUpdate == True:
    print("Updating required packages...")
    print("Please set autoUpdate to False after the installation of the packages")
    print("")
    os.system("pip install PySimpleGui")
    print("Finished installing packages")
else:
    import PySimpleGUI as gui
    gui.theme('SystemDefault1')
    mainlayout = [
        [gui.Text('Undertale De-Steamer')],
        [gui.Text('Type in your Undertale directory below:')],
        [gui.InputText()],
        [gui.Button('De-Steam!!'), gui.Button('Close')]
    ]
    window = gui.Window('Undertale De-Steamer', mainlayout)
    while True:
        event, dir = window.read()
        if event == gui.WIN_CLOSED or event == 'Close':
            break
        elif event == 'De-Steam!!':
            confirmlayout = [
                [gui.Text('Are you sure you want to De-Steam??')],
                [gui.Text('Selected directory: ' + dir[0])],
                [gui.Button('De-Steam!!!'), gui.Button('No')]
            ]
            confirmwin = gui.Window('Undertale De-Steamer', confirmlayout)
            window.close()
            break
        #print('Selected Undertale directory: ', values[0])
    while True:
        event, values = confirmwin.read()
        if event == gui.WIN_CLOSED or event == 'No':
            break
        elif event == 'De-Steam!!!':
            if os.path.exists(dir[0]):
                window.close()
                if os.path.isfile(str(dir[0]) + "\\steam_api.dll") and os.path.isfile(str(dir[0]) + "\\steam_appid.txt"):
                    print("Patching...")
                    os.rename(dir[0] + "\\steam_api.dll", dir[0] + "\\steam_api.dll.bkp")
                    os.rename(dir[0] + "\\steam_appid.txt", dir[0] + "\\steam_appid.txt.bkp")
                    print("Patched!!")
            else:
                print("Invalid Directory")
                break
    window.close()