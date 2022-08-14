import sys
import passcode as p
import easygui as g
import time as t
dic={}

dicc={}

ti=t.perf_counter()
with open('wordsSpace.txt', 'r', encoding='UTF-8') as listt:
    ram = listt.readlines()
for i in range(len(ram)-1):
        ramm=ram[i].split('#')
        dic[ramm[1]]={'no.':ramm[0],'ch':ramm[2]}
for i in range(len(ram)-1):
        rammm = ram[i].split('#')
        dicc[rammm[2]] = {'no.': rammm[0], 'ch': rammm[1]}
tii=t.perf_counter()

tt=(tii-ti,'s')
tstr='PLEASE ENTER WORD YOUR WANT (',tt,' for load)' 

if p.passcode()==1:
    while True:
        ti=0
        tii=0
        item=('EN:', 'CH:')
        box=g.multenterbox(msg=tstr,title='FIND WORD',fields=item)
        print(box)
        tstr=''
        if box[1]=='':    
            try:
            
                
                cc = g.ccbox(msg=dic[box[0]], title='trans', choices=('C[o]ntinue', 'C[a]ncel'), default_choice='C[o]ntinue', cancel_choice='C[a]ncel')
                print(cc)
                if cc==False:
                    sys.exit(0)
                    
            except:
                g.msgbox('404 not found.', ok_button='YES,I KNOW.')
            tstr=''
        elif box[0]=='':
            try:
                
                cc = g.ccbox(msg=dicc[box[1]],title='trans', choices=('C[o]ntinue', 'C[a]ncel'), default_choice='C[o]ntinue', cancel_choice='C[a]ncel')
                print(cc)
                if cc==False:
                    sys.exit(0)
            except:
                g.msgbox('404 not found.', ok_button='YES,I KNOW.')
        elif box[0]!=''and box[1] !='':
            g.msgbox('PLEASE WAITE ONE ITEM DOWN ONLY.', ok_button='YES,I KNOW.')
        elif box[0]== '' and box[1]== '':
            g.msgbox('PLEASE WAITE ONE ITEM DOWN.', ok_button='YES,I KNOW.')
