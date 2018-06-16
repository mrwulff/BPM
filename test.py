from Tkinter import *
import os
import json
from PIL import Image, ImageTk


dirpath ="E:/Steam/steamapps/common/Beat Saber/CustomSongs"


listPlist=0

value=0

txtColor='white'

def add():
    global value
    global listPlist

    print value
    listPlist.insert(END, value)
def remove():
    print 'remove'
def addall():
    print 'addall'

def OnDouble(event):
    global value
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    #print "selection:", selection, ": '%s'" % value
    a=dirpath+"/"+value+"/info.json"
    #print a
    input_file  = file(a, "r")
    j = json.loads(input_file.read())
    #print j["songSubName"]
    #print j
    environmentName=j['environmentName']
    difficultyLevels=j['difficultyLevels']
    diff=difficultyLevels
    ddd=''
        
    '''
    for aa in difficultyLevels:
        print aa
        print type(aa)
        for key, value in aa.iteritems() :
            print key,value
    '''
    authorName=j['authorName']
    songsubname=j['songSubName']
    bpm=j['beatsPerMinute']
    songName=j['songName']
    thumb=j['coverImagePath']


    image = Image.open(dirpath+'/'+value+'/'+thumb)
    image=image.resize((250,250))

    photo = ImageTk.PhotoImage(image)
    


    #print songName,thumb,bpm,songsubname,authorName,environmentName

    #return songName,thumb,bpm,songsubname,authorName,environmentName
    Label(justify='right',anchor='w',bg=txtColor,text=songName,font=(12)).grid(row=3,column=1,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='w',bg=txtColor,text=songsubname,font=(12)).grid(row=4,column=1,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='w',bg=txtColor,text=authorName,font=(12)).grid(row=5,column=1,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='w',bg=txtColor,text=songName,font=(12)).grid(row=7,column=1,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='nw',bg=txtColor,text=environmentName,font=(12)).grid(row=8,column=1,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='nw',bg=txtColor,text=bpm,font=(12)).grid(row=9,column=1,ipadx=100,sticky='W'+'E'+'S'+'N')


    Label(justify='left',anchor='e',bg=txtColor,text="Title: ",font=(12)).grid(row=3,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="Artist: ",font=(12)).grid(row=4,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="Mapper: ",font=(12)).grid(row=5,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="Difficulties: ",font=(12)).grid(row=6,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="ID: ",font=(12)).grid(row=7,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="Graphics: ",font=(12)).grid(row=8,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="BPM: ",font=(12)).grid(row=9,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="HighScore: ",font=(12)).grid(row=10,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="Rating: ",font=(12)).grid(row=11,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="Comment: ",font=(12)).grid(row=12,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')
    Label(justify='left',anchor='e',bg=txtColor,text="Categories : ",font=(12)).grid(row=13,column=0,ipadx=100,sticky='W'+'E'+'S'+'N')





    
    print diff
    for bb in difficultyLevels:
        print bb
        print type(bb)
        ddd= bb['difficulty']+' '+ddd
        


    label = Label(image=photo)
    label.image=photo
    label.grid(row=3,column=2,rowspan=9,sticky="N"+"W")
    Label(justify='left',anchor='w',bg=txtColor,text=ddd,font=(12)).grid(row=6,column=1,ipadx=100,sticky='W'+'E'+'S'+'N')



def main():
    global listPlist
    footer=10
    #rightedge=4


        
    root = Tk()
    root.bg='black'




    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=add)
    filemenu.add_command(label="Save", command=add)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)







    Label(text="All Songs",font=(20)).grid(row=0,column=0)
    Label(text="Playlist",font=(20)).grid(row=0,column=2)






    #listInfo = Listbox(frameI, width=30, height=20, font=("Helvetica", 12))
    #listInfo.grid(row=1,column=0)






    listPlist = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listPlist.grid(row=1,column=2,rowspan=1)


    listSongs = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listSongs.grid(row=1,column=0,rowspan=1)
    listSongs.bind("<Double-Button-1>", OnDouble)





    

    w = Canvas(root, width=400, height=380,bg="white")
    #w.create_rectangle(50, 25, 150, 75, fill="white")
    w.create_text(10,20,anchor='nw',justify='left',fill="black",font="Helvetica 12 ", width=400,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quis arcu volutpat arcu malesuada imperdiet quis id sem. Nunc ornare sapien in ante bibendum, quis blandit ante semper. Nullam ante arcu, semper nec suscipit vitae, vehicula sit amet felis. Nulla facilisi. Aenean interdum vel ante sed facilisis. Sed interdum pretium gravida. Suspendisse suscipit id turpis quis elementum. Nunc dapibus in justo a gravida. Aliquam ullamcorper nibh non leo posu.")
    w.grid(row=1,column=1,rowspan=1)





    addsongbutton = Button(root, text="Add to Playlist", command=add).grid(row=2,column=0)
    addallsongbutton = Button(root, text="Add All to Playlist", command=addall).grid(row=8,column=0)


    removesongbutton = Button(root, text="RemoveSelected", command=remove).grid(row=2,column=2,)
    removesongbutton2 = Button(root, text="Remove All", command=remove).grid(row=8,column=2)

    ratebutton = Button(root, text="Rate", command=remove).grid(row=2,column=1)











    for x in os.listdir(dirpath):
        listSongs.insert(END, str(x))
    #widget=event.widget
    #selection=widget.curselection()




    mainloop()
main()
