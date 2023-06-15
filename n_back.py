import sys
import pygame
import numpy as np
from image import Image
from settings import Settings
from datetime import datetime
from dateutil.parser import parse


def run_n_back():
    settings = Settings()
    first_time = datetime.now()
    array = np.zeros(30)
    respon_time = 0
    time_array= np.zeros(30)
    array2 = np.zeros(30)
    array3 = np.zeros(30)
    k=0
    picnum=settings.picnum + 2
    acrate = 0
    tcount = 0
    nback =settings.nback
    value = 99
    flag = 1
    last_k=1+nback
    pygame.init()
    screen = pygame.display.set_mode(settings.screen_mode)
    pygame.display.set_caption(settings.caption)
    image = Image(screen, settings,k,array,value,picnum)
    while k<(picnum):
        screen.fill(settings.screen_bg_color)
        (first_time,array,k)=image.image_update()
        for i in range(1,picnum):
            if k==last_k+i:
                flag = 1
                last_k=last_k+1
                break     
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN) & (flag == 1) & (k>1+nback):
                m=k-2
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_RIGHT:
                    if array[m]!= array[m-nback]:
                       tcount=tcount+1
                       print("ojbk")
                    else:
                       print("not ojbk")   
                if event.key == pygame.K_LEFT:
                    if array[m] == array[m-nback]:
                       tcount=tcount+1
                       print("ojbk")
                    else:
                       print("not ojbk")             
                #space=space+1
                flag = 0
                respon_time= (datetime.now()-first_time).total_seconds()
                time_array[k-2-nback]= respon_time
            else:
                pass
    if (k-2-nback) != 0:
        acrate=float(tcount/(k-2-nback))
    pygame.display.quit()
    return (array,acrate,time_array)

if __name__ == '__main__':
    (array2,acrate,array3)=run_n_back()
    #print(array2)
    settings = Settings()
    picnum=settings.picnum
    print("你小子的正确率为 ",acrate)
    print("你小子的反应时间为 ",array3[:picnum-1])