import mido
import tkinter as tk
from tkinter import filedialog
def write(event):
    global usecond_per_tick
    note_list = {48:'Z',50:'X',52:'C',53:'V',55:'B',57:'N',59:'M',\
                 60:'A',62:'S',64:'D',65:'F',67:'G',69:'H',71:'J',\
                 72:'Q',74:'W',76:'E',77:'R',79:'T',81:'Y',83:'U'}
    keyName = note_list[event.note]
    delay_time = round(event.time*usecond_per_tick,2)
    with open("output1.txt",'a+') as f:
        if(delay_time != 0.0):
            f.write('Delay '+str(delay_time)+'\n')
        if(event.type == 'note_on'):
            f.write('KeyDown "'+str(keyName)+'", 1\n'+'KeyUp "'+str(keyName)+'", 1\n')

def main():
    window = tk.Tk()
    window.withdraw()
    path = filedialog.askopenfilename()
    mid = mido.MidiFile(path)
    ticks_per_beat = mid.ticks_per_beat#每一拍的ticks

    for track in mid.tracks:#tempo 每一拍的微秒数
        for event in track:
            if(event.type == "set_tempo" ):
                tempo = event.tempo
                global usecond_per_tick
                usecond_per_tick = tempo/ticks_per_beat/1000
            if(event.type == "note_on" or event.type == "note_off"):
                print(event)
                write(event)
    print("Done!")
main()
