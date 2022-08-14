import easygui as g
import sys

def passcode():
    tryy=1
    while True:
        if tryy%5!=0:
            item=('USERNAME', 'PASSCODE')
            box=g.multpasswordbox(msg='PLEASE ENTER YOUR PASSCODE',title='LOGIN',fields=item)
            print(box)
            try:
                if box[0] == 'tititi' and box[1] == '114514':
                    return 1
                    sys.exit(0)
                else:
                    g.msgbox('PASSCODE ERROR!',ok_button='TRY AGAIN')
            except:
                g.msgbox('PLEASE WRITE YOUR INFO DOWN!', ok_button='YES,I KNOW.')
            tryy+=1
        else:
            msg=('YOU HAVE TRIED %s TIMES. DO YOU WANNA CONTINUE?'%tryy)
            button=g.buttonbox(msg=msg, title='LOGIN', choices=('YES', 'NO'))
            print(button)
            if button=='NO':
                sys.exit(0)
            elif button=='YES':
                tryy+=1



    

