from Tkinter import *
import TkTreectrl as Tktree

import os
import json
from PIL import Image, ImageTk
from string import *
import emoji
import ast
from natsort import natsorted

dirpath ="C:/vr/Beat Saber/CustomSongs"


listPlist=0
listSongs=0
value=0
pvalue=0

txtColor='white'
plistselect2=0
mlist=[]
dirs=[]
short=20
#column=[]


upordown=0

def rate(rating):

    selection=listSongs.curselection()
    print selection,rating
    #value= mlist[selection[0]][0]
    print type(rating)
    rating=str(rating)
    mlist[selection[0]][10]=rating
    print mlist[selection[0]]
    savesongs()
    init()

    
    #print value
    

    

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
    a1='{\n  "playlistTitle": "Test",\n'
    a2='  "playlistAuthor": "MRWULFF",\n'
    a3='  "songs": [\n'
    w.write(a1+a2+a3)
    
    a=[0]*len(aa)
    for b in range(len(aa)):
        a[b]=aa[b]
        t='    {"id": 1, "songName": "'+a[b]+'"},\n'
        w.write(t)
    w.write('   ]\n}')
    
       
    
    
    

def init():
    listSongs.delete(0,'end')
    
    
    #print mlist
    #print mlist[1][1]
    #print mlist[1]
    #print len(mlist)
    #for xx in (mlist):
       # print mlist
    for x in range(len(mlist)):
        #print mlist[x][1]
        #listSongs.insert(END, mlist[x][1])
        #print len(mlist[x])
        ea=''
        m=''
        h=''
        ex=''
        p=''

        
        if mlist[x][4]==True:
            ea=emoji.emojize(':heavy_check_mark:')
        if mlist[x][5]==True:
            m=emoji.emojize(':heavy_check_mark:')
        if mlist[x][6]==True:
            h=emoji.emojize(':heavy_check_mark:')
        if mlist[x][7]==True:
            ex=emoji.emojize(':heavy_check_mark:')
        if mlist[x][8]==True:
            p=emoji.emojize(':heavy_check_mark:')

        rate=''
        #print ((mlist[x][10])),'junk'
        if mlist[x][10]=='':
            (mlist[x][10])=0
        for cz in range(int(mlist[x][10])):
            #print 'stars'
            rate=rate+emoji.emojize(':star:',use_aliases=True)
        
        listSongs.insert(END,emoji.emojize(':star:',use_aliases=True),mlist[x][14],mlist[x][13],mlist[x][12],ea,m,h,ex,p,mlist[x][9],rate)



    

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
    
    for x in os.listdir(dirpath):
        dirs.append(x)
    sl=dirs
    print sl
    #print sl
    for c in range(len(sl)):
        
        value=sl[c]
        if value!='.cache':
            if value!='playlist.json':
        
                diffE=False
                diffN=False
                diffH=False
                diffX=False
                diffP=False
                
                if 1==1:
                    a=dirpath+"/"+value+"/info.json"
                    print a
                    input_file  = file(a, "r")
                    j = json.loads(input_file.read())
                    #print j["songSubName"]
                    #print j
                    environmentName=j['environmentName']
                    difficultyLevels=j['difficultyLevels']
                    diff=difficultyLevels
                    ddd=''
                        
                    '''
                    for aa in range(len(difficultyLevels)):
                        #print aa
                        #print type(aa)
                        for key, value2 in aa.iteritems() :
                            print diff
                            print key,value2,'fuckoff22'
                    '''
                    #print diff
                    for i in range(len(diff)):
                        #print diff[i]
                        test2=diff[i]
                        di= test2['difficulty']
                        #print di
                        if di=='Normal':
                            diffN=True
                        if di=='Easy':
                            diffE=True
                        if di=='Hard':
                        

                            diffH=True
                        if di=="Expert":
                            diffX=True
                        if di=="ExpertPlus":
                            diffP=True
                            #print test2
                            #teest=raw_input('fuck')
                        
                        
                            #print diffE,diffN,diffH,diffX,diffP

                    
                    
                    authorName=j['authorName']
                    authorNameS=authorName
                    if len(authorName)>short:
                        authorNameS=authorNameS[:short]+'...'
                        #print authorNameS
                    
                    
                    songsubname=j['songSubName']

                    songsubnameS=songsubname
                    if len(songsubname)>short:
                        songsubnameS=songsubnameS[:short]+'...'
                        #print songsubnameS

                    songName=j['songName']
                    songNameS=songName
                    if len(songNameS)>short:
                        songNameS=songNameS[:short]+'...'
                       # print songNameS






                    
                    bpm=j['beatsPerMinute']
                    #bpm,junk2=bpm(split,'.')
                    
                    try:
                        bpm=str(bpm)
                        bpm,junk=split(bpm,'.')
                    except:
                        ''
                    
                    thumb=j['coverImagePath']
                    ###extra 0 for future content
                    songdetails=[value,songName,songsubname,authorName,diffE,diffN,diffH,diffX,diffP,str(bpm),'',environmentName,authorNameS,songsubnameS,songNameS,thumb,'',0,0,0,0,0,]
                    mlist.append(songdetails)
                    #print songdetails

            #except:
            #    print value
