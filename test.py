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


upordown=1
debug=5
lastselected=0


def rate(rating):

    selection=listSongs.curselection()
    if debug>0:
        print selection,rating ,' Song selection and rating'
    rating=str(rating)
    mlist[selection[0]][10]=rating
    mlist[selection[0]][17]=1
    export_extra_data()
    savesongs()
    init()


    
'''
def savejk():
    

    
    global listPlist

    if debug>1:
        print 'savej'
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
'''


def save():
    global dirpath
    dd=dirpath+'/'+'playlist.json'
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
    Label(text="All Songs "+str(len(mlist)),font=(20)).grid(row=0,column=0,columnspan=7)

    print 'running init with',len(mlist),' songs'
    listSongs.delete(0,'end')
    print 'running ini2 with',len(mlist),' songs'
    
    odd=0
    tag="odd"

    for x in range(len(mlist)):
        odd=odd+1

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
        if mlist[x][10]=='':
            (mlist[x][10])=0
        for cz in range(int(mlist[x][10])):
            rate=rate+emoji.emojize(':star:',use_aliases=True)
        
        listSongs.insert(END,emoji.emojize(':star:',use_aliases=True),mlist[x][14],mlist[x][13],mlist[x][12],ea,m,h,ex,p,mlist[x][9],rate,)
        
        tag = "even" if tag == "odd" else "odd"
        '''
        if odd%2==0:
            listSongs.configure(itembackground="#e0e0e0")
            print odd
        if odd%2==1:
            listSongs.configure(itembackground="white")
            print odd
        '''
            
        



    

def add():
    cc=listSongs.curselection()
    print cc
    global value
    global listPlist

    print value
    for a in range(len(cc)):
        
        listPlist.insert(END, mlist[cc[a]][1])
    listSongs.selection_clear(0, END)

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

    
    pos=pos[0]


    if pos >= listPlist.size()-1:
        print "End of List"
        return

    text = listPlist.get(pos)
    listPlist.delete(pos)
    listPlist.insert(pos+1, text)
    listPlist.select_set(pos+1)

    

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

def loadinfojson(input_file,value):
    global listsongs
    global mlist
    j = json.loads(input_file.read())
    

    #print j["songSubName"]
    #print j
    environmentName=j['environmentName']
    difficultyLevels=j['difficultyLevels']
    diff=difficultyLevels
    ddd=''
        
    diffE=False
    diffN=False
    diffH=False
    diffX=False
    diffP=False
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
    #17=updated?
    mlist.append(songdetails)
    #print songdetails
def loadxinfo(j,value):
    print value,'VALUE'

    
    '''
    aa=aa+'    "SongName": "'+mlist[a][1]+'",\n'
    aa=aa+'    "ArtistName": "'+mlist[a][3]+'",\n'
    aa=aa+'    "Mapper": "'+mlist[a][2]+'",\n'
    aa=aa+'    "Directory": "'+mlist[a][0]+'",\n'
    aa=aa+'    "Easy?": "'+str(mlist[a][4])+'",\n'
    aa=aa+'    "Normal": "'+str(mlist[a][5])+'",\n'
    aa=aa+'    "Hard": "'+str(mlist[a][6])+'",\n'
    aa=aa+'    "Expert": "'+str(mlist[a][7])+'",\n'
    aa=aa+'    "Expert+": "'+str(mlist[a][8])+'",\n'
    aa=aa+'    "BPM": '+mlist[a][9]+',\n'
    aa=aa+'    "User Rating": '+mlist[a][10]+',\n'
    aa=aa+'    "Enviroment": "'+mlist[a][11]+'",\n'
    aa=aa+'    "Short Artist": "'+mlist[a][12]+'",\n'
    aa=aa+'    "Short Song": "'+mlist[a][13]+'",\n'
    aa=aa+'    "Short Mapper": "'+mlist[a][14]+'",\n'
    aa=aa+'    "Thumbnail": "'+mlist[a][15]+'",\n'
    aa=aa+'    "BeatSaverID (FUTURE)": "'+mlist[a][16]+'",\n'
    aa=aa+'    "Comments(FUTURE)": "'+str(mlist[a][17])+'",\n'
    aa=aa+'    "Genere(FURURE)": "'+str(mlist[a][18])+'",\n'
    aa=aa+'    "Uploaded(FUTURE)": "'+str(mlist[a][19])+'",\n'
    aa=aa+'    "Downloaded(FUTURE)": "'+str(mlist[a][20])+'"\n}'
    '''
    



    
    #print j,value,' inputfile and value of loadx'

    global listsongs
    global mlist
    
    newa=j["Directory"],j["SongName"],j["Mapper"],j["ArtistName"],sb(j["Easy?"]),sb(j["Normal"]),sb(j["Hard"]),sb(j["Expert"]),sb(j["Expert+"]),j["BPM"],j["User Rating"],j["Enviroment"],j["Short Artist"],j["Short Song"],j["Short Mapper"],j["Thumbnail"],j["BeatSaverID"],j["Comments"],j["Genere"],
    j["Uploaded"],j["Downloaded"]
    mlist.append(newa)
    print type(j["Hard"]),'jhard#######'
    
    
