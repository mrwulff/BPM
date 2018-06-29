from Tkinter import *
import TkTreectrl as Tktree
import webbrowser
import Tkinter, Tkconstants, tkFileDialog


import os
import json
from PIL import Image, ImageTk
from string import *
import emoji
import ast
from natsort import natsorted
import shutil

from tkinter import ttk


dirpath =0


listPlist=0
listSongs=0
value=0
pvalue=0

txtColor='white'
plistselect2=0
mlist=[]
tempmlist=[]
dirs=[]
short=20
#column=[]


upordown=1
debug=5
lastselected=0
searchf=[]

dif=[False,False,False,False,False]
test1=0


def rate(rating):

    
        
    selection=listSongs.curselection()

    
    if debug>0:
        print selection,rating ,mlist[selection[0]][10],' Song selection and rating'
    rating=str(rating)
    mlist[selection[0]][10]=rating
    mlist[selection[0]][17]=1
    export_extra_data()
    savesongs()
    init(mlist)


    
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
    
       
    
    
    

def init(all_list):

    Label(anchor='w',text=str(len(all_list))+" Songs ",font=(20)).grid(row=0,column=0,columnspan=7,ipadx=50,sticky='W')

    print 'running init with',len(all_list),' songs'
    try:
        listSongs.delete(0,'end')
    except:
        print listSongs
    print 'running ini2 with',len(all_list),' songs'
    
    odd=0
    tag="odd"

    for x in range(len(all_list)):
        odd=odd+1

        ea=''
        m=''
        h=''
        ex=''
        p=''

        
        if all_list[x][4]==True:
            ea=emoji.emojize(':heavy_check_mark:')
        if all_list[x][5]==True:
            m=emoji.emojize(':heavy_check_mark:')
        if all_list[x][6]==True:
            h=emoji.emojize(':heavy_check_mark:')
        if all_list[x][7]==True:
            ex=emoji.emojize(':heavy_check_mark:')
        if all_list[x][8]==True:
            p=emoji.emojize(':heavy_check_mark:')

        rate=''
        if all_list[x][10]=='':
            (all_list[x][10])=0
        for cz in range(int(all_list[x][10])):
            rate=rate+emoji.emojize(':star:',use_aliases=True)
        
        listSongs.insert(END,emoji.emojize(':star:',use_aliases=True),all_list[x][14],all_list[x][13],all_list[x][12],ea,m,h,ex,p,all_list[x][9],rate,all_list[x][16],'no')
        
        tag = "even" if tag == "odd" else "odd"
        '''
        if odd%2==0:
            listSongs.configure(itembackground="#e0e0e0")
            print odd
        if odd%2==1:
            listSongs.configure(itembackground="white")
            print odd
        '''
            
        

    #sortS(1)



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

def loadinfojson(input_file,value,bsid):
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
    songdetails=[value,songName,songsubname,authorName,diffE,diffN,diffH,diffX,diffP,str(bpm),'',environmentName,authorNameS,songsubnameS,songNameS,thumb,bsid,0,0,0,0,0,]
    #17=updated?
    mlist.append(songdetails)
    #print songdetails
def loadxinfo(j,value,bsid):
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
    #rint type(j["Hard"]),'jhard#######'
    
    
def sb(v):
  return v.lower() in ("yes", "true", "t", "1")
def findid(a,b):
    newdirpath=a+'/'+b+'/'
    for x in os.listdir(newdirpath):
        return b+'/'+x,b


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
        bsid=0
        isid=False
        has_extra_data=False
        
        value=sl[c]
        if value!='.cache':
            if value!='playlist.json':
        
                
                
                if 1==1:
                    try:
                        #print value,'wtf'
                        if int(value)>1:
                           isid=True
                    except:
                        print value,'not found'
                        ''
                    if isid:
                        
                        value,bsid=findid(dirpath,value)
                    
                           
                    a=dirpath+"/"+value+"/info.json"
                    a_extra=dirpath+"/"+value+"/ainfo.json"
                    input_file  = file(a, "r")
                    try:
                        input_file2  = file(a_extra, "r")
                        j2 = json.loads(input_file2.read())
                        has_extra_data=True
                        if debug>1:
                            print 'found extra data',value
                            
                    except:
                        if debug>10:
                            print 'did not find extra data',value
                    if has_extra_data==False:
                        #load all songs without extradata
                        loadinfojson(input_file,value,bsid)
                        ""

                    if has_extra_data==True:
                        xdata=xdata+1
                        loadxinfo(j2,value,bsid)
                        ''
                        #print 'running extra data'
    if debug>3:
        print xdata, 'found songs with x data'
 
        
       
