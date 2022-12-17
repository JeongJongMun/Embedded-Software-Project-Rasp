import numpy as np
import time
import math

class Weapon:
    def __init__(self, width, height):
        self.state = None
        self.weaponState = None
        self.airbombardment = False
        
        self.aimPos = np.array([int(width/2), int(height/2)]) # Aim 위치
        self.aimCenter = np.array([self.aimPos[0]-15, self.aimPos[1]-15 , self.aimPos[0]+15, self.aimPos[1]+15]) # Fire 시 충돌 범위
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
        self.greTargetPos = 0
        self.greCenter = 0
        self.nowThrowing = False
        self.throwAngle = 0
        
        # Air Bombardment
        self.airplanePos = np.array([120, 270])
        self.airplaneCenter = np.array([self.airplanePos[0]-200, self.airplanePos[1]-65, self.airplanePos[0]+200, self.airplanePos[1]+65])
        self.airbombardmentCount = True
        
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
        self.aimCenter = np.array([self.aimPos[0]-15, self.aimPos[1]-15 , self.aimPos[0]+15, self.aimPos[1]+15]) # Fire 시 충돌 범위
    
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
            self.greTargetPos = self.aimPos.copy()
            self.greCenter = np.array([self.greTargetPos[0]-100, self.greTargetPos[1]-100, self.greTargetPos[0]+100, self.greTargetPos[1]+100])

            self.nowThrowing = True
            
    def ThrowControl(self):
        if self.throw_speed < 50: # Throw 속도 == while문이 50번 돌때마다 1번
            self.throw_speed += 1
        if self.weaponState == "throw": # Throw 시
            self.throw_speed = 0
            # 각도 계산
            if self.greTargetPos[0] > 120:
                temp = math.atan2(self.greTargetPos[1]-210, self.greTargetPos[0]-120)
            else:
                temp = math.atan2(self.greTargetPos[1]-210, 120-self.greTargetPos[0])
            self.throwAngle = math.degrees(temp)
            self.weaponState = None
        if self.throw_speed == 50: # Throw 가능
            return True
        
        
    def collision_check(self, my_enemy, check):
        for zombie in my_enemy.zombies_list:
            if check == "aim":
                collision = self.overlap(self.aimCenter, zombie.center, "aim")
            elif check == "gre":
                collision = self.overlap(self.greCenter, zombie.center, "gre")
            elif check == "air":
                collision = self.overlap(self.airplaneCenter, zombie.center, "air")
            
            if collision:
                my_enemy.zombies_list.remove(zombie)
                self.score += 100
                
        for rock in my_enemy.rockList:
            if check == "aim":
                collision = self.overlap(self.aimCenter, rock.center, "aim")
            elif check == "gre":
                collision = self.overlap(self.greCenter, rock.center, "gre")
            elif check == "air":
                collision = self.overlap(self.airplaneCenter, rock.center, "air")
            
            if collision:
                my_enemy.rockList.remove(rock)
                self.score += 300
                
        if check == "aim":
            collision = self.overlap(self.aimCenter, my_enemy.bossCenter, "aim")
        elif check == "gre":
            collision = self.overlap(self.greCenter, my_enemy.bossCenter, "gre")
        elif check == "air":
            collision = self.overlap(self.airplaneCenter, my_enemy.bossCenter, "air")
            
        if collision:
            if check == "aim":
                my_enemy.bossHp -= 5
            elif check == "gre":
                my_enemy.bossHp -= 10
            elif check == "air":
                my_enemy.bossHp -= 2
            print("Boss HP : ",my_enemy.bossHp)

                
    def overlap(self, ego_aimPos, other_aimPos, check): # ego = 자기 자신
        if check == "aim":
            return ego_aimPos[0] > other_aimPos[0] and ego_aimPos[1] > other_aimPos[1] \
                 and ego_aimPos[2] < other_aimPos[2] and ego_aimPos[3] < other_aimPos[3]
                 
        else:
            return ego_aimPos[0] < other_aimPos[0] and ego_aimPos[1] < other_aimPos[1] \
                 and ego_aimPos[2] > other_aimPos[2] and ego_aimPos[3] > other_aimPos[3]
                 
    def Airbombardment(self):
        if self.airplanePos[1] > -130:
            self.airplanePos[1] -= 5
            self.airplaneCenter = np.array([self.airplanePos[0]-200, self.airplanePos[1]-65, self.airplanePos[0]+200, self.airplanePos[1]+65])

        else:
            self.airplanePos = np.array([120, 270])
            self.airbombardment = False