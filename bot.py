import pyautogui, keyboard

class Rect:
    def __init__(self,x,y,w,h):
        self.x = x 
        self.y = y 
        self.h = h 
        self.w = w
class Coords:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

bot_mode = 'Turn off'
ticker = 0
ticker_max = 21 
seccond_ticker = 0
seccond_ticker_max = 100

stage_counter = 1


width, height = pyautogui.size()

level_change_coords = Coords(0,0)

def Search_for_next_upgrade(rect):
    try:
        x,y,w,h = pyautogui.locateOnScreen('hire_enable_button.png', region=(rect.x,rect.y,rect.w,rect.h/2))
        if x and y and w and h:
            return x,y
    except:
        try:
            x,y,w,h = pyautogui.locateOnScreen('hire_enable_button2.png', region=(rect.x,rect.y,rect.w,rect.h))
            if x and y and w and h:
                return x,y
        except:
            return 0,0


def Try_change_level(l,r,a):
    rect = Rect(l.x,l.y,r.x-l.x,r.h)
    print(" x:"+str(rect.x)+" y:"+str(rect.y)+" w:"+str(rect.w)+" h:"+str(rect.h*2))
    try: 
        x,y,w,h = pyautogui.locateAllOnScreen('next_stage_icon.png',region=(rect.x,rect.y,rect.w,rect.h*2))
        if x and y and w and h:
            level_change_coords = Coords(x+w/2,y+h/2)
            return
    except:
        level_change_coords = Coords(0,0)     
        return
x = None
x,y,w,h = pyautogui.locateOnScreen('clicking_background.png')
Attack_rect = Rect(x,y,w,h)
ux, uy, uw, uh = pyautogui.locateOnScreen('Upgrades_image.png')
print("x:"+str(ux)+" y:"+str(uy)+" w:"+str(uw)+" h:"+str(uh))
Upgrades_icon_rect = Rect(ux,uy,uw,uh)

Upgrades_rect = Rect(Upgrades_icon_rect.x, 
                    Upgrades_icon_rect.y + Upgrades_icon_rect.h,
                    Upgrades_icon_rect.w*24,
                    Upgrades_icon_rect.h*24
               )
print("x:"+str(Upgrades_rect.x)+" y:"+str(Upgrades_rect.y)+" w:"+str(Upgrades_rect.w)+" h:"+str(Upgrades_rect.h))

x,y,w,h = pyautogui.locateOnScreen('level_changer_left.png')
level_changer_left = Rect(x,y,w,h)
print("x:"+str(x)+" y:"+str(y)+" w:"+str(w)+" h:"+str(h))

x,y,w,h = pyautogui.locateOnScreen('Next_stage_arrow.png')
Next_stage_arrow = Rect(x,y,w,h)
print("x:"+str(x)+" y:"+str(y)+" w:"+str(w)+" h:"+str(h))

x,y,w,h = pyautogui.locateOnScreen('level_changer_right.png')
level_changer_right = Rect(x,y,w,h)
print("x:"+str(x)+" y:"+str(y)+" w:"+str(w)+" h:"+str(h))


pyautogui.moveTo(Attack_rect.x+Attack_rect.w/2,Attack_rect.y+Attack_rect.h/2)
while True:
    if seccond_ticker >= seccond_ticker_max:
        pyautogui.moveTo(level_changer_left.x + (level_changer_right.x - level_changer_left.x)/2 + (level_changer_right.x - level_changer_left.x)/7, level_changer_left.y + level_changer_left.h/2)
        pyautogui.click()
        pyautogui.moveTo(Attack_rect.x+Attack_rect.w/2,Attack_rect.y+Attack_rect.h/2)
        seccond_ticker = 0
        seccond_ticker_max += seccond_ticker_max *0.1
    if ticker >=ticker_max:
        x,y = Search_for_next_upgrade(Upgrades_rect)
        if x != 0 and y !=0:
            pyautogui.moveTo(x,y)
            pyautogui.click()
            pyautogui.moveTo(Attack_rect.x+Attack_rect.w/2,Attack_rect.y+Attack_rect.h/2)
            ticker_max += 2
        ticker = 0
    if keyboard.is_pressed('q'): break
    if keyboard.is_pressed('a'):
        pyautogui.moveTo(level_changer_left.x + (level_changer_right.x - level_changer_left.x)/2 - (level_changer_right.x - level_changer_left.x)/8, level_changer_left.y + level_changer_left.h/2)
        pyautogui.click()
        pyautogui.moveTo(Attack_rect.x+Attack_rect.w/2,Attack_rect.y+Attack_rect.h/2)
    if keyboard.is_pressed('d'):
        pyautogui.moveTo(level_changer_left.x + (level_changer_right.x - level_changer_left.x)/2 + (level_changer_right.x - level_changer_left.x)/7, level_changer_left.y + level_changer_left.h/2)
        pyautogui.click()
        pyautogui.moveTo(Attack_rect.x+Attack_rect.w/2,Attack_rect.y+Attack_rect.h/2)
    
    pyautogui.click()
    ticker+=1
    seccond_ticker += 1

   