def OnDouble(event):
    
    global lastselected
    

    #Label(text="All Songs "+str(len(mlist)),font=(20)).grid(row=0,column=0,columnspan=5)
    #global value
    #widget = event.widget

    selection=listSongs.curselection()
    if type(selection)==tuple:

        print selection,'tuple.'
        selection=selection[0]
    value= mlist[selection][0]

    '''
    if mlist[selection][16] == 0:
        updatebsid(selection)
    if mlist[selection][16] == "":
        updatebsid(selection)
    '''

    
    #value55 = widget.get(selection[0])
    #print value55
    #print "selection:", selection, ": '%s'" % value
    #a=dirpath+"/"+value+"/info.json"
    #print a
    #input_file  = file(a, "r")
    #j = json.loads(input_file.read())
    #print j["songSubName"]
    #print j
    diff=''
    
    try:
        environmentName=mlist[selection][11]
    except:
        selection=selection[0]
        environmentName=mlist[selection][11]
    '''
    for i in range(4-10):
        print i,'shitbird'
        if mlist[selection][i]:
            diff=diff+1
    ddd=diff
    print diff,'diff levels'
    '''
    print mlist[selection][4],'woop'
    if mlist[selection][4]:
        diff=diff+'Easy '
    if mlist[selection][5]:
        diff=diff+'Normal '
    if mlist[selection][6]:
        diff=diff+'Hard '
    if mlist[selection][7]:
        diff=diff+'Expert '
    if mlist[selection][8]:
        diff=diff+'Expert+'
    

        

    #songdetails=[value,songName,songsubname,authorName,diffE,diffN,diffH,diffX,diffP,str(bpm),'',environmentName,authorNameS,songsubnameS,songNameS,thumb,'',0,0,0,0,0,]





    authorName=mlist[selection][3]
    songsubname=mlist[selection][2]
    bpm=mlist[selection][9]
    songName=mlist[selection][1]
    thumb=mlist[selection][15]
    #print thumb
    try:
        print dirpath+'/'+value+'/'+thumb
        image = Image.open(dirpath+'/'+value+'/'+thumb)
    except:
        image = Image.open(dirpath+'/'+value+'/'+thumb+'.jpg')
        print "error: invalid image(double.jpg in "+value

    image=image.resize((250,250))

    photo = ImageTk.PhotoImage(image)
    


    #print songName,thumb,bpm,songsubname,authorName,environmentName

    #return songName,thumb,bpm,songsubname,authorName,environmentName
    offs=1
    fcoll=0
    p=7
    
    Label(justify='right',anchor='w',bg=txtColor,text=songName,font=(12)).grid(       row=offs+3,column=fcoll+1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7+p)
    Label(justify='left',anchor='w',bg=txtColor,text=songsubname,font=(12)).grid(     row=offs+4,column=fcoll+1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7+p)
    Label(justify='left',anchor='w',bg=txtColor,text=authorName,font=(12)).grid(      row=offs+5,column=fcoll+1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7+p)
    Label(justify='left',anchor='w',bg=txtColor,text=songName,font=(12)).grid(        row=offs+7,column=fcoll+1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7+p)
    Label(justify='left',anchor='nw',bg=txtColor,text=environmentName,font=(12)).grid(row=offs+8,column=fcoll+1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7+p)
    Label(justify='left',anchor='nw',bg=txtColor,text=bpm,font=(12)).grid(            row=offs+9,column=fcoll+1,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=7+p)
    Label(justify='left',anchor='w',bg=txtColor,text=diff,font=(12)).grid(row=offs+6,column=fcoll+1,columnspan=7+p,ipadx=100,sticky='W'+'E'+'S'+'N')


    Label(justify='left',anchor='e',bg=txtColor,text="Title: ",font=(12)).grid(       row=offs+3,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Artist: ",font=(12)).grid(      row=offs+4,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Mapper: ",font=(12)).grid(      row=offs+5,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Difficulties: ",font=(12)).grid(row=offs+6,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Directory: ",font=(12)).grid(          row=offs+7,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Graphics: ",font=(12)).grid(    row=offs+8,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="BPM: ",font=(12)).grid(         row=offs+9,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="HighScore: ",font=(12)).grid(  row=offs+10,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Rating: ",font=(12)).grid(     row=offs+11,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Comment: ",font=(12)).grid(    row=offs+12,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)
    Label(justify='left',anchor='e',bg=txtColor,text="Categories : ",font=(12)).grid(row=offs+13,column=fcoll+0,ipadx=100,sticky='W'+'E'+'S'+'N',columnspan=1)


    

    '''
    #print diff
    for bb in difficultyLevels:
        #print bb
        #print type(bb)
        ddd= bb['difficulty']+' '+ddd
    '''
        


    label = Label(image=photo)
    label.image=photo
    
    
    label.grid(row=3,column=18,rowspan=9,columnspan=4,sticky="N"+"W")


def savesongs():
    ###Saves mlist (all song array) to local file for caching
    print 'opendd'
    dd=open('localsongs.txt','w')
    dd.write(str(mlist))
    print 'wrotedd'
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
def sortS(sort,col):
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
        
    mlist=natsorted(mlist,key=lambda l:l[col], reverse=way)
    #mlist=sorted(mlist,key=lambda l:l[sort], reverse=way)
    #mlist=natsorted(mlist)
    init(mlist)
    way=way+1
    print way,' in sort'
    #for a in range(len(mlist)):
        #print mlist[a][10]

        
    return way
def write_extra_data(a,val):

#songdetails=[value,songName,songsubname,authorName,diffE,diffN,diffH,diffX,diffP,str(bpm),'',environmentName,authorNameS,songsubnameS,songNameS,thumb,'',0,0,0,0,0,]
    print mlist[a]
    print dirpath

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
    aa=aa+'    "BeatSaverID": "'+str(mlist[a][16])+'",\n'
    aa=aa+'    "Comments": "'+str(mlist[a][17])+'",\n'
    aa=aa+'    "Genere": "'+str(mlist[a][18])+'",\n'
    aa=aa+'    "Uploaded": "'+str(mlist[a][19])+'",\n'
    aa=aa+'    "Downloaded": "'+str(mlist[a][20])+'"\n}'
    
    w=open(dirpath+'/'+mlist[a][0]+"/ainfo.json",'w')
    w.write(aa)
    if debug>3:
        #print aa, 'extra json output'
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
def search(data,f):
    listSongs.delete(0,'end')
    tempmlist=[]

    ff=f.get()
    print ff
    for i in range(len(mlist)):
        is_in=False
        for j in range(len(mlist[i])):
            try:
                if lower(ff) in lower(mlist[i][j]) and is_in==False:
                    #print mlist[i]
                    is_in=True
                    tempmlist.append(mlist[i])
            except:
                ''
    init(tempmlist)
def resettext():
    searchf.delete(0, END)
    
    init(mlist)



def callback(event):
    webbrowser.open_new(r"http://www.google.com")

def getdir():
    global dirpath
    dirpath = tkFileDialog.askdirectory()

    d={'dir':dirpath}
    a=open('config.json','w')
    a.write(str(d))
    a.close()
    print 

def filterset(root3,a,b,c,d,e,diff):
    global test1
    for i in range(len(a)):
        if a[i]=='selected':
            dif[0]=True
        else:
            dif[0]=False

    for i in range(len(b)):
        if b[i]=='selected':
            dif[1]=True
        else:
            dif[1]=False

    for i in range(len(c)):
        if c[i]=='selected':
            dif[2]=True
        else:
            dif[2]=False

    for i in range(len(d)):
        if d[i]=='selected':
            dif[3]=True
        else:
            dif[3]=False

    for i in range(len(e)):
        if e[i]=='selected':
            dif[4]=True
        else:
            dif[4]=False

    all_list=mlist

    print all_list[1][4]


    listSongs.delete(0,'end')
    tempmlist=[]


    for i in range(len(mlist)):
        is_in=False
        for j in range(len(mlist[i])):
            try:
                if dif[0]==True and mlist[i][4]==True and is_in==False:
                    #print mlist[i]
                    is_in=True

                if dif[1]==True and mlist[i][5]==True and is_in==False:
                    #print mlist[i]
                    is_in=True

                if dif[2]==True and mlist[i][6]==True and is_in==False:
                    #print mlist[i]
                    is_in=True

                if dif[3]==True and mlist[i][7]==True and is_in==False:
                    #print mlist[i]
                    is_in=True


                if dif[4]==True and mlist[i][8]==True and is_in==False:
                    #print mlist[i]
                    is_in=True





                    
            except:
                ''



        if is_in==True:
            tempmlist.append(mlist[i])
            
    init(tempmlist)


def filter2():
    global dif


            
    root3 = Tk()



    root3.title('Filter')
    Label(root3,text="Include in list:",font=(30)).grid(row=0,column=0,columnspan=4)



    chk1 = ttk.Checkbutton(root3, text="E")
    chk1.grid(row=3,column=0,sticky='w')
    
    if dif[0]==True:
        chk1.state(['!alternate'])
        chk1.state(['selected',])

    if dif[0]==False:
        chk1.state(['!alternate'])
        chk1.state(['!selected'])



    chk2 = ttk.Checkbutton(root3, text="N")
    chk2.grid(row=4,column=0,sticky='w')

    if dif[1]==True:
        chk2.state(['!alternate'])
        chk2.state(['selected',])

    if dif[1]==False:
        chk2.state(['!alternate'])
        chk2.state(['!selected'])

    chk3 = ttk.Checkbutton(root3, text="H")
    chk3.grid(row=5,column=0,sticky='w')

    if dif[2]==True:
        chk3.state(['!alternate'])
        chk3.state(['selected',])

    if dif[2]==False:
        chk3.state(['!alternate'])
        chk3.state(['!selected'])

    chk4 = ttk.Checkbutton(root3, text="E")
    chk4.grid(row=6,column=0,sticky='w')

    if dif[3]==True:
        chk4.state(['!alternate'])
        chk4.state(['selected',])

    if dif[3]==False:
        chk4.state(['!alternate'])
        chk4.state(['!selected'])

    chk5 = ttk.Checkbutton(root3, text="E+")
    chk5.grid(row=7,column=0,sticky='w')

    if dif[4]==True:
        chk5.state(['!alternate'])
        chk5.state(['selected',])

    if dif[4]==False:
        chk5.state(['!alternate'])
        chk5.state(['!selected'])



    setdir = Button(root3,anchor='w', text="Set Filter", command= lambda: filterset(root3,chk1.state(),chk2.state(),chk3.state(),chk4.state(),chk5.state(),dif)).grid(row=7,column=1,columnspan=1,sticky='E'+'W')



def about():

    root2 = Tk()
    root2.title('ABOUT BPM')
    Label(root2,text="BeatSaber Playlist Maker (BPM)",font=(30)).grid(row=0,column=0,columnspan=4)
    #Label(root2,text="Coded by @kevlights",font=(20)).grid(row=1,column=0,columnspan=4)
    Label(root2,text="Thanks to Beatsaver and Bsaver",font=(20)).grid(row=2,column=0,columnspan=4)

    Label(root2,anchor='w',text="Set Beatsaber directory:",font=(20)).grid(row=3,column=0,columnspan=1,sticky='w')
    setdir = Button(root2,anchor='w', text="...", command=getdir).grid(row=3,column=1,columnspan=1,sticky='E'+'W')
    



    

    lbl = Label(root2,justify='left',anchor='w', text="Coded by Kevin", font=20 ,cursor="hand2")

    lbl.grid(row=1,column=0,columnspan=4,sticky='W')
    #lbl.pack()
    lbl.bind("<Button-1>", callback)

    Label(root2,text=dirpath,font=(14)).grid(row=4,column=0,columnspan=1)


    
    




    
def main():
    global dirpath
    global searchf
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
    root.title('BPM')

    global bpmsort
    configfound=False
    try:
        zz=open('config.json','r')
        configfound=True
        
    except:
        getdir()

    if configfound:
        for line in zz.readlines():
            line=ast.literal_eval(line)
            dirpath= line['dir']
            if len(dirpath)<3:
                getdir()
    print dirpath,'dirpath@!!!!!'



    fcol=10
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=12)
    filemenu.add_command(label="Open", command=add)
    filemenu.add_command(label="Save", command=save)
    filemenu.add_command(label="About", command=about)

    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Local Songs", command=init(mlist))
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
    bpmsort= filemenu.add_command(label="NEW", command=lambda: sortS(10,16))

    filemenu.add_command(label="Song", command=lambda: sortS(1,1))
    filemenu.add_command(label="Artist", command=lambda: sortS(2,2))
    filemenu.add_command(label="Mapper", command=lambda: sortS(3,3))
    filemenu.add_command(label="Starred", command=lambda: sortS(4,4))
    filemenu.add_command(label="Rating", command=lambda: sortS(10,10))
    filemenu.add_command(label="Score", command=lambda: sortS(6,6))
    bpmsort= filemenu.add_command(label="BPM", command=lambda: sortS(9,9))

    filemenu.add_separator()
    filemenu.add_command(label="Easy", command=lambda: sortS(4,4))
    filemenu.add_command(label="Normal", command=lambda: sortS(5,5))
    filemenu.add_command(label="Hard", command=lambda: sortS(6,6))
    filemenu.add_command(label="Expert", command=lambda: sortS(7,7))
    filemenu.add_command(label="Expert+", command=lambda: sortS(8,8))

    menubar.add_cascade(label="Sort", menu=filemenu)

    
    if debug>0:

        
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="clear", command=lambda: clear_data())
        filemenu.add_command(label="firstload", command=lambda: firstload())
        filemenu.add_command(label="init", command=lambda: init(mlist))
        filemenu.add_command(label="4", command=lambda: sortS(7))
        filemenu.add_command(label="5+", command=lambda: sortS(8))

        
         

        menubar.add_cascade(label="Debug", menu=filemenu)


    
    root.config(menu=menubar)



    #Label(text="All Songs "+str(len(mlist)),font=(20)).grid(row=0,column=0,columnspan=7)
    Label(text="Playlist",font=(20)).grid(row=0,column=8,columnspan=4)







    listPlist = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listPlist.grid(row=1,column=fcol+8,columnspan=4)
    listPlist.bind("<Double-Button-1>", OnDouble)



    #listSongs = Listbox(root, width=30, height=20, font=("Helvetica", 12))
    listSongs = Tktree.MultiListbox(root, width=1200,height=400,font=("Helvetica", 12),backgroundmode="row",selectmode=1,selectcmd=nice)
    listSongs.grid(row=1,column=0,rowspan=1,columnspan=fcol+8)
    #listSongs.config(columns=('Directory', 'Song Name','songSubname','authorName','difficlty','bpm','rating','highscore','date'))
    print emoji.emojize('Python is :thumbs_up:')
    listSongs.config(columns=(emoji.emojize(':star:',use_aliases=True),'Song Name', 'Artist Name','Mapper?!','E','N','H','X','P','BPM','Rating','bsid','yes'))
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


    


    addsongbutton = Button(root,justify='left',anchor='w', text="Filter", command=filter2).grid(row=2,column=0)
    addsongbutton = Button(root, text="Add to Playlist", command=add).grid(row=2,column=2,columnspan=3)


    
    addallsongbutton = Button(root, text="Add All to Playlist", command=addall).grid(row=8,column=1)






    removesongbutton = Button(root, text="RemoveSelected", command=lambda listPlist=listPlist: listPlist.delete(ANCHOR)).grid(row=2,column= fcol+8,)
    moveup = Button(root, text="Move up", command=move_up).grid(row=2,column=fcol+9,)
    movedown = Button(root, text="Move down", command=move_down).grid(row=2,column=fcol+10,)
    removesongbutton2 = Button(root, text="Remove All", command=remove).grid(row=2,column=fcol+11)








    #b = Button(master, text="Delete",command=lambda lb=lb: lb.delete(ANCHOR))

    plistselect2=listPlist.get(ANCHOR)


    

    Label(text="Rating:",anchor="e").grid(row=2,column=fcol+1,sticky='W'+'E'+'S'+'N')
    fcol=10

    #ratebutton = Button(root, text="0", command=remove).grid(row=2,column=1,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="1", command=lambda: rate(1)).grid(row=2,column=fcol+2,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="2", command=lambda: rate(2)).grid(row=2,column=fcol+3,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="3", command=lambda: rate(3)).grid(row=2,column=fcol+4,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="4", command=lambda: rate(4)).grid(row=2,column=fcol+5,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text="5", command=lambda: rate(5)).grid(row=2,column=fcol+6,sticky='W'+'E'+'S'+'N')
    ratebutton = Button(root, text=emoji.emojize(':star:',use_aliases=True), command=lambda: rate(6)).grid(row=2,column=fcol+7,sticky='W'+'E'+'S'+'N')



    

    #Label(text="Search",font=(20)).grid(row=0,column=5,columnspan=1)
    #Label(text="BLALB",font=(20)).grid(row=0,column=7,columnspan=1,sticky='W'+'S'+'N')
    searchf=Entry(root,font=(20),width=5)
    searchf.grid(row=0,column=fcol+6,sticky='E'+'S'+'N'+'W')
    print searchf
    sf=searchf.get()
    searchbutton = Button(root, text="search", command=lambda: search(sf,searchf)).grid(row=0,column=fcol+5,sticky='E'+'S'+'N')
    searchbutton = Button(root, text="reset", command=lambda: resettext()).grid(row=0,column=fcol+7,sticky='W'+'S'+'N')



    try:
        opensongs()
    except:
        print 'error loading db. scanning dirs...'
        firstload()
        print 'wtf'
    init(mlist)
    #sortS(1)


    mainloop()
