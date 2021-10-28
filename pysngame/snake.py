import pygame as py
import math
import random as rand
import pickle as pic

def addsnbody():
    snbod.append(py.Vector2((800,800)))

py.init()
py.font.init()
myfont = py.font.SysFont('Comic Sans MS', 15)
running = True
screenh=500
screenw=500
screen=py.display.set_mode((screenw,screenh),vsync=0)
snbod=[]
snbod.append(py.Vector2())
snbod[0].x=screenh/2
snbod[0].y=screenw/2
speed=12
dir=0
fps=25
fpsclock=py.time.Clock()
snsize=12
upturn=False
lefturn=True
ctr=0
t=()
fcounter=0
appsize=7.5
aploc=py.Vector2(800,800)
gameover=False
py.display.set_caption('SNAKEGAME')


try:
    f=open("sg.bin","rb")
    r=pic.load(f)
    hiscore=r[0]
    f.close()
    
except FileNotFoundError:
     f=open("sg.bin","wb")
     hiscore=0
     
     f.close


while True:
    
    if not gameover:
        for event in py.event.get():
            if event.type==py.QUIT:
                if ctr>hiscore:
                    f=open("sg.bin","wb")
                    hiscore=ctr
                    r=[]
                    r.append(hiscore)
                    pic.dump(r,f)
                    f.close()
                py.quit()

            if event.type == py.KEYDOWN:
                if event.key == py.K_UP and upturn:
                    dir=0
                    lefturn=True
                    upturn=False
                if event.key == py.K_DOWN and upturn:
                    dir=1
                    lefturn=True
                    upturn=False
                if event.key == py.K_LEFT and lefturn:
                    dir=2
                    lefturn=False
                    upturn=True
                if event.key == py.K_RIGHT and lefturn:
                    dir=3
                    lefturn=False
                    upturn=True
               
        if ctr>=0:
            t=()
            for i in range(0,ctr+1):
                x=snbod[i].x
                y=snbod[i].y
                t+=(py.Vector2((x,y)),)
            for i in range(0,ctr+1):

                if i==0:
                    continue
                snbod[i]=t[i-1]

        if fcounter>75:
            aploc=py.Vector2(((rand.randint(10,490)),(rand.randint(10,490))))
            fcounter=0   

        if dir==0:
            snbod[0].y-=speed
        if dir==1:
            snbod[0].y+=speed
        if dir==2:
            snbod[0].x-=speed
        if dir==3:
            snbod[0].x+=speed

        if snbod[0].x> screenw:
            snbod[0].x=0
        if snbod[0].y>screenh:
            snbod[0].y=0
        if snbod[0].x<0:
            snbod[0].x=screenw
        if snbod[0].y<0:
            snbod[0].y=screenh

        screen.fill((211,211,211))
        screen.blit(myfont.render("Score ="+str(ctr), False, (218,165,32)), (5, 10))
        screen.blit(myfont.render("HIScore ="+str(hiscore), False, (218,165,32)), (5, 40))
        
        if (snbod[0].x < (aploc.x + appsize) and ((snbod[0].x + snsize) > aploc.x) and (snbod[0].y < (aploc.y + appsize) and (snbod[0].y +snsize) >aploc.y)):
            ctr+=1
            aploc=py.Vector2(((rand.randint(10,490)),(rand.randint(10,490))))
            addsnbody()
        py.draw.rect(screen,(0,150,0),(snbod[0].x,snbod[0].y,snsize,snsize))
        if ctr!=0:
            for i in range(1,ctr+1):
                py.draw.rect(screen,(0,255,0),(snbod[i].x,snbod[i].y,snsize,snsize))
        py.draw.rect(screen,(255,0,0),(aploc.x,aploc.y,appsize,appsize))
        py.display.flip()

        

        for i in range(1,len(snbod)):
            if snbod[0]==snbod[i]:
                
                gameover=True
                break
    else:
        
        if ctr>hiscore:
            f=open("sg.bin","wb")
            hiscore=ctr
            r=[]
            r.append(hiscore)
            pic.dump(r,f)
            f.close()
        for event in py.event.get():
            screen.blit(myfont.render("Yuo Ded NOOB", False, (150,0,0)), (175, 250))
            screen.blit(myfont.render("Press enter to restart", False, (150,0,0)), (175, 290))
            if event.type==py.QUIT:
                if ctr>hiscore:
                    f=open("sg.bin","wb")
                    hiscore=ctr
                    r=[]
                    r.append(hiscore)
                    pic.dump(r,f)
                    f.close()
                py.quit()

            if event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    snbod=[]
                    snbod.append(py.Vector2((screenw/2,screenw/2)))
                    ctr=0
                    dir=0
                    upturn=False
                    lefturn=True
                    gameover=False
    py.display.update()
    fpsclock.tick(fps)
    fcounter+=1      









