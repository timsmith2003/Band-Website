from tkinter import *
import random
import requests
root = Tk()

words = ('about','above','abuse','actor','acute','admit','adopt','adult','after','again','agent','agree','ahead','alarm','album','alert','alike','alive','allow','alone','along','alter','among','anger','Angle','angry','apart','apple','apply','arena','argue','arise','array','aside','asset','audio','audit','avoid','award','aware','badly','baker','bases','basic','basis','beach','began','begin','begun','being','below','bench','billy','birth','black','blame','blind','block','blood','board','boost','booth','bound','brain','brand','bread','break','breed','brief','bring','broad','broke','brown','build','built','buyer','cable','calif','carry','catch','cause','chain','chair','chart','chase','cheap','check','chest','chief','child','china','chose','civil','claim','class','clean','clear','click','clock','close','coach','coast','could','count','court','cover','craft','crash','cream','crime','cross','crowd','crown','curve','cycle','daily','dance','dated','dealt','death','debut','delay','depth','doing','doubt','dozen','draft','drama','drawn','dream','dress','drill','drink','drive','drove','dying','eager','early','earth','eight','elite','empty','enemy','enjoy','enter','entry','equal','error','event','every','exact','exist','extra','faith','false','fault','fiber','field','fifth','fifty','fight','final','first','fixed','flash','fleet','floor','fluid','focus','force','forth','forty','forum','found','frame','frank','fraud','fresh','front','fruit','fully','funny','giant','given','glass','globe','going','grace','grade','grand','grant','grass','great','green','gross','group','grown','guard','guess','guest','guide','happy','harry','heart','heavy','hence','henry','horse','hotel','house','human','ideal','image','index','inner','input','issue','japan','jimmy','joint','jones','judge','known','label','large','laser','later','laugh','layer','learn','lease','least','leave','legal','level','lewis','light','limit','links','lives','local','logic','loose','lower','lucky','lunch','lying','magic','major','maker','march','maria','match','maybe','mayor','meant','media','metal','might','minor','minus','mixed','model','money','month','moral','motor','mount','mouse','mouth','movie','music','needs','never','newly','night','noise','north','noted','novel','nurse','occur','ocean','offer','often','order','other','ought','paint','panel','paper','party','peace','peter','phase','phone','photo','piece','pilot','pitch','place','plain','plane','plant','plate','point','pound','power','press','price','pride','prime','print','prior','prize','proof','proud','prove','queen','quick','quiet','quite','radio','raise','range','rapid','ratio','reach','ready','refer','right','rival','river','robin','roger','roman','rough','round','route','royal','rural','scale','scene','scope','score','sense','serve','seven','shall','shape','share','sharp','sheet','shelf','shell','shift','shirt','shock','shoot','short','shown','sight','since','sixth','sixty','sized','skill','sleep','slide','small','smart','smile','smith','smoke','solid','solve','sorry','sound','south','space','spare','speak','speed','spend','spent','split','spoke','sport','staff','stage','stake','stand','start','state','steam','steel','stick','still','stock','stone','stood','store','storm','story','strip','stuck','study','stuff','style','sugar','suite','super','sweet','table','taken','taste','taxes','teach','teeth','terry','texas','thank','theft','their','theme','there','these','thick','thing','think','third','those','three','threw','throw','tight','times','tired','title','today','topic','total','touch','tough','tower','track','trade','train','treat','trend','trial','tried','tries','truck','truly','trust','truth','twice','under','undue','union','unity','until','upper','upset','urban','usage','usual','valid','value','video','virus','visit','vital','voice','waste','watch','water','wheel','where','which','while','white','whole','whose','woman','women','world','worry','worse','worst','worth','would','wound','write','wrong')