#                 songdetails=[0,0,0,0,0,0,0,0]
#            """
#    return mlist
    
def OnDouble(event):
    global value
    widget = event.widget
    selection=widget.curselection()
    value= mlist[selection[0]][0]
    value55 = widget.get(selection[0])
    print value55
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
    #print thumb
    try:
        image = Image.open(dirpath+'/'+value+'/'+thumb)
    except:
        image = Image.open(dirpath+'/'+value+'/'+thumb+'.jpg')
        print "error: invalid image(double.jpg in "+value

    image=image.resize((250,250))

    photo = ImageTk.PhotoImage(image)
    


    #print songName,thumb,bpm,songsubname,authorName,environmentName

    #return songName,thumb,bpm,songsubname,authorName,environmentName
    offs=1
    
    Label(justify='right',anchor='w',bg=txtColor,text=songName,font=(12)).grid(       row=offs+3,column=1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7)
    Label(justify='left',anchor='w',bg=txtColor,text=songsubname,font=(12)).grid(     row=offs+4,column=1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7)
    Label(justify='left',anchor='w',bg=txtColor,text=authorName,font=(12)).grid(      row=offs+5,column=1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7)
    Label(justify='left',anchor='w',bg=txtColor,text=songName,font=(12)).grid(        row=offs+7,column=1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7)
    Label(justify='left',anchor='nw',bg=txtColor,text=environmentName,font=(12)).grid(row=offs+8,column=1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7)
    Label(justify='left',anchor='nw',bg=txtColor,text=bpm,font=(12)).grid(            row=offs+9,column=1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7)


    Label(justify='left',anchor='e',bg=txtColor,text="Title: ",font=(12)).grid(       row=offs+3,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Artist: ",font=(12)).grid(      row=offs+4,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Mapper: ",font=(12)).grid(      row=offs+5,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Difficulties: ",font=(12)).grid(row=offs+6,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="ID: ",font=(12)).grid(          row=offs+7,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Graphics: ",font=(12)).grid(    row=offs+8,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="BPM: ",font=(12)).grid(         row=offs+9,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="HighScore: ",font=(12)).grid(  row=offs+10,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Rating: ",font=(12)).grid(     row=offs+11,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Comment: ",font=(12)).grid(    row=offs+12,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Categories : ",font=(12)).grid(row=offs+13,column=0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)




    
    #print diff
    for bb in difficultyLevels:
        #print bb
        #print type(bb)
        ddd= bb['difficulty']+' '+ddd
        


    label = Label(image=photo)
    label.image=photo
    label.grid(row=3,column=8,rowspan=9,columnspan=4,sticky="N"+"W")
    Label(justify='left',anchor='w',bg=txtColor,text=ddd,font=(12)).grid(row=offs+6,column=1,columnspan=7,ipadx=100,sticky='W'+'E'+'S'+'N')

def Sort():
    print "sort"
def savesongs():
    dd=open('localsongs.txt','w')
    dd.write(str(mlist))
    dd.close()

def opensongs():
    global mlist
    dd=open('localsongs.txt','r')
    for line in dd.readlines():
        #print len(line)
        line=ast.literal_eval(line)
        #print len(line)
        #print type(line[1])
        mlist=line
def sortS(sort):
    global upordown
    global listSongs

    #print upordown
    upordown=upordown+1
    #print sort,'fuck'

    for z in range(11):
        listSongs.column_configure(z,arrow='none')
    
    

    way=True
    listSongs.column_configure(sort,arrow='down')
    global mlist
    if upordown%2==0:
        way=False
        listSongs.column_configure(sort,arrow='up')
        
    #mlist=natsorted(mlist,key=lambda l:l[sort], reverse=way)
    mlist=sorted(mlist,key=lambda l:l[sort], reverse=way)
    #mlist=natsorted(mlist)
    init()
    way=way+1
    print way,' in sort'
    #for a in range(len(mlist)):
        #print mlist[a][10]

        
    return way
    
    

def main():
    global listPlist
    global listSongs
    global plistselect2
    global aaa
    global mlist
    global column
    footer=10
    #rightedge=4
    global dirs


        
    root = Tk()
    root.bg='black'

    global bpmsort



    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=12)
    filemenu.add_command(label="Open", command=add)
    filemenu.add_command(label="Save", command=save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Local Songs", command=init)
    filemenu.add_command(label="BeatSaberDB", command=save)
    filemenu.add_command(label="BsaberDB", command=save)

    menubar.add_cascade(label="Update", menu=filemenu)


    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Local Songs DB", command=savesongs)
    filemenu.add_command(label="Current Playlist", command=save)
    filemenu.add_command(label="Favorites", command=save)

    menubar.add_cascade(label="Export", menu=filemenu)


    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Local Songs DB", command=opensongs)
    filemenu.add_command(label="Current Playlist", command=save)
    filemenu.add_command(label="Favorites", command=save)

    menubar.add_cascade(label="Export", menu=filemenu)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Song", command=lambda: sortS(1))
    filemenu.add_command(label="Artist", command=lambda: sortS(2))
    filemenu.add_command(label="Mapper", command=lambda: sortS(3))
    filemenu.add_command(label="Starred", command=lambda: sortS(4))
    filemenu.add_command(label="Rating", command=lambda: sortS(10))
    filemenu.add_command(label="Score", command=lambda: sortS(6))
    bpmsort= filemenu.add_command(label="BPM", command=lambda: sortS(9))

    filemenu.add_separator()
    filemenu.add_command(label="Easy", command=lambda: sortS(4))
    filemenu.add_command(label="Normal", command=lambda: sortS(5))
    filemenu.add_command(label="Hard", command=lambda: sortS(6))
    filemenu.add_command(label="Expert", command=lambda: sortS(7))
    filemenu.add_command(label="Expert+", command=lambda: sortS(8))

    
     
    print "TEST"

    menubar.add_cascade(label="Sort", menu=filemenu)

    

    
    root.config(menu=menubar)







    Label(text="All Songs",font=(20)).grid(row=0,column=0,columnspan=7)
    Label(text="Playlist",font=(20)).grid(row=0,column=8,columnspan=4)






    #listInfo = Listbox(frameI, width=30, height=20, font=("Helvetica", 12))
    #listInfo.grid(row=1,column=0)





    #print emoji.emojize(use_aliases=True)
    listPlist = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listPlist.grid(row=1,column=8,columnspan=4)
    listPlist.bind("<Double-Button-1>", OnDouble)



    #listSongs = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listSongs = Tktree.MultiListbox(root, width=1200,height=400,font=("Helvetica", 12))
    listSongs.grid(row=1,column=0,rowspan=1,columnspan=8)
    #listSongs.config(columns=('Directory', 'Song Name','songSubname','authorName','difficlty','bpm','rating','highscore','date'))
    print emoji.emojize('Python is :thumbs_up:')
    listSongs.config(columns=(emoji.emojize(':star:',use_aliases=True),'Song Name', 'Artist Name','Mapper?!','E','N','H','X','P','BPM','Rating'))
    listSongs.column_configure(1,arrow='down')
    listSongs.bind("<Double-Button-1>", OnDouble)
    #listSongs.bind("<Double-Button-1>", add)

    ##############songdetails=[value,songName,songsubname,authorName,diff,bpm,thumb,environmentName]






    

    #w = Canvas(root, width=400, height=380,bg="white")
    #w.create_rectangle(50, 25, 150, 75, fill="white")
    #w.create_text(10,20,anchor='nw',justify='left',fill="black",font="Helvetica 12 ", width=400,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quis arcu volutpat arcu malesuada imperdiet quis id sem. Nunc ornare sapien in ante bibendum, quis blandit ante semper. Nullam ante arcu, semper nec suscipit vitae, vehicula sit amet felis. Nulla facilisi. Aenean interdum vel ante sed facilisis. Sed interdum pretium gravida. Suspendisse suscipit id turpis quis elementum. Nunc dapibus in justo a gravida. Aliquam ullamcorper nibh non leo posu.")
    #w.grid(row=1,column=1,columnspan=1)



    addsongbutton = Button(root, text="Add to Playlist", command=add).grid(row=2,column=0)


    
    addallsongbutton = Button(root, text="Add All to Playlist", command=addall).grid(row=8,column=0)






    removesongbutton = Button(root, text="RemoveSelected", command=lambda listPlist=listPlist: listPlist.delete(ANCHOR)).grid(row=2,column=8,)
    moveup = Button(root, text="Move up", command=move_up).grid(row=2,column=9,)
    movedown = Button(root, text="Move down", command=move_down).grid(row=2,column=10,)
    removesongbutton2 = Button(root, text="Remove All", command=remove).grid(row=2,column=11)








    #b = Button(master, text="Delete",command=lambda lb=lb: lb.delete(ANCHOR))

    plistselect2=listPlist.get(ANCHOR)


    

    Label(text="Rating:",anchor="e").grid(row=2,column=1,sticky='W'+'E'+'S'+'N')

    #ratebutton = Button(root, text="0", command=remove).grid(row=2,column=1,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="1", command=lambda: rate(1)).grid(row=2,column=2,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="2", command=lambda: rate(2)).grid(row=2,column=3,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="3", command=lambda: rate(3)).grid(row=2,column=4,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="4", command=lambda: rate(4)).grid(row=2,column=5,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="5", command=lambda: rate(5)).grid(row=2,column=6,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text=emoji.emojize(':star:',use_aliases=True), command=lambda: rate(6)).grid(row=2,column=7,sticky='W'+'E'+'S'+'N')






    try:
        opensongs()
    except:
        print 'error loading db. scanning dirs...'
        firstload()
        print 'wtf'
    init()


    mainloop()
main()
