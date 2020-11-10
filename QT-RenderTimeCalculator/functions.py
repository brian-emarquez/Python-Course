from datetime import datetime, timedelta
import time
import os
os.system("cls")

print("\u001b[36m###########################################################")
print("## RENDER TIME CALCULATOR                                ##")
print("###########################################################")
print("\u001b[32mDigite abaixo o tempo de render por frame:")
getHours = input("\u001b[36m Horas: \u001b[37m")
getMinutes = input("\u001b[36m Minutos: \u001b[37m")
getSeconds = input("\u001b[36m Segundos: \u001b[37m")
getNumFrame = input("\u001b[36m Quantidade de frames: \u001b[37m")
getNumMachines = input("\u001b[36m Quantidade de máquinas: \u001b[37m")

timeNow = datetime.today()

frameTime = timedelta(hours=int(getHours), minutes=int(getMinutes), seconds=int(getSeconds))
mathDateEnd = timeNow + (frameTime * int(getNumFrame) / int(getNumMachines))
totalTime = mathDateEnd - timeNow
splitTime = str(totalTime).split(':')
days = splitTime[0].replace(' days,', 'd').replace(' day,', 'd')
strRenderRime =  days + 'h ' + splitTime[1] + 'm ' + splitTime[2] + 's'


strDayEnd = ' \u001b[36mTerminará no dia \u001b[37m' + str(mathDateEnd.day) + '  \u001b[36mas \u001b[37m' + str(mathDateEnd.hour) + '  \u001b[36mhoras, \u001b[37m' + str(mathDateEnd.minute) + '  \u001b[36mminutos e \u001b[37m' + str(mathDateEnd.second) + '  \u001b[36msegundos!'

print("\u001b[36m###########################################################")
print("\u001b[32mRESULTADO:")
print('\u001b[36mTEMPO TOTAL:\u001b[37m' + strRenderRime)
print('\u001b[36mDATA DE TÉRMINO:\u001b[32m', strDayEnd, '\u001b[37m')