def begin():
    global row
    row = 9
    global answer
    answer = random.choice(words)
    e.delete(0, END)
    e.insert(0, "Enter guess here")
    q = Button(root, text="q")
    w = Button(root, text="w")
    E = Button(root, text="e")
    r = Button(root, text="r")
    t = Button(root, text="t")
    y = Button(root, text="y")
    u = Button(root, text="u")
    i = Button(root, text="i")
    o = Button(root, text="o")
    p = Button(root, text="p")
    a = Button(root, text="a")
    s = Button(root, text="s")
    d = Button(root, text="d")
    f = Button(root, text="f")
    g = Button(root, text="g")
    h = Button(root, text="h")
    j = Button(root, text="j")
    k = Button(root, text="k")
    l = Button(root, text="l")
    z = Button(root, text="z")
    x = Button(root, text="x")
    c = Button(root, text="c")
    v = Button(root, text="v")
    b = Button(root, text="b")
    n = Button(root, text="n")
    m = Button(root, text="m")


    q .grid(row=6,column=1)
    w .grid(row=6,column=2)
    E .grid(row=6,column=3)
    r .grid(row=6,column=4) 
    t .grid(row=6,column=5)
    y .grid(row=6,column=6)
    u .grid(row=6,column=7)
    i .grid(row=6,column=8)
    o .grid(row=6,column=9)
    p .grid(row=6,column=10)
    a .grid(row=7,column=1)
    s .grid(row=7,column=2)
    d .grid(row=7,column=3)
    f .grid(row=7,column=4)
    g .grid(row=7,column=5)
    h .grid(row=7,column=6) 
    j .grid(row=7,column=7)
    k .grid(row=7,column=8)
    l .grid(row=7,column=9)
    z .grid(row=8,column=2)
    x .grid(row=8,column=3)
    c .grid(row=8,column=4)
    v .grid(row=8,column=5)
    b .grid(row=8,column=6)
    n .grid(row=8,column=7) 
    m .grid (row=8,column=8)
    
    reset = Label(root, text='                                                                                                                                      \n                                                                                                                                                                       \n                                                                                                                                                                       \n                                                                                                                                                                       \n                                                                                                                                                                       \n                                                                                                                                                                       \n                                                                                                                                                                       \n                                                                                                                                                                       \n                                                                               \n                                                                                     \n                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n                                 ', bg='#f0f0f0')
    reset.grid(row=9, column=0, columnspan=30, rowspan=30)