def sb(v):
  return v.lower() in ("yes", "true", "t", "1")   

def firstload():
    global listSongs
    global mlist
    listSongs.delete(0,'end')
    mlist=[]
    dirs=[]
    for x in os.listdir(dirpath):
        dirs.append(x)
    sl=[]
    sl=dirs
    xdata=0
    for c in range(len(sl)):
        has_extra_data=False
        
        value=sl[c]
        if value!='.cache':
            if value!='playlist.json':
        
                
                
                if 1==1:
                    a=dirpath+"/"+value+"/info.json"
                    a_extra=dirpath+"/"+value+"/einfo.json"
                    input_file  = file(a, "r")
                    try:
                        input_file2  = file(a_extra, "r")
                        j2 = json.loads(input_file2.read())
                        has_extra_data=True
                        if debug>50:
                            print 'found extra data',value
                            
                    except:
                        if debug>10:
                            print 'did not find extra data',value
                    if has_extra_data==False:
                        #load all songs without extradata
                        loadinfojson(input_file,value)
                        ""

                    if has_extra_data==True:
                        xdata=xdata+1
                        loadxinfo(j2,value)
                        ''
                        #print 'running extra data'
    if debug>3:
        print xdata, 'found songs with x data'
def OnDouble(event):
    global lastselected
    
    Label(text="All Songs "+str(len(mlist)),font=(20)).grid(row=0,column=0,columnspan=7)
    #global value
    #widget = event.widget

    selection=listSongs.curselection()
    if type(selection)==tuple:

        print selection,'tuple.'
        selection=selection[0]
    value= mlist[selection][0]

    
    #value55 = widget.get(selection[0])
    #print value55
    #print "selection:", selection, ": '%s'" % value
    #a=dirpath+"/"+value+"/info.json"
    #print a
    #input_file  = file(a, "r")
    #j = json.loads(input_file.read())
    #print j["songSubName"]
    #print j
    diff=0
    try:
        environmentName=mlist[selection][11]
    except:
        selection=selection[0]
        environmentName=mlist[selection][11]
    for i in range(4-10):
        if mlist[selection][i]:
            diff=diff+1
    ddd=diff
    print diff,'diff levels'
    

        

    #songdetails=[value,songName,songsubname,authorName,diffE,diffN,diffH,diffX,diffP,str(bpm),'',environmentName,authorNameS,songsubnameS,songNameS,thumb,'',0,0,0,0,0,]





    authorName=mlist[selection][3]
    songsubname=mlist[selection][2]
    bpm=mlist[selection][9]
    songName=mlist[selection][1]
    thumb=mlist[selection][15]
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




    '''
    #print diff
    for bb in difficultyLevels:
        #print bb
        #print type(bb)
        ddd= bb['difficulty']+' '+ddd
    '''
        


    label = Label(image=photo)
    label.image=photo
    label.grid(row=3,column=8,rowspan=9,columnspan=4,sticky="N"+"W")
    Label(justify='left',anchor='w',bg=txtColor,text=ddd,font=(12)).grid(row=offs+6,column=1,columnspan=7,ipadx=100,sticky='W'+'E'+'S'+'N')

def Sort():
    print "sort"
def savesongs():
    ###Saves mlist (all song array) to local file for caching
    dd=open('localsongs.txt','w')
    dd.write(str(mlist))
    dd.close()
    print 'saving to localcongs.txt'

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
        #print listSongs.column_configure(z, <Button-1>)

        
    
    

    way=True
    listSongs.column_configure(sort,arrow='down')
    global mlist
    if upordown%2==0:
        way=False
        listSongs.column_configure(sort,arrow='up')
        
    mlist=natsorted(mlist,key=lambda l:l[sort], reverse=way)
    #mlist=sorted(mlist,key=lambda l:l[sort], reverse=way)
    #mlist=natsorted(mlist)
    init()
    way=way+1
    print way,' in sort'
    #for a in range(len(mlist)):
        #print mlist[a][10]

        
    return way
def write_extra_data(a,val):

