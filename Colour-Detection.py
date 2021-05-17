import numpy as np
import cv2 as cv
import pandas as pd
import copy

# Read the image, list column names, read csv with the said columns
image=cv.imread('bg.jpg')
column_names=['colour','colour name','hex','r','g','b']
df=pd.read_csv('colors.csv',names=column_names,header=None)

#create a copy of the original image for resetting on each click
image_copy=copy.deepcopy(image)

click=False
b=g=r=xpos=ypos=-1

def mouse_function(event,x,y,flag,params):
    global click,b,g,r,xpos,ypos,image,image_copy
    if event == cv.EVENT_LBUTTONDOWN: #single click event 
        image_copy=copy.deepcopy(image)
        click=True
        b,g,r=image[y,x] #get the RGB values on the pixel 
        b=int(b)
        g=int(g)
        r=int(r)
        xpos=x
        ypos=y
cv.namedWindow('image') 

def Getcolorname(r,g,b):
    min=float('inf')
    for i in range(len(df)):
        #iterate through each row in the dataset and calculate the min value of the RGB differences 
        distance= abs(df.loc[i,'r']-r) + abs(df.loc[i,'g']-g)+abs(df.loc[i,'b']-b)
        if distance < min:
            min=distance
            name=df.loc[i,'colour name']
    return name

while True:
    
    cv.imshow('image',image_copy)
    if click == True:
        cname=Getcolorname(r,g,b)
         #if the click is on the right most area of the image, that would result 
         #in the rectangle going out of the boundary of the image, hence tweaking the rectangle points
        if(xpos>0.75*image.shape[1]):
            xpos=xpos-400
          
        cv.rectangle(image_copy,(xpos,ypos-40),(xpos+600,ypos),(b,g,r),-1)
        text=cname+' R =' + str(r)+' G =' + str(g)+' B =' + str(b)
        
        if b+g+r>=600: #if the colour is light, use black as the text colour
            cv.putText(image_copy, text,(xpos+10,ypos-10),2,0.5,(0,0,0),1,cv.LINE_AA)
        else:
            cv.putText(image_copy,text,(xpos+10,ypos-10),2,0.5,(255,255,255),1,cv.LINE_AA)
    #keep calling the function on mouse click until ESC is pressed       
    cv.setMouseCallback('image',mouse_function)
    
    k= cv.waitKey(20) & 0xFF
    if k==27:
        break
    
cv.destroyAllWindows()

