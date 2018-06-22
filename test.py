from Tkinter import *
import os
import json
from PIL import Image, ImageTk


dirpath ="E:/steam/Beat Saber/CustomSongs"


listPlist=0
listSongs=0
value=0
pvalue=0

txtColor='white'
plistselect2=0
mlist=[]
dirs=[]

def savej():
    global listPlist
    print listPlist
    print 'fuckoff'
    aa= listPlist.get(0, END)
    song={}
    print type(song)
    print aa
    
    

    d = {"playlistTitle":"KEVIN TEST 111"}
    #d.update={"playlistAuthor":"KEVIN"}
    d['playlistAutor']='KEVIN'
    #d.update={"songs":'TEST'}
    


    
    with open('data.txt', 'w') as outfile:
        json.dump(d, outfile)

def save():
    global dirpath
    dd=dirpath+'/'+'playlist.json'
    print dd
    w=open(dd,'w')
    
    
    aa= listPlist.get(0, END)
    a1='{\n  "playlistTitle": "Stars Picks",\n'
    a2='  "playlistAuthor": "StarGazer1258",\n'
    a3='  "songs": [\n'
    w.write(a1+a2+a3)
    
    a=[0]*len(aa)
    for b in range(len(aa)):
        a[b]=aa[b]
        t='    {"id": 221, "songName": "'+a[b]+'"},\n'
        w.write(t)
    w.write('   ]\n}')
    
       
    
    
    



    

def add():
    global value
    global listPlist

    print value
    listPlist.insert(END, value)
def remove():
    global listPlist
    listPlist.delete(0, END)
def addall():
    print 'addall'
def move_down():





    
    global plistselect2
    global listPlist
    global aaa
    pos= listPlist.curselection()

    print listPlist.size()
    
    pos=pos[0]
    print pos


    if pos >= listPlist.size()-1:
        print "End of List"
        return

    text = listPlist.get(pos)
    listPlist.delete(pos)
    listPlist.insert(pos+1, text)
    listPlist.select_set(pos+1)

    print listPlist
    

def move_up():




    
    global plistselect2
    global listPlist
    global aaa
    pos= listPlist.curselection()
    
    pos=pos[0]


    if pos == 0:
        return

    text = listPlist.get(pos)
    listPlist.delete(pos)
    listPlist.insert(pos-1, text)
    listPlist.select_set(pos-1)

    print listPlist
    
def firstload():
    global mlist
    #print mlist

    sl=dirs
    #print sl
    for c in range(len(sl)):
        
        #print sl[c]
        value=sl[c]
        if value!='.cache' or  value!='playlist.json':
            
            try:
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
                songdetails=[value,songName,songsubname,authorName,diff,bpm,thumb,environmentName]
                mlist.append(songdetails)
                #print songdetails

            except:
                print value
#                 songdetails=[0,0,0,0,0,0,0,0]
#            """
#    return mlist
    
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





    
    #print diff
    for bb in difficultyLevels:
        #print bb
        #print type(bb)
        ddd= bb['difficulty']+' '+ddd
        


    label = Label(image=photo)
    label.image=photo
    label.grid(row=3,column=2,rowspan=9,columnspan=4,sticky="N"+"W")
    Label(justify='left',anchor='w',bg=txtColor,text=ddd,font=(12)).grid(row=6,column=1,columnspan=1,ipadx=100,sticky='W'+'E'+'S'+'N')



def main():
    global listPlist
    global listSongs
    global plistselect2
    global aaa
    global mlist
    footer=10
    #rightedge=4
    global dirs


        
    root = Tk()
    root.bg='black'




    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=add)
    filemenu.add_command(label="Save", command=save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)







    Label(text="All Songs",font=(20)).grid(row=0,column=0)
    Label(text="Playlist",font=(20)).grid(row=0,column=2,columnspan=2)






    #listInfo = Listbox(frameI, width=30, height=20, font=("Helvetica", 12))
    #listInfo.grid(row=1,column=0)






    listPlist = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listPlist.grid(row=1,column=2,columnspan=4)
    listPlist.bind("<Double-Button-1>", OnDouble)



    listSongs = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listSongs.grid(row=1,column=0,rowspan=1)
    listSongs.bind("<Double-Button-1>", OnDouble)





    

    w = Canvas(root, width=400, height=380,bg="white")
    #w.create_rectangle(50, 25, 150, 75, fill="white")
    w.create_text(10,20,anchor='nw',justify='left',fill="black",font="Helvetica 12 ", width=400,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quis arcu volutpat arcu malesuada imperdiet quis id sem. Nunc ornare sapien in ante bibendum, quis blandit ante semper. Nullam ante arcu, semper nec suscipit vitae, vehicula sit amet felis. Nulla facilisi. Aenean interdum vel ante sed facilisis. Sed interdum pretium gravida. Suspendisse suscipit id turpis quis elementum. Nunc dapibus in justo a gravida. Aliquam ullamcorper nibh non leo posu.")
    w.grid(row=1,column=1,columnspan=1)





    addsongbutton = Button(root, text="Add to Playlist", command=add).grid(row=2,column=0)


    
    addallsongbutton = Button(root, text="Add All to Playlist", command=addall).grid(row=8,column=0)


    removesongbutton = Button(root, text="RemoveSelected", command=lambda listPlist=listPlist: listPlist.delete(ANCHOR)).grid(row=2,column=2,)

    #b = Button(master, text="Delete",command=lambda lb=lb: lb.delete(ANCHOR))
    print plistselect2
    print 
    plistselect2=listPlist.get(ANCHOR)


    
    moveup = Button(root, text="Move up", command=move_up).grid(row=2,column=4,)

    
    movedown = Button(root, text="Move down", command=move_down).grid(row=2,column=5,)
    removesongbutton2 = Button(root, text="Remove All", command=remove).grid(row=2,column=3)

    


    ratebutton = Button(root, text="Rate", command=remove).grid(row=2,column=1)







    for x in os.listdir(dirpath):
        dirs.append(x)
    #print dirs

    firstload()
    
    #print mlist
    #print mlist[1][1]
    print mlist[1]
    print len(mlist)
    #for xx in (mlist):
       # print mlist
    for x in range(len(mlist)):
        print mlist[x][1]
        listSongs.insert(END, mlist[x][1])


##############songdetails=[value,songName,songsubname,authorName,diff,bpm,thumb,environmentName]
        
    #    print mlist[x][1]
        #listSongs.insert(END,mlist[xx][1])

    #    listSongs.insert(END,mlist[x][1])
    #for x in os.listdir(dirpath):
    #    listSongs.insert(END, str(x))
    
    #widget=event.widget
    #selection=widget.curselection()




    mainloop()
main()
