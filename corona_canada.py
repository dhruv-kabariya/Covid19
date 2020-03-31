import pygame
import pandas as pd
import csv
# import datetime
import time


provision = ['Ontario','Alberta','British Columbia','Manitoba','Saskatchewan',"Nunavut",'Northwest Territories','Quebec','Nova Scotia','New Brunswick','Prince Edward Island','Yukon','Newfoundland and Labrador','Repatriated Travellers']
provisions = {
    'Ontario' : { "color" : (90, 175, 82),'point':(1900,1000),"case":0,"deaths" : 0,},
    'Alberta' : { "color" : (92, 191, 197),'point':(1620,950),"case":0,"deaths" : 0,},
    'British Columbia' : { "color" : (87, 133, 195),'point':(1520,1000),"case":0,"deaths" : 0,},
    'Manitoba' : { "color" : (179, 206, 75),'point':(1795,1000),"case":0,"deaths" : 0,},
    'Saskatchewan' : { "color" : (101, 186, 144),'point':(1705,1050),"case":0,"deaths" : 0,},
    'Nunavut' : { "color" :  (190, 104, 153),'point':(1780,770),"case":0,"deaths" : 0,},
    'Northwest Territories' : { "color" : (144, 103, 169),'point':(1600,800),"case":0,"deaths" : 0,},
    'Quebec' : { "color" : (252, 225, 72),'point':(2070,1050),"case":0,"deaths" : 0,},
    'Nova Scotia' : { "color" : (96, 228, 255),'point':(2250,1240),"case":0,"deaths" : 0,"line":[(2100,1240),(2120,1240)],'circle':(2265,1255)},
    'New Brunswick' : { "color" : (242, 87, 105),'point':(2100,1240),"case":0,"deaths" : 0,"line":[(2120,1240),(2100,1240)],'circle':(2115,1255)},
    'Prince Edward Island' : { "color" : (8, 81, 156),'point':(2400,1250),"case":0,"deaths" : 0,"line":[(2120,1240),(2100,1240)],'circle':(2405,1260)},
    'Yukon' : { "color" : (103, 107, 171),'point':(1425,850),"case":0,"deaths" : 0,},
    'Newfoundland And Labrador' : { "color" : (238, 148, 77),'point':(2370,1045),"case":0,"deaths" : 0,"line":[(2120,1240),(2100,1240)],'circle':(2380,1060)},
    'Repatriated Travellers' : { "color" : (181, 185, 188),'point':(2250,450),"case":0,"deaths" : 0,},
    'Canada' : { "color" : (255, 225, 186),'point':(1414,50),"case":0,"deaths" : 0,}
}



format = '%d-%m-%Y'
df = pd.read_csv('covid19 .csv')

le = len(df["prname"])
pygame.init()



height = 1300
width = 2500
remain = 2500-923-200

resolution = (width,height)
black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0) 



win =  pygame.display.set_mode(resolution)
pygame.display.set_caption('Canada COVID-19 Cases')
win.fill(black)


#load image
backgroud =  pygame.image.load('canada.png').convert()

# transform image ( raise size )
backgroud = pygame.transform.scale(backgroud,(923,1200))



# simple text
def showTitle(text,color,size=72): 
    font = pygame.font.SysFont("comicsansms", size)
    return font.render(text, True, color)

# number text
def updateText(text,color):
    font = pygame.font.SysFont("comicsansms", 50)
    return font.render(text, True, color)


# line for bars
def printLine(name,he,case,color,tot):

    #name
    font = pygame.font.SysFont("comicsansms", 30)
    name = font.render(name,True,color)
    win.blit(name,(100,he-30))

    # bar length
    length = ((case/tot)*1000)
    if length < 100:
        length = 105
    pygame.draw.lines(win, color, False, [(100,he), (length,he)], 20)
    font = pygame.font.SysFont("comicsansms", 30)
    text =  font.render(str(case), True, color)
    win.blit(text,(length+10,he-10))


total = 0

start =0
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill(black)
    backgroud =  pygame.image.load('canada.png').convert()

    # transform image ( raise size )
    backgroud = pygame.transform.scale(backgroud,(923,1200))
    
    font = pygame.font.SysFont("comicsansms", 40)
    win.blit(backgroud, (remain,0))

    # total cases
    win.blit(showTitle("Total cases : ",(255, 225, 186)),(1100,50))
    win.blit(showTitle(str(provisions['Canada']['case']),(255, 225, 186)),(1414,50))

    # total deaths
    win.blit(showTitle("Total Deaths : ",(255, 225, 186)),(1100,120))
    win.blit(showTitle(str(provisions['Canada']['deaths']),(255, 225, 186)),(1440,120))

    # traveller name
    win.blit(showTitle("Repatriated Travellers",(255, 225, 255),size=35),(2100,400))
    # win.blit(showTitle(str(provisions['Repatriated Travellers']['case']),(255, 0, 186)),(2250,450))
    
    
    
    if start < le:
        date = df["date"][start]
        win.blit(showTitle("Date : ",(255, 225, 186)),(40,40))
        win.blit(showTitle(date,(255, 225, 186)),(200,40))
        # if provisions[df["prname"][start]]["case"] != df["numconf"][start]:
        if provisions[df["prname"][start].title()]["case"] != df["numconf"][start]:
            if df["prname"][start].title() == "Canada":
                # print("yes")
                total = df["numconf"][start]
            else:

                total += (df["numconf"][start] - provisions[df["prname"][start].title()]["case"])
                # print(total)
        # print(total)
        provisions[df["prname"][start].title()]["case"] = df["numconf"][start]
        provisions[df["prname"][start].title()]["deaths"] = df["numdeaths"][start]
    else:

        win.blit(showTitle("Date : ",(255, 225, 186)),(40,40))
        win.blit(showTitle(date,(255, 225, 186)),(200,40))
        
    he = 200

    for key in provisions:
            
        if key != "Canada":
            if 'line' in provisions[key]:
                pygame.draw.circle(win, provisions[key]['color'], provisions[key]["circle"], 35, 0)
                   
                text =  font.render(str(provisions[key]['case']), True, (255,255,255))  # provisions[key]['color']
                win.blit(text,provisions[key]['point'])
    
            else:
                text =  font.render(str(provisions[key]['case']), True, (255,255,255))  # provisions[key]['color']
                win.blit(text,provisions[key]['point'])
            printLine(key,he,provisions[key]['case'],provisions[key]['color'],total)
            he += 80
            
    # time.sleep(0.1)     
    # prevade = df["date"][start]   
    start +=1
    pygame.display.flip()
    pygame.display.update()

pygame.quit()