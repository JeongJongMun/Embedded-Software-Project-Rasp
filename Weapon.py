import numpy as np
import time

class Weapon:
    def __init__(self, width, height):
        self.state = None
        self.weaponState = None
        
        self.aimPos = np.array([int(width/2)-25, int(height/2)-25]) # Aim 위치
        self.aimCenter = np.array([self.aimPos[0]+15, self.aimPos[1]+15 , self.aimPos[0]+35, self.aimPos[1]+35]) # Fire 시 충돌 범위
        self.score = 0
        self.hp_list = [[0,0],[30,0],[60,0]] # 체력 리스트
        
        # Fire
        self.fire_speed = 0
        self.reload_speed = 0
        self.bullets_list = [(-5, 210), (8, 210), (21, 210), (34, 210), (47, 210)]        
        self.fireDamage = 1
        # Throw - grenade
        self.throw_speed = 0
        self.grenades = 3
        self.grePos = 0
        self.greCenter = 0
        self.nowThrowing = False
        
    def move(self, command = None):
        if command['move'] == False:
            self.state = None
        
        else:
            self.state = 'move'

            if command['up_pressed']:
                self.aimPos[1] -= 10

            if command['down_pressed']:
                self.aimPos[1] += 10

            if command['left_pressed']:
                self.aimPos[0] -= 10
                
            if command['right_pressed']:
                self.aimPos[0] += 10
                
        # aimCenter 업데이트
        self.aimCenter = np.array([self.aimPos[0]+15, self.aimPos[1]+15 , self.aimPos[0]+35, self.aimPos[1]+35])
    
    def Reload(self):
        self.bullets_list = [(-5, 210), (8, 210), (21, 210), (34, 210), (47, 210)]        
        self.weaponState = None
        
    def ReloadControl(self):
        if self.reload_speed < 30:
            self.reload_speed += 1
        else:
            self.reload_speed = 0
            self.Reload()
        

    def Fire(self):
        if len(self.bullets_list) != 0:
            self.bullets_list.pop()
        self.weaponState = "fire"
        
    def FireControl(self):
        if self.fire_speed < 7: # Fire 속도 == while문이 7번 돌때마다 1발
            self.fire_speed += 1
        if self.weaponState == "fire": # Fire 시
            self.fire_speed = 0
            self.weaponState = None
        if self.fire_speed == 7: # Fire 가능
            return True

    def Throw(self):
        if self.grenades != 0:
            self.weaponState = "throw"
            self.grenades -= 1
            self.grePos = self.aimPos.copy()
            self.greCenter = np.array([self.grePos[0]-50, self.grePos[1]-50, self.grePos[0]+100, self.grePos[1]+100])

            self.nowThrowing = True
            
    def ThrowControl(self):
        if self.throw_speed < 50: # Throw 속도 == while문이 50번 돌때마다 1번
            self.throw_speed += 1
        if self.weaponState == "throw": # Throw 시
            self.throw_speed = 0
            self.weaponState = None
        if self.throw_speed == 50: # Throw 가능
            return True
        
        
    def collision_check(self, zombies, my_enemy, check):
        for zombie in zombies:
            if check == "aim":
                collision = self.overlap(self.aimCenter, zombie.position, "aim")
            elif check == "gre":
                collision = self.overlap(self.greCenter, zombie.position, "gre")
            
            if collision:
                my_enemy.zombies_list.remove(zombie)
                self.score += 100

                
    def overlap(self, ego_aimPos, other_aimPos, check): # ego = 자기 자신
        if check == "aim":
            print(check)
            return ego_aimPos[0] > other_aimPos[0] and ego_aimPos[1] > other_aimPos[1] \
                 and ego_aimPos[2] < other_aimPos[2] and ego_aimPos[3] < other_aimPos[3]
                 
        elif check == "gre":
            print(check)
            return ego_aimPos[0] < other_aimPos[0] and ego_aimPos[1] < other_aimPos[1] \
                 and ego_aimPos[2] > other_aimPos[2] and ego_aimPos[3] > other_aimPos[3]