#songdetails=[value,songName,songsubname,authorName,diffE,diffN,diffH,diffX,diffP,str(bpm),'',environmentName,authorNameS,songsubnameS,songNameS,thumb,'',0,0,0,0,0,]
    print mlist[a]

    aa='{\n'
    aa=aa+'    "SongName": "'+mlist[a][1]+'",\n'
    aa=aa+'    "ArtistName": "'+mlist[a][3]+'",\n'
    aa=aa+'    "Mapper": "'+mlist[a][2]+'",\n'
    aa=aa+'    "Directory": "'+mlist[a][0]+'",\n'
    aa=aa+'    "Easy?": "'+str(mlist[a][4])+'",\n'
    aa=aa+'    "Normal": "'+str(mlist[a][5])+'",\n'
    aa=aa+'    "Hard": "'+str(mlist[a][6])+'",\n'
    aa=aa+'    "Expert": "'+str(mlist[a][7])+'",\n'
    aa=aa+'    "Expert+": "'+str(mlist[a][8])+'",\n'
    aa=aa+'    "BPM": '+mlist[a][9]+',\n'
    aa=aa+'    "User Rating": '+mlist[a][10]+',\n'
    aa=aa+'    "Enviroment": "'+mlist[a][11]+'",\n'
    aa=aa+'    "Short Artist": "'+mlist[a][12]+'",\n'
    aa=aa+'    "Short Song": "'+mlist[a][13]+'",\n'
    aa=aa+'    "Short Mapper": "'+mlist[a][14]+'",\n'
    aa=aa+'    "Thumbnail": "'+mlist[a][15]+'",\n'
    aa=aa+'    "BeatSaverID": "'+mlist[a][16]+'",\n'
    aa=aa+'    "Comments": "'+str(mlist[a][17])+'",\n'
    aa=aa+'    "Genere": "'+str(mlist[a][18])+'",\n'
    aa=aa+'    "Uploaded": "'+str(mlist[a][19])+'",\n'
    aa=aa+'    "Downloaded": "'+str(mlist[a][20])+'"\n}'
    
    w=open(dirpath+"/"+mlist[a][0]+"/einfo.json",'w')
    w.write(aa)
    if debug>3:
        print aa, 'extra json output'
        print 'wrote '+mlist[a][1]


    
    
def export_extra_data():
    updating=0
    if debug>1:
        print "exporting extra data"
    for a in range(len(mlist)):
        #print mlist[a][17]
        
        if mlist[a][17]==1:
            if debug>0:
                print mlist[a][10],"found an update",mlist[a][1]
            write_extra_data(a,10)
            
    print updating, ' Songs have updates'
def clear_data():
    listSongs.delete(0,'end')
def Test(event):
    widget = event.widget
    print widget
    selection=widget.curselection()
    print selection

def nice(event):
    print 'nice'
    try:
        OnDouble(event[0])
    except:
        OnDouble(event)
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
    filemenu.add_command(label="Extra_Data", command=export_extra_data)
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

    menubar.add_cascade(label="Import", menu=filemenu)

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

    menubar.add_cascade(label="Sort", menu=filemenu)

    
    if debug>0:

        
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="clear", command=lambda: clear_data())
        filemenu.add_command(label="firstload", command=lambda: firstload())
        filemenu.add_command(label="init", command=lambda: init())
        filemenu.add_command(label="4", command=lambda: sortS(7))
        filemenu.add_command(label="5+", command=lambda: sortS(8))

        
         

        menubar.add_cascade(label=str(len(mlist)), menu=filemenu)


    
    root.config(menu=menubar)



    Label(text="All Songs "+str(len(mlist)),font=(20)).grid(row=0,column=0,columnspan=7)
    Label(text="Playlist",font=(20)).grid(row=0,column=8,columnspan=4)







    listPlist = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listPlist.grid(row=1,column=8,columnspan=4)
    listPlist.bind("<Double-Button-1>", OnDouble)



    #listSongs = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listSongs = Tktree.MultiListbox(root, width=1200,height=400,font=("Helvetica", 12),backgroundmode="row",selectmode=1,selectcmd=nice)
    listSongs.grid(row=1,column=0,rowspan=1,columnspan=8)
    #listSongs.config(columns=('Directory', 'Song Name','songSubname','authorName','difficlty','bpm','rating','highscore','date'))
    print emoji.emojize('Python is :thumbs_up:')
    listSongs.config(columns=(emoji.emojize(':star:',use_aliases=True),'Song Name', 'Artist Name','Mapper?!','E','N','H','X','P','BPM','Rating'))
    listSongs.column_configure(1,arrow='down')
    listSongs.bind("<Double-Button-1>", OnDouble)
    #listSongs.bind("<Double-Button-1>", add)
    listSongs.column_configure(0,button=True)
    woop = Image.open('shit.png')
    woop = woop.resize((10, 40))
    woop = ImageTk.PhotoImage(woop)
    woop

    listSongs.configure(backgroundimage=woop)

    





    ##############songdetails=[value,songName,songsubname,authorName,diff,bpm,thumb,environmentName]





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
    sortS(1)


    mainloop()
main()