def enter():
    guess = e.get()
    response = (requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{guess}"))
    if len(e.get()) == 5 and response.status_code == 200:
        global row
        row+=2

        global one
        global two
        global three
        global four
        global five
        global dash

        dash = Label(text='--------------------------------------------------------').grid(row=row, column=0, columnspan=10)

        if guess[0] == answer[0]:    
            one = Button(root, text=guess[0], bg='green').grid(row=row+1, column=3)
        elif guess[0] in answer:
            one = Button(root, text=guess[0], bg='yellow').grid(row=row+1, column=3)
        else:
            one = Button(root, text=guess[0], bg='gray').grid(row=row+1, column=3)
        if guess[1] == answer[1]:
            two = Button(root, text=guess[1], bg='green').grid(row= row+1, column=4)
        elif guess[1] in answer:
            two = Button(root, text=guess[1], bg='yellow').grid(row=row+1, column=4)
        else:
            two = Button(root, text=guess[1], bg='gray').grid(row=row+1, column=4)
        if guess[2] == answer[2]:
            three = Button(root, text=guess[2], bg='green').grid(row=row+1, column=5)
        elif guess[2] in answer:
            three = Button(root, text=guess[2], bg='yellow').grid(row=row+1, column=5)
        else:
            three = Button(root, text=guess[2], bg='gray').grid(row=row+1, column=5)
        if guess[3] == answer[3]:
            four = Button(root, text=guess[3], bg='green').grid(row=row+1, column=6)
        elif guess[3] in answer:
            four = Button(root, text=guess[3], bg='yellow').grid(row=row+1, column=6)
        else:
            four = Button(root, text=guess[3], bg='gray').grid(row=row+1, column=6)
        if guess[4] == answer[4]:
            five = Button(root, text=guess[4], bg='green').grid(row=row+1, column=7)
        elif guess[4] in answer:
            five = Button(root, text=guess[4], bg='yellow').grid(row=row+1, column=7)
        else:
            five = Button(root, text=guess[4], bg='gray').grid(row=row+1, column=7)
        

        if   'q'  in guess and   'q' not in answer:
            q = Button(root, text="q", bg='gray').grid(row=6, column=1)
        elif   'q' in guess and   'q' in answer and (  'q' in guess[0] and   'q' in answer[0]) or (  'q' in guess[1] and   'q'  in answer[1]) or (  'q' in guess[2] and   'q' in answer[2]) or (  'q' in guess[3] and   'q' in answer[3]) or (  'q' in guess[4] and   'q' in answer[4]):
            q = Button(root, text="q", bg='green').grid(row=6, column=1)
        elif   'q' in guess and   'q' in answer:
            q = Button(root, text="q", bg='yellow').grid(row=6, column=1)

        if    'w'  in guess and    'w' not in answer:
            w = Button(root, text="w", bg='gray').grid(row=6, column=2)
        elif    'w' in guess and    'w' in answer and (   'w' in guess[0] and    'w' in answer[0]) or (   'w' in guess[1] and    'w'  in answer[1]) or (   'w' in guess[2] and    'w' in answer[2]) or (   'w' in guess[3] and    'w' in answer[3]) or (   'w' in guess[4] and    'w' in answer[4]):
            w = Button(root, text="w", bg='green').grid(row=6, column=2)
        elif    'w' in guess and    'w' in answer:
            w = Button(root, text="w", bg='yellow').grid(row=6, column=2)

        if    'e'  in guess and    'e' not in answer:
            E = Button(root, text="e", bg='gray').grid(row=6, column=3)
        elif    'e' in guess and    'e' in answer and (   'e' in guess[0] and    'e' in answer[0]) or (   'e' in guess[1] and    'e'  in answer[1]) or (   'e' in guess[2] and    'e' in answer[2]) or (   'e' in guess[3] and    'e' in answer[3]) or (   'e' in guess[4] and    'e' in answer[4]):
            E = Button(root, text="e", bg='green').grid(row=6, column=3)
        elif    'e' in guess and    'e' in answer:
            E = Button(root, text="e", bg='yellow').grid(row=6, column=3)

        if    'r'  in guess and    'r' not in answer:
            r = Button(root, text="r", bg='gray').grid(row=6, column=4)
        elif    'r' in guess and    'r' in answer and (   'r' in guess[0] and    'r' in answer[0]) or (   'r' in guess[1] and    'r'  in answer[1]) or (   'r' in guess[2] and    'r' in answer[2]) or (   'r' in guess[3] and    'r' in answer[3]) or (   'r' in guess[4] and    'r' in answer[4]):
            r = Button(root, text="r", bg='green').grid(row=6, column=4)
        elif    'r' in guess and    'r' in answer:
            r = Button(root, text="r", bg='yellow').grid(row=6, column=4)

        if    't'  in guess and    't' not in answer:
            t = Button(root, text="t", bg='gray').grid(row=6, column=5)
        elif    't' in guess and    't' in answer and (   't' in guess[0] and    't' in answer[0]) or (   't' in guess[1] and    't'  in answer[1]) or (   't' in guess[2] and    't' in answer[2]) or (   't' in guess[3] and    't' in answer[3]) or (   't' in guess[4] and    't' in answer[4]):
            t = Button(root, text="t", bg='green').grid(row=6, column=5)
        elif    't' in guess and    't' in answer:
            t = Button(root, text="t", bg='yellow').grid(row=6, column=5)

        if    'y'  in guess and    'y' not in answer:
            y = Button(root, text="y", bg='gray').grid(row=6, column=6)
        elif    'y' in guess and    'y' in answer and (   'y' in guess[0] and    'y' in answer[0]) or (   'y' in guess[1] and    'y'  in answer[1]) or (   'y' in guess[2] and    'y' in answer[2]) or (   'y' in guess[3] and    'y' in answer[3]) or (   'y' in guess[4] and    'y' in answer[4]):
            y = Button(root, text="y", bg='green').grid(row=6, column=6)
        elif    'y' in guess and    'y' in answer:
            y = Button(root, text="y", bg='yellow').grid(row=6, column=6)
        
        if    'u'  in guess and    'u' not in answer:
            u = Button(root, text="u", bg='gray').grid(row=6, column=7)
        elif    'u' in guess and    'u' in answer and (   'u' in guess[0] and    'u' in answer[0]) or (   'u' in guess[1] and    'u'  in answer[1]) or (   'u' in guess[2] and    'u' in answer[2]) or (   'u' in guess[3] and    'u' in answer[3]) or (   'u' in guess[4] and    'u' in answer[4]):
            u = Button(root, text="u", bg='green').grid(row=6, column=7)
        elif    'u' in guess and    'u' in answer:
            u = Button(root, text="u", bg='yellow').grid(row=6, column=7)

        if    'i'  in guess and    'i' not in answer:
            i = Button(root, text="i", bg='gray').grid(row=6, column=8)
        elif    'i' in guess and    'i' in answer and (   'i' in guess[0] and    'i' in answer[0]) or (   'i' in guess[1] and    'i'  in answer[1]) or (   'i' in guess[2] and    'i' in answer[2]) or (   'i' in guess[3] and    'i' in answer[3]) or (   'i' in guess[4] and    'i' in answer[4]):
            i = Button(root, text="i", bg='green').grid(row=6, column=8)
        elif    'i' in guess and    'i' in answer:
            i = Button(root, text="i", bg='yellow').grid(row=6, column=8)

        if    'o'  in guess and    'o' not in answer:
            o = Button(root, text="o", bg='gray').grid(row=6, column=9)
        elif    'o' in guess and    'o' in answer and (   'o' in guess[0] and    'o' in answer[0]) or (   'o' in guess[1] and    'o'  in answer[1]) or (   'o' in guess[2] and    'o' in answer[2]) or (   'o' in guess[3] and    'o' in answer[3]) or (   'o' in guess[4] and    'o' in answer[4]):
            o = Button(root, text="o", bg='green').grid(row=6, column=9)
        elif    'o' in guess and    'o' in answer:
            o = Button(root, text="o", bg='yellow').grid(row=6, column=9)
        
        if    'p'  in guess and    'p' not in answer:
            p = Button(root, text="p", bg='gray').grid(row=6, column=10)
        elif    'p' in guess and    'p' in answer and (   'p' in guess[0] and    'p' in answer[0]) or (   'p' in guess[1] and    'p'  in answer[1]) or (   'p' in guess[2] and    'p' in answer[2]) or (   'p' in guess[3] and    'p' in answer[3]) or (   'p' in guess[4] and    'p' in answer[4]):
            p = Button(root, text="p", bg='green').grid(row=6, column=10)
        elif    'p' in guess and    'p' in answer:
            p = Button(root, text="p", bg='yellow').grid(row=6, column=10)

        if    'a'  in guess and    'a' not in answer:
            a = Button(root, text="a", bg='gray').grid(row=7, column=1)
        elif    'a' in guess and    'a' in answer and (   'a' in guess[0] and    'a' in answer[0]) or (   'a' in guess[1] and    'a'  in answer[1]) or (   'a' in guess[2] and    'a' in answer[2]) or (   'a' in guess[3] and    'a' in answer[3]) or (   'a' in guess[4] and    'a' in answer[4]):
            a = Button(root, text="a", bg='green').grid(row=7, column=1)
        elif    'a' in guess and    'a' in answer:
            a = Button(root, text="a", bg='yellow').grid(row=7, column=1)

        if    's'  in guess and    's' not in answer:
            s = Button(root, text="s", bg='gray').grid(row=7, column=2)
        elif    's' in guess and    's' in answer and (   's' in guess[0] and    's' in answer[0]) or (   's' in guess[1] and    's'  in answer[1]) or (   's' in guess[2] and    's' in answer[2]) or (   's' in guess[3] and    's' in answer[3]) or (   's' in guess[4] and    's' in answer[4]):
            s = Button(root, text="s", bg='green').grid(row=7, column=2)
        elif    's' in guess and    's' in answer:
            s = Button(root, text="s", bg='yellow').grid(row=7, column=2)

        if    'd'  in guess and    'd' not in answer:
            d = Button(root, text="d", bg='gray').grid(row=7, column=3)
        elif    'd' in guess and    'd' in answer and (   'd' in guess[0] and    'd' in answer[0]) or (   'd' in guess[1] and    'd'  in answer[1]) or (   'd' in guess[2] and    'd' in answer[2]) or (   'd' in guess[3] and    'd' in answer[3]) or (   'd' in guess[4] and    'd' in answer[4]):
            d = Button(root, text="d", bg='green').grid(row=7, column=3)
        elif    'd' in guess and    'd' in answer:
            d = Button(root, text="d", bg='yellow').grid(row=7, column=3)
        
        if    'f'  in guess and    'f' not in answer:
            f = Button(root, text="d", bg='gray').grid(row=7, column=4)
        elif    'f' in guess and    'f' in answer and (   'f' in guess[0] and    'f' in answer[0]) or (   'f' in guess[1] and    'f'  in answer[1]) or (   'f' in guess[2] and    'f' in answer[2]) or (   'f' in guess[3] and    'f' in answer[3]) or (   'f' in guess[4] and    'f' in answer[4]):
            f = Button(root, text="d", bg='green').grid(row=7, column=4)
        elif    'f' in guess and    'f' in answer:
            f = Button(root, text="d", bg='yellow').grid(row=7, column=4)

        if    'g'  in guess and    'g' not in answer:
            g = Button(root, text="g", bg='gray').grid(row=7, column=5)
        elif    'g' in guess and    'g' in answer and (   'g' in guess[0] and    'g' in answer[0]) or (   'g' in guess[1] and    'g'  in answer[1]) or (   'g' in guess[2] and    'g' in answer[2]) or (   'g' in guess[3] and    'g' in answer[3]) or (   'g' in guess[4] and    'g' in answer[4]):
            g = Button(root, text="g", bg='green').grid(row=7, column=5)
        elif    'g' in guess and    'g' in answer:
            g = Button(root, text="g", bg='yellow').grid(row=7, column=5)

        if    'h'  in guess and    'h' not in answer:
            h = Button(root, text="h", bg='gray').grid(row=7, column=6)
        elif    'h' in guess and    'h' in answer and (   'h' in guess[0] and    'h' in answer[0]) or (   'h' in guess[1] and    'h'  in answer[1]) or (   'h' in guess[2] and    'h' in answer[2]) or (   'h' in guess[3] and    'h' in answer[3]) or (   'h' in guess[4] and    'h' in answer[4]):
            h = Button(root, text="h", bg='green').grid(row=7, column=6)
        elif    'h' in guess and    'h' in answer:
            h = Button(root, text="h", bg='yellow').grid(row=7, column=6)
        
        if    'j'  in guess and    'j' not in answer:
            j = Button(root, text="j", bg='gray').grid(row=7, column=7)
        elif    'j' in guess and    'j' in answer and (   'j' in guess[0] and    'j' in answer[0]) or (   'j' in guess[1] and    'j'  in answer[1]) or (   'j' in guess[2] and    'j' in answer[2]) or (   'j' in guess[3] and    'j' in answer[3]) or (   'j' in guess[4] and    'j' in answer[4]):
            j = Button(root, text="j", bg='green').grid(row=7, column=7)
        elif    'j' in guess and    'j' in answer:
            j = Button(root, text="j", bg='yellow').grid(row=7, column=7)

        if    'k'  in guess and    'k' not in answer:
            k = Button(root, text="k", bg='gray').grid(row=7, column=8)
        elif    'k' in guess and    'k' in answer and (   'k' in guess[0] and    'k' in answer[0]) or (   'k' in guess[1] and    'k'  in answer[1]) or (   'k' in guess[2] and    'k' in answer[2]) or (   'k' in guess[3] and    'k' in answer[3]) or (   'k' in guess[4] and    'k' in answer[4]):
            k = Button(root, text="k", bg='green').grid(row=7, column=8)
        elif    'k' in guess and    'k' in answer:
            k = Button(root, text="k", bg='yellow').grid(row=7, column=8)

        if    'l'  in guess and    'l' not in answer:
            l = Button(root, text="l", bg='gray').grid(row=7, column=9)
        elif    'l' in guess and    'l' in answer and (   'l' in guess[0] and    'l' in answer[0]) or (   'l' in guess[1] and    'l'  in answer[1]) or (   'l' in guess[2] and    'l' in answer[2]) or (   'l' in guess[3] and    'l' in answer[3]) or (   'l' in guess[4] and    'l' in answer[4]):
            l = Button(root, text="l", bg='green').grid(row=7, column=9)
        elif    'l' in guess and    'l' in answer:
            l = Button(root, text="l", bg='yellow').grid(row=7, column=9)

        if    'z'  in guess and    'z' not in answer:
            z = Button(root, text="z", bg='gray').grid(row=8, column=2)
        elif    'z' in guess and    'z' in answer and (   'z' in guess[0] and    'z' in answer[0]) or (   'z' in guess[1] and    'z'  in answer[1]) or (   'z' in guess[2] and    'z' in answer[2]) or (   'z' in guess[3] and    'z' in answer[3]) or (   'z' in guess[4] and    'z' in answer[4]):
            z = Button(root, text="z", bg='green').grid(row=8, column=2)
        elif    'z' in guess and    'z' in answer:
            z = Button(root, text="z", bg='yellow').grid(row=8, column=2)
        
        if    'x'  in guess and    'x' not in answer:
            x = Button(root, text="x", bg='gray').grid(row=8, column=3)
        elif    'x' in guess and    'x' in answer and (   'x' in guess[0] and    'x' in answer[0]) or (   'x' in guess[1] and    'x'  in answer[1]) or (   'x' in guess[2] and    'x' in answer[2]) or (   'x' in guess[3] and    'x' in answer[3]) or (   'x' in guess[4] and    'x' in answer[4]):
            x = Button(root, text="x", bg='green').grid(row=8, column=3)
        elif    'x' in guess and    'x' in answer:
            x = Button(root, text="x", bg='yellow').grid(row=8, column=3)

        if    'c'  in guess and    'c' not in answer:
            c = Button(root, text="c", bg='gray').grid(row=8, column=4)
        elif    'c' in guess and    'c' in answer and (   'c' in guess[0] and    'c' in answer[0]) or (   'c' in guess[1] and    'c'  in answer[1]) or (   'c' in guess[2] and    'c' in answer[2]) or (   'c' in guess[3] and    'c' in answer[3]) or (   'c' in guess[4] and    'c' in answer[4]):
            c = Button(root, text="c", bg='green').grid(row=8, column=4)
        elif    'c' in guess and    'c' in answer:
            c = Button(root, text="c", bg='yellow').grid(row=8, column=4)
        
        if    'v'  in guess and    'v' not in answer:
            v = Button(root, text="v", bg='gray').grid(row=8, column=5)
        elif    'v' in guess and    'v' in answer and (   'v' in guess[0] and    'v' in answer[0]) or (   'v' in guess[1] and    'v'  in answer[1]) or (   'v' in guess[2] and    'v' in answer[2]) or (   'v' in guess[3] and    'v' in answer[3]) or (   'v' in guess[4] and    'v' in answer[4]):
            v = Button(root, text="v", bg='green').grid(row=8, column=5)
        elif    'v' in guess and    'v' in answer:
            v = Button(root, text="v", bg='yellow').grid(row=8, column=5)

        if    'b'  in guess and    'b' not in answer:
            b = Button(root, text="b", bg='gray').grid(row=8, column=6)
        elif    'b' in guess and    'b' in answer and (   'b' in guess[0] and    'b' in answer[0]) or (   'b' in guess[1] and    'b'  in answer[1]) or (   'b' in guess[2] and    'b' in answer[2]) or (   'b' in guess[3] and    'b' in answer[3]) or (   'b' in guess[4] and    'b' in answer[4]):
            b = Button(root, text="b", bg='green').grid(row=8, column=6)
        elif    'b' in guess and    'b' in answer:
            b = Button(root, text="b", bg='yellow').grid(row=8, column=6)

        if    'n'  in guess and    'n' not in answer:
            n = Button(root, text="n", bg='gray').grid(row=8, column=7)
        elif    'n' in guess and    'n' in answer and (   'n' in guess[0] and    'n' in answer[0]) or (   'n' in guess[1] and    'n'  in answer[1]) or (   'n' in guess[2] and    'n' in answer[2]) or (   'n' in guess[3] and    'n' in answer[3]) or (   'n' in guess[4] and    'n' in answer[4]):
            n = Button(root, text="n", bg='green').grid(row=8, column=7)
        elif    'n' in guess and    'n' in answer:
            n = Button(root, text="n", bg='yellow').grid(row=8, column=7)

        if    'm'  in guess and    'm' not in answer:
            m = Button(root, text="m", bg='gray').grid(row=8, column=8)
        elif    'm' in guess and    'm' in answer and (   'm' in guess[0] and    'm' in answer[0]) or (   'm' in guess[1] and    'm'  in answer[1]) or (   'm' in guess[2] and    'm' in answer[2]) or (   'm' in guess[3] and    'm' in answer[3]) or (   'm' in guess[4] and    'm' in answer[4]):
            m = Button(root, text="m", bg='green').grid(row=8, column=8)
        elif    'm' in guess and    'm' in answer:
            m = Button(root, text="m", bg='yellow').grid(row=8, column=8)
        
        if guess == answer:
            e.delete(0, END)
            e.insert(0,"Winner! Click WORDLE to play again")
        if row >= 20 and guess != answer:
            e.delete(0, END)
            e.insert(0,f':(the word was "{answer}" click WORDLE to play again')
    else:
        e.delete(0,END)
        e.insert(0,f"{guess} is not a 5 letter words in the dictionary!")

top = Button(root, width=15, text='WORDLE', command=begin, padx=3, pady=3)
e = Entry(root,width=50, border=7)
submit = Button(root, text="submit", command=enter, bg="pink")
space = Label(root, text=" ")

q = Button(root, text="q")
w = Button(root, text="w")
E = Button(root, text="e")
r = Button(root, text="r")
t = Button(root, text="t")
y = Button(root, text="y")
u = Button(root, text="u")
i = Button(root, text="i")
o = Button(root, text="o")
p = Button(root, text="p")
a = Button(root, text="a")
s = Button(root, text="s")
d = Button(root, text="d")
f = Button(root, text="f")
g = Button(root, text="g")
h = Button(root, text="h")
j = Button(root, text="j")
k = Button(root, text="k")
l = Button(root, text="l")
z = Button(root, text="z")
x = Button(root, text="x")
c = Button(root, text="c")
v = Button(root, text="v")
b = Button(root, text="b")
n = Button(root, text="n")
m = Button(root, text="m")

 
 



top.grid(row=0, column=0, rowspan=2, columnspan=10)
space.grid(row=2, column=0, columnspan=10)
submit.grid(row=3, column=8)
e.grid(row=3, column=1, columnspan=7 )
e.insert(0,'Click the wordle button above to begin!')



q .grid(row=6,column=1)
w .grid(row=6,column=2)
E .grid(row=6,column=3)
r .grid(row=6,column=4) 
t .grid(row=6,column=5)
y .grid(row=6,column=6)
u .grid(row=6,column=7)
i .grid(row=6,column=8)
o .grid(row=6,column=9)
p .grid(row=6,column=10)
a .grid(row=7,column=1)
s .grid(row=7,column=2)
d .grid(row=7,column=3)
f .grid(row=7,column=4)
g .grid(row=7,column=5)
h .grid(row=7,column=6) 
j .grid(row=7,column=7)
k .grid(row=7,column=8)
l .grid(row=7,column=9)
z .grid(row=8,column=2)
x .grid(row=8,column=3)
c .grid(row=8,column=4)
v .grid(row=8,column=5)
b .grid(row=8,column=6)
n .grid(row=8,column=7) 
m .grid(row=8,column=8)

root.geometry('410x450')

root.mainloop()