main()









'''
def writebsid(b,c,a):
    #shutil.move('test', 'test2')
    print b,c,a,'JESUS SHIT'
    print mlist[a][0],'dir?'
    print 'oldfile=',dirpath+'/'+mlist[a][0]
    print 'newfile=',dirpath+'/'+str(b)+'/'+mlist[a][0]
                                         
    shutil.move(dirpath+'/'+mlist[a][0],dirpath+'/'+str(b)+'/'+mlist[a][0])
    

    ''
def updatebsid(a):
    print "   OMG MOTHERFUCKER",mlist[a][16]
    cc=open('datarip.txt')
    l=0
    newsong=[]
    newdate=[]
    newbsid=[]
    flag=False

    for line in cc.readlines():
        
            
        line=ast.literal_eval(line)
        if l==0:   
            for i in range(len(line)):
                newsong.append(line[i])
        if l==1:   
            for i in range(len(line)):
                newdate.append(line[i])
        if l==2:   
            for i in range(len(line)):
                newbsid.append(line[i])
            
        l=l+1
    
    #for c in range(len(newsong)):
    for c in range(len(newsong)):
        #print mlist[a][0],'       DAFUCK       ',newsong[c]
        if newsong[c]==mlist[a][0]:
            #print newsong[c]," FOUND MOTHERFUCKER",newbsid[c]
            part1=newbsid[c]
            part2=newdate[c]
            part3=a
            flag=True
        
        if mlist[a][1] in newsong[c]   :
           #print newsong[c]," FOUND CLOSE MOTHERFUCKER",newbsid[c]
            part1=newbsid[c]
            part2=newdate[c]
            part3=a
            
           
            flag=True
    if flag==True:
        writebsid(part1,part2,part3)
'''
       
