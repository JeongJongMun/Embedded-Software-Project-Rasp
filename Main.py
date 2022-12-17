from PIL import Image, ImageDraw, ImageFont
import time
import random
import cv2 as cv
import numpy as np
import math
from colorsys import hsv_to_rgb
from Zombie import Zombie
from Weapon import Weapon
from Enemy import Enemy
from Joystick import Joystick
from Rock import Rock

# 총 맞을시 피 튀는거


def main():
    
    joystick = Joystick()
    my_weapon = Weapon(joystick.width, joystick.height)
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_enemy = Enemy()
    joystick.disp.image(my_image)
    throwPos = np.array([120,210])
    greRotation = 1
    

    img_bosszombie = Image.open('/home/kau-esw/esw/ESW-Project/images/bosszombie.png', mode='r').convert('RGBA')
    img_rock1 = Image.open('/home/kau-esw/esw/ESW-Project/images/rock.png', mode='r').convert('RGBA')
    img_rock2 = img_rock1.transpose(Image.ROTATE_90)
    img_rock3 = img_rock2.transpose(Image.ROTATE_90)
    img_rock4 = img_rock3.transpose(Image.ROTATE_90)

    img_zombie1 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie1.png', mode='r').convert('RGBA')
    img_zombie2 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie2.png', mode='r').convert('RGBA')
    img_zombie3 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie3.png', mode='r').convert('RGBA')
    img_zombie4 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie4.png', mode='r').convert('RGBA')
    img_zombie5 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie5.png', mode='r').convert('RGBA')
    img_zombie6 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie6.png', mode='r').convert('RGBA')
    img_zombie7 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie7.png', mode='r').convert('RGBA')
    img_zombie8 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie8.png', mode='r').convert('RGBA')
    img_zombie9 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie9.png', mode='r').convert('RGBA')
    img_zombie10 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie10.png', mode='r').convert('RGBA')
    img_zombie11 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie11.png', mode='r').convert('RGBA')
    img_zombie12 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie12.png', mode='r').convert('RGBA')
    img_zombie13 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie13.png', mode='r').convert('RGBA')
    img_zombie14 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie14.png', mode='r').convert('RGBA')
    img_zombie15 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie15.png', mode='r').convert('RGBA')
    
    img_grenadetimer1 = Image.open('/home/kau-esw/esw/ESW-Project/images/grenadetimer1.png', mode='r').convert('RGBA')
    img_grenadetimer2 = Image.open('/home/kau-esw/esw/ESW-Project/images/grenadetimer2.png', mode='r').convert('RGBA')
    img_grenadetimer3 = Image.open('/home/kau-esw/esw/ESW-Project/images/grenadetimer3.png', mode='r').convert('RGBA')

    img_hp = Image.open('/home/kau-esw/esw/ESW-Project/images/hp.png', mode='r').convert('RGBA')
    img_muzzleflash = Image.open('/home/kau-esw/esw/ESW-Project/images/muzzleflash.png', mode='r').convert('RGBA')
    img_statusbar = Image.open('/home/kau-esw/esw/ESW-Project/images/statusbar.png', mode='r').convert('RGBA')
    img_fieldbackground = Image.open('/home/kau-esw/esw/ESW-Project/images/fieldbackground.png', mode='r')       
    img_aim = Image.open('/home/kau-esw/esw/ESW-Project/images/aim.png', mode='r').convert('RGBA')
    img_bullet = Image.open('/home/kau-esw/esw/ESW-Project/images/bullet.png', mode='r').convert('RGBA')
    img_reload = Image.open('/home/kau-esw/esw/ESW-Project/images/reload.png', mode='r').convert('RGBA')
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25) # 폰트, 크기
    img_grenade1 = Image.open('/home/kau-esw/esw/ESW-Project/images/grenade.png', mode='r').convert('RGBA')
    img_grenade2 = img_grenade1.transpose(Image.ROTATE_90)
    img_grenade3 = img_grenade2.transpose(Image.ROTATE_90)
    img_grenade4 = img_grenade3.transpose(Image.ROTATE_90)
    
    img_airplane = Image.open('/home/kau-esw/esw/ESW-Project/images/airplane.png', mode='r').convert('RGBA')
    img_airbombardment = Image.open('/home/kau-esw/esw/ESW-Project/images/airbombardment.png', mode='r').convert('RGBA')

    img_greeffect = Image.open('/home/kau-esw/esw/ESW-Project/images/greeffect.png', mode='r').convert('RGBA')
    
    img_finish = Image.open('/home/kau-esw/esw/ESW-Project/images/finish.png', mode='r')
    img_fail = Image.open('/home/kau-esw/esw/ESW-Project/images/fail.png', mode='r')
    img_main = Image.open('/home/kau-esw/esw/ESW-Project/images/main.png', mode='r')
    img_kauemblem = Image.open('/home/kau-esw/esw/ESW-Project/images/kauemblem.png', mode='r')


    def Start(): # 시작 화면
        while True:
            my_image.paste(im=img_main, box=(0,0), mask=img_main)                     
            joystick.disp.image(my_image)
            if not joystick.button_A.value:
                break
            
    def Fail(): # 실패 화면
        while True:
            my_image.paste(im=img_fail, box=(0,0), mask=img_fail)                     
            my_draw.text((140, 105), str(my_weapon.score), font=fnt, fill=(211,99,110))           
            joystick.disp.image(my_image)
            if not joystick.button_A.value:
                my_weapon.hp_list = [[0,0],[30,0],[60,0]]
                my_weapon.score = 0
                my_weapon.grenades = 3
                my_enemy.zombies_list.clear()
                my_weapon.bullets_list.clear()
                my_enemy.rockList.clear()
                my_weapon.Reload()
                my_weapon.bossHp = 100
                my_weapon.airbombardmentCount = True
                break
    def Finish(): # 성공 화면
        while True:
            my_image.paste(im=img_finish, box=(0,0), mask=img_finish)                     
            my_draw.text((140, 105), str(my_weapon.score), font=fnt, fill=(211,99,110))           
            joystick.disp.image(my_image)
            if not joystick.button_A.value:
                my_weapon.hp_list = [[0,0],[30,0],[60,0]]
                my_weapon.score = 0
                my_weapon.grenades = 3
                my_enemy.zombies_list.clear()
                my_weapon.bullets_list.clear()
                my_enemy.rockList.clear()
                my_weapon.Reload()
                my_weapon.bossHp = 100
                my_weapon.airbombardmentCount = True
                break    
    Start() # 메인화면 시작
        
    
    while True: # 게임 시작
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False} # 딕셔너리
        
        my_image.paste(im=img_fieldbackground, box=(0,0)) # 배경 Draw

        # Boss
        if my_weapon.score >= 100:
            if my_enemy.BossMove() == "finish":
                Finish()
            my_enemy.bossStage = True
            my_image.paste(im=img_bosszombie, box=(tuple(my_enemy.bossPos-50)), mask=img_bosszombie)
            my_enemy.BossMove()
            if my_enemy.bossPhase == 1:
                my_enemy.BossPhaseOne(my_weapon)
                if my_enemy.BossPhaseOne(my_weapon):
                    my_enemy.rockList.append(Rock(my_enemy.rockSpawnPos[my_enemy.zombie_turn]))
            elif my_enemy.bossPhase == 2:
                my_enemy.BossPhaseTwo(my_weapon)
        
        # Phase One Rock Draw
        for rock in my_enemy.rockList:
            if greRotation == 4:
                greRotation = 1
            else:
                greRotation += 1
            rockList = {1 : img_rock1, 2 : img_rock2, 3 : img_rock3, 4 : img_rock4}
            my_image.paste(im=rockList[greRotation], box=(tuple(rock.spawn_position-25)), mask=rockList[greRotation])
            

            rock.move() # Rock Move
            
            if rock.spawn_position[1] > 210: # Rock 아래 상태바 통과 시 attack
                rock.Attack(rock, my_enemy, my_weapon)
                if len(my_weapon.hp_list) <= 0: # 체력이 0이 되면 Fail
                    Fail()
            
       
        if not joystick.button_U.value:  # up pressed / 조이스틱 버튼 눌림 감지
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        # A pressed = Fire
        if not joystick.button_A.value and joystick.button_B.value and len(my_weapon.bullets_list) != 0 and my_weapon.FireControl() == True:
            my_image.paste(img_muzzleflash, tuple(my_weapon.aimPos-25), mask=img_muzzleflash)   # 총구 화염 Draw
            my_weapon.collision_check(my_enemy, "aim")
            my_weapon.Fire()
            
        # B Pressed = Grenade Throw
        if not joystick.button_B.value and my_weapon.ThrowControl() and joystick.button_A.value == True and my_weapon.grenades != 0: 
            my_weapon.Throw()
                
        # A + B Pressed = Air Bombardment
        if not joystick.button_A.value and not joystick.button_B.value and my_weapon.airbombardmentCount == True: # Air Bombardment
            my_weapon.airbombardment = True
            my_weapon.airbombardmentCount = False

           
        my_weapon.move(command) # 캐릭터 무브 함수에 커맨드를 넣어줌
        my_weapon.FireControl()
        my_weapon.ThrowControl()

                        
        my_enemy.ZombieSpawn()
        if my_enemy.ZombieSpawn(): # 좀비 스폰
            my_enemy.zombies_list.append(Zombie(my_enemy.zombie_spawn_position[my_enemy.zombie_turn]))

                    
        for zombie in my_enemy.zombies_list: # 좀비 Draw - 점점 커짐
            if zombie.zPos < 3:
                my_image.paste(im=img_zombie1, box=(tuple(zombie.spawn_position-32)), mask=img_zombie1)
            elif zombie.zPos < 6:
                my_image.paste(im=img_zombie2, box=(tuple(zombie.spawn_position-32)), mask=img_zombie2)
            elif zombie.zPos < 9:
                my_image.paste(im=img_zombie3, box=(tuple(zombie.spawn_position-32)), mask=img_zombie3)
            elif zombie.zPos < 12:
                my_image.paste(im=img_zombie4, box=(tuple(zombie.spawn_position-32)), mask=img_zombie4)
            elif zombie.zPos < 15:
                my_image.paste(im=img_zombie5, box=(tuple(zombie.spawn_position-32)), mask=img_zombie5)
            elif zombie.zPos < 18:
                my_image.paste(im=img_zombie6, box=(tuple(zombie.spawn_position-32)), mask=img_zombie6)
            elif zombie.zPos < 21:
                my_image.paste(im=img_zombie7, box=(tuple(zombie.spawn_position-32)), mask=img_zombie7)
            elif zombie.zPos < 24:
                my_image.paste(im=img_zombie8, box=(tuple(zombie.spawn_position-32)), mask=img_zombie8)
            elif zombie.zPos < 27:
                my_image.paste(im=img_zombie9, box=(tuple(zombie.spawn_position-32)), mask=img_zombie9)
            elif zombie.zPos < 31:
                my_image.paste(im=img_zombie10, box=(tuple(zombie.spawn_position-32)), mask=img_zombie10)
            elif zombie.zPos < 35:
                my_image.paste(im=img_zombie11, box=(tuple(zombie.spawn_position-32)), mask=img_zombie11)
            elif zombie.zPos < 40:
                my_image.paste(im=img_zombie12, box=(tuple(zombie.spawn_position-32)), mask=img_zombie12)
            elif zombie.zPos < 45:
                my_image.paste(im=img_zombie13, box=(tuple(zombie.spawn_position-32)), mask=img_zombie13)
            elif zombie.zPos < 50:
                my_image.paste(im=img_zombie14, box=(tuple(zombie.spawn_position-32)), mask=img_zombie14)
            else:
                my_image.paste(im=img_zombie15, box=(tuple(zombie.spawn_position-32)), mask=img_zombie15)

            zombie.move() # 좀비 Move
            
            if zombie.spawn_position[1] > 210: # 좀비가 아래 상태바 통과 시 attack
                zombie.Attack(zombie, my_enemy, my_weapon)
                if len(my_weapon.hp_list) <= 0: # 체력이 0이 되면 Fail
                    Fail()

                    
        if my_weapon.nowThrowing == True: # 수류탄 던지기
            if my_weapon.greTargetPos[1] < throwPos[1]:
                # 수류탄 Draw
                if greRotation == 4: # 수류탄 회전
                    greRotation = 1
                else:
                    greRotation += 1
                greList = {1 : img_grenade1, 2 : img_grenade2, 3 : img_grenade3, 4 : img_grenade4}
                my_image.paste(greList[greRotation], tuple(throwPos-20), mask=greList[greRotation])

                
                # 수류탄 xy 좌표 이동
                throwPos[1] -= math.sin(math.radians(my_weapon.throwAngle)) * 8 * -1
                if my_weapon.greTargetPos[0] < throwPos[0]:
                    throwPos[0] -= math.cos(math.radians(my_weapon.throwAngle)) * 8
                elif my_weapon.greTargetPos[0] > throwPos[0]:
                    throwPos[0] += math.cos(math.radians(my_weapon.throwAngle)) * 8

            else:
                # 수류탄 이펙트 Draw
                my_image.paste(img_greeffect, tuple(my_weapon.greTargetPos-75), mask=img_greeffect)  
                my_weapon.collision_check(my_enemy, "gre") # 충돌 확인

                
                # my_draw.polygon((my_weapon.greCenter[0], my_weapon.greCenter[1],
                #                  my_weapon.greCenter[0], my_weapon.greCenter[3],
                #                  my_weapon.greCenter[2], my_weapon.greCenter[3],
                #                  my_weapon.greCenter[2], my_weapon.greCenter[1]), fill=(0,0,0))


                throwPos = np.array([120,210])
                my_weapon.nowThrowing = False
                
        if my_weapon.airbombardment == True:
            randXPos = random.randint(-115,55)
            randYPos = random.randint(-95,35)
            my_image.paste(img_airbombardment, box = (my_weapon.airplanePos[0]+randXPos, my_weapon.airplanePos[1]+randYPos), mask=img_airbombardment) # 70x60
            randXPos = random.randint(-115,55)
            randYPos = random.randint(-95,35)
            my_image.paste(img_airbombardment, box = (my_weapon.airplanePos[0]+randXPos, my_weapon.airplanePos[1]+randYPos), mask=img_airbombardment) # 70x60
            randXPos = random.randint(-115,55)
            randYPos = random.randint(-95,35)
            my_image.paste(img_airbombardment, box = (my_weapon.airplanePos[0]+randXPos, my_weapon.airplanePos[1]+randYPos), mask=img_airbombardment) # 70x60

            my_image.paste(img_airplane, box = (my_weapon.airplanePos[0]-80, my_weapon.airplanePos[1]-65), mask=img_airplane) # 160x130
            my_weapon.Airbombardment()
            my_weapon.collision_check(my_enemy, "air") # 충돌 확인

                    
        
        # 상태 바 Draw
        my_image.paste(im=img_statusbar, box=(0,0), mask=img_statusbar)                     
        
        # 점수 Draw
        my_draw.text((160, 0), str(my_weapon.score), font=fnt, fill=(211,99,110))           
        
        # 수류탄 개수 Draw
        my_draw.text((112, 211), str(my_weapon.grenades), font=fnt, fill=(211,99,110))      
        
        # 수류탄 카운트 Draw
        if my_weapon.throw_speed < 17:
            my_image.paste(im=img_grenadetimer1, box=(0,0), mask=img_grenadetimer1)
        elif my_weapon.throw_speed < 34:
            my_image.paste(im=img_grenadetimer2, box=(0,0), mask=img_grenadetimer2)
        elif my_weapon.throw_speed < 50:
            my_image.paste(im=img_grenadetimer3, box=(0,0), mask=img_grenadetimer3)
        
        # 체력 Draw
        for hpPos in my_weapon.hp_list:
            my_image.paste(im=img_hp, box=(hpPos), mask=img_hp)                             

        # 총알 Draw
        for bullet in my_weapon.bullets_list:
            my_image.paste(im=img_bullet, box=(tuple(bullet)), mask=img_bullet)              
              
                
        if len(my_weapon.bullets_list) == 0: # Reload
            my_weapon.weaponState = "reload"
        
        # RELOAD 텍스트 Draw 
        if my_weapon.weaponState == "reload":
            my_weapon.ReloadControl()
            my_image.paste(im=img_reload, box=(140, 210),mask=img_reload)            
        
        # 에임 드로우
        my_image.paste(img_aim, tuple(my_weapon.aimPos-25), mask=img_aim) 

        joystick.disp.image(my_image)
        

        

if __name__ == '__main__':
    main()