from drawBot import *

class showtype:
    
    def __init__(self,msg,font,fSize,duration=1/20,delay=20,bgSize=(800,600),bgColor = 0,fColor = 1):
        self.msg = msg
        self.font = font
        self.fSize = fSize
        self.duration = duration
        self.delay = delay
        self.bgSize = bgSize
        self.bgColor = bgColor
        self.fColor = fColor

        self.w,self.h = self.bgSize
        
        self.transTime = 5
        
        self.alpha = 1        
        self.alphaInc = self.alpha / self.transTime 
        
        self.fadeInc = 1/self.transTime
        
        self.marginW = self.w/12
        self.marginH = self.h/12
        
        self.typewriter()
        
    def bg(self):
        fill(self.bgColor)
        rect(0,0,self.w,self.h)
        
    def draw(self,fx = None):
        self.bg()

        font(self.font)
        fontSize(self.fSize)
        openTypeFeatures(calt="True")
        fill(self.fColor,self.alpha)
        textBox(self.temp,(self.marginW,self.marginH,self.w-self.marginW*2,self.h-self.marginH*2))           
        
    def typewriter(self,temp=""):
    
        txt = list(self.msg)
        self.temp = temp

        for i in txt:

            newPage(self.w,self.h)
            frameDuration(self.duration)
    
            self.draw()
            self.temp += i
                        
        self.atraso()
        self.fadeOut()

    def atraso(self):

        for i in range(self.delay):
            w,h = self.bgSize
            newPage(self.w,self.h)
            
            self.draw()        

    def fadeOut(self):
        # self.fading = self.fColor
        # cor = self.fColor
        
        for i in range(self.transTime):
            newPage(self.w,self.h)
            fill(self.fColor,self.alpha)
                  
            self.alpha -= self.alphaInc
            print(self.alphaInc,self.alpha)
            self.draw("fadeOut")
        

say = "Squint at the world. You will see more, by seeing less. \n\n— John Maeda"
showtype(say,"helvetica",70)

# txt = showtype(say,"FoglihtenNo07calt",150,bgSize=(1920,1080),duration=1/10)


saveImage("showtype_teste_calt_blink.mp4")
