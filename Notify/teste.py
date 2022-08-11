import time
import os
import sys
from winotify import Notification, audio
sys.platform = 'win32'

def callbackfunc():
     return os.startfile('mstsc.exe')


toast = Notification(app_id="Notificação",
                     title="Notificação de Backup",
                     msg="Faça o Backup vagabundo!",
                     icon=r"C:\Users\HSVP\Downloads\Iconsmind-Outline-Data-Backup.ico",
                     duration="long",
                     launch='callbackfunc()')

toast.set_audio(audio.LoopingAlarm, loop=True)

toast.add_actions(label="Click Me!")


toast.build().show()

