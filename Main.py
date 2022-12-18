from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
import math
from colorsys import hsv_to_rgb
from Zombie import Zombie
from Character import Character
from Enemy import Enemy
from Joystick import Joystick
from Rock import Rock

# my_draw.polygon((my_character.greCenter[0], my_character.greCenter[1],
#                  my_character.greCenter[0], my_character.greCenter[3],
#                  my_character.greCenter[2], my_character.greCenter[3],
#                  my_character.greCenter[2], my_character.greCenter[1]), fill=(0,0,0))

def main():
    
    joystick = Joystick()
    my_character = Character(joystick.width, joystick.height)
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_enemy = Enemy()
    joystick.disp.image(my_image)
    throwPos = np.array([120,210]) # 수류탄이 던져지는 위치
    greRotation = 1 # 수류탄 회전을 위한 변수
    rockRotation = 1 # Rock 회전을 위한 변수

    img_bosszombie = Image.open('/home/kau-esw/esw/ESW-Project/images/bosszombie.png', mode='r').convert('RGBA')    # 보스 좀비
    img_rock1 = Image.open('/home/kau-esw/esw/ESW-Project/images/rock.png', mode='r').convert('RGBA')               # 돌 1 - 회전에 따른 이미지
    img_rock2 = img_rock1.transpose(Image.ROTATE_90)                                                                # 돌 2
    img_rock3 = img_rock2.transpose(Image.ROTATE_90)                                                                # 돌 3
    img_rock4 = img_rock3.transpose(Image.ROTATE_90)                                                                # 돌 4

    img_zombie1 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie1.png', mode='r').convert('RGBA')          # 좀비 1 - 크기 변화에 따른 이미지
    img_zombie2 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie2.png', mode='r').convert('RGBA')          # 좀비 2
    img_zombie3 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie3.png', mode='r').convert('RGBA')          # 좀비 3
    img_zombie4 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie4.png', mode='r').convert('RGBA')          # 좀비 4
    img_zombie5 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie5.png', mode='r').convert('RGBA')          # 좀비 5
    img_zombie6 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie6.png', mode='r').convert('RGBA')          # 좀비 6
    img_zombie7 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie7.png', mode='r').convert('RGBA')          # 좀비 7
    img_zombie8 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie8.png', mode='r').convert('RGBA')          # 좀비 8
    img_zombie9 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie9.png', mode='r').convert('RGBA')          # 좀비 9
    img_zombie10 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie10.png', mode='r').convert('RGBA')        # 좀비 10
    img_zombie11 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie11.png', mode='r').convert('RGBA')        # 좀비 11
    img_zombie12 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie12.png', mode='r').convert('RGBA')        # 좀비 12
    img_zombie13 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie13.png', mode='r').convert('RGBA')        # 좀비 13
    img_zombie14 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie14.png', mode='r').convert('RGBA')        # 좀비 14
    img_zombie15 = Image.open('/home/kau-esw/esw/ESW-Project/images/zombie15.png', mode='r').convert('RGBA')        # 좀비 15
    
    img_grenadetimer1 = Image.open('/home/kau-esw/esw/ESW-Project/images/grenadetimer1.png', mode='r').convert('RGBA')  # 수류탄 타이머 1
    img_grenadetimer2 = Image.open('/home/kau-esw/esw/ESW-Project/images/grenadetimer2.png', mode='r').convert('RGBA')  # 수류탄 타이머 2
    img_grenadetimer3 = Image.open('/home/kau-esw/esw/ESW-Project/images/grenadetimer3.png', mode='r').convert('RGBA')  # 수류탄 타이머 3

    img_hp = Image.open('/home/kau-esw/esw/ESW-Project/images/hp.png', mode='r').convert('RGBA')                        # 체력(하트 아이콘)
    img_muzzleflash = Image.open('/home/kau-esw/esw/ESW-Project/images/muzzleflash.png', mode='r').convert('RGBA')      # 총 발사시 총구섬광
    img_statusbar = Image.open('/home/kau-esw/esw/ESW-Project/images/statusbar.png', mode='r').convert('RGBA')          # 상단, 하단 상태바
    img_fieldbackground = Image.open('/home/kau-esw/esw/ESW-Project/images/fieldbackground.png', mode='r')              # 고속도로 배경
    img_aim = Image.open('/home/kau-esw/esw/ESW-Project/images/aim.png', mode='r').convert('RGBA')                      # 에임
    img_bullet = Image.open('/home/kau-esw/esw/ESW-Project/images/bullet.png', mode='r').convert('RGBA')                # 총알 아이콘
    img_reload = Image.open('/home/kau-esw/esw/ESW-Project/images/reload.png', mode='r').convert('RGBA')                # 재장전 문구
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)                                     # 폰트
    img_grenade1 = Image.open('/home/kau-esw/esw/ESW-Project/images/grenade.png', mode='r').convert('RGBA')             # 수류탄 1 - 회전에 따른 이미지
    img_grenade2 = img_grenade1.transpose(Image.ROTATE_90)                                                              # 수류탄 2
    img_grenade3 = img_grenade2.transpose(Image.ROTATE_90)                                                              # 수류탄 3
    img_grenade4 = img_grenade3.transpose(Image.ROTATE_90)                                                              # 수류탄 4
    
    img_airplane = Image.open('/home/kau-esw/esw/ESW-Project/images/airplane.png', mode='r').convert('RGBA')                # 공중폭격 비행기
    img_airbombardment = Image.open('/home/kau-esw/esw/ESW-Project/images/airbombardment.png', mode='r').convert('RGBA')    # 공중폭격 이펙트

    img_greeffect = Image.open('/home/kau-esw/esw/ESW-Project/images/greeffect.png', mode='r').convert('RGBA')              # 수류탄 터지는 이펙트
    
    img_finish = Image.open('/home/kau-esw/esw/ESW-Project/images/finish.png', mode='r')                                    # 성공 화면
    img_fail = Image.open('/home/kau-esw/esw/ESW-Project/images/fail.png', mode='r')                                        # 실패 화면
    img_main = Image.open('/home/kau-esw/esw/ESW-Project/images/main.png', mode='r')                                        # 메인 화면
    img_kauemblem = Image.open('/home/kau-esw/esw/ESW-Project/images/kauemblem.png', mode='r')                              # 항공대 엠블럼


    def Start(): # 시작 화면
        while True:
            my_image.paste(im=img_main, box=(0,0), mask=img_main)                     
            joystick.disp.image(my_image)
            if not joystick.button_A.value: 
                break
            
    def Fail(): # 실패 화면
        while True:
            my_image.paste(im=img_fail, box=(0,0), mask=img_fail) # 실패 화면 Draw
            my_draw.text((140, 105), str(my_character.score), font=fnt, fill=(211,99,110)) # 스코어 Draw     
            joystick.disp.image(my_image)
            if not joystick.button_A.value: # 게임 진행하면서 수정된 값들 초기화
                my_character.hpList = [[0,0],[30,0],[60,0]]
                my_character.score = 0
                my_character.grenades = 3
                my_enemy.zombieList.clear()
                my_character.bulletList.clear()
                my_enemy.rockList.clear()
                my_character.Reload()
                my_enemy.bossHp = 100
                my_character.airbombardmentCount = True
                my_enemy.bossStage = False
                my_enemy.bossPos = np.array([120,0])
                my_enemy.bossCenter = np.array([my_enemy.bossPos[0]-50, my_enemy.bossPos[1]-50,
                                                 my_enemy.bossPos[0]+50, my_enemy.bossPos[1]+50])
                break
    def Finish(): # 성공 화면
        while True:
            my_image.paste(im=img_finish, box=(0,0), mask=img_finish)        
            my_image.paste(im=img_kauemblem, box=(95,140), mask=img_kauemblem)             
            my_draw.text((140, 105), str(my_character.score), font=fnt, fill=(211,99,110))           
            joystick.disp.image(my_image)
            if not joystick.button_A.value: # 게임 진행하면서 수정된 값들 초기화
                my_character.hpList = [[0,0],[30,0],[60,0]]
                my_character.score = 0
                my_character.grenades = 3
                my_enemy.zombieList.clear()
                my_character.bulletList.clear()
                my_enemy.rockList.clear()
                my_character.Reload()
                my_enemy.bossHp = 100
                my_character.airbombardmentCount = True
                my_enemy.bossStage = False
                my_enemy.bossPos = np.array([120,0])
                my_enemy.bossCenter = np.array([my_enemy.bossPos[0]-50, my_enemy.bossPos[1]-50,
                                                 my_enemy.bossPos[0]+50, my_enemy.bossPos[1]+50])
                break    
            
    Start() # 메인화면 시작        
    
    while True: # 게임 시작
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False} # 딕셔너리
        
        my_image.paste(im=img_fieldbackground, box=(0,0)) # 배경 Draw

        # Boss : 3000 점 이상 획득 시 시작
        if my_character.score >= 3000:
            if my_enemy.BossMove() == "finish": # 보스 물리침
                my_character.score += 10000
                Finish()
            my_enemy.bossStage = True
            my_image.paste(im=img_bosszombie, box=(tuple(my_enemy.bossPos-50)), mask=img_bosszombie)
            my_enemy.BossMove()
            my_enemy.BossAttack()
            if my_enemy.BossAttack():
                my_enemy.rockList.append(Rock(my_enemy.rockSpawnPos[my_enemy.zombie_turn])) # 돌 던지기

        
        # Rock Draw
        for rock in my_enemy.rockList:
            if rockRotation == 4: # 돌 회전을 위한 변수
                rockRotation = 1
            else:
                rockRotation += 1
            rockList = {1 : img_rock1, 2 : img_rock2, 3 : img_rock3, 4 : img_rock4} # 90도씩 회전되어 있음.
            my_image.paste(im=rockList[rockRotation], box=(tuple(rock.spawnPos-25)), mask=rockList[rockRotation])
            

            rock.move() # Rock Move
            
            if rock.spawnPos[1] > 210: # Rock 아래 상태바 통과 시 attack
                rock.Attack(rock, my_enemy, my_character)
                if len(my_character.hpList) <= 0: # 체력이 0이 되면 Fail
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
        if not joystick.button_A.value and joystick.button_B.value and len(my_character.bulletList) != 0 and my_character.FireControl() == True:
            my_image.paste(img_muzzleflash, tuple(my_character.aimPos-25), mask=img_muzzleflash)   # 총구 화염 Draw
            my_character.collision_check(my_enemy, "aim") # 충돌 체크
            my_character.Fire()
            
        # B Pressed = Grenade Throw
        if not joystick.button_B.value and my_character.ThrowControl() and joystick.button_A.value == True and my_character.grenades != 0: 
            my_character.Throw()
                
        # A + B Pressed = Air Bombardment
        if not joystick.button_A.value and not joystick.button_B.value and my_character.airbombardmentCount == True:
            my_character.airbombardment = True
            my_character.airbombardmentCount = False

           
        my_character.move(command) # 캐릭터 무브 함수에 커맨드를 넣어줌
        my_character.FireControl() # 총 발사 시간 컨트롤
        my_character.ThrowControl() # 수류탄 재사용 대기시간 컨트롤

                        
        my_enemy.ZombieSpawn()
        if my_enemy.ZombieSpawn(): # 좀비 스폰
            my_enemy.zombieList.append(Zombie(my_enemy.zombieSpawnPos[my_enemy.zombie_turn]))

                    
        for zombie in my_enemy.zombieList: # 좀비 Draw - 점점 커짐
            if zombie.zPos < 3:
                my_image.paste(im=img_zombie1, box=(tuple(zombie.spawnPos-32)), mask=img_zombie1)
            elif zombie.zPos < 6:
                my_image.paste(im=img_zombie2, box=(tuple(zombie.spawnPos-32)), mask=img_zombie2)
            elif zombie.zPos < 9:
                my_image.paste(im=img_zombie3, box=(tuple(zombie.spawnPos-32)), mask=img_zombie3)
            elif zombie.zPos < 12:
                my_image.paste(im=img_zombie4, box=(tuple(zombie.spawnPos-32)), mask=img_zombie4)
            elif zombie.zPos < 15:
                my_image.paste(im=img_zombie5, box=(tuple(zombie.spawnPos-32)), mask=img_zombie5)
            elif zombie.zPos < 18:
                my_image.paste(im=img_zombie6, box=(tuple(zombie.spawnPos-32)), mask=img_zombie6)
            elif zombie.zPos < 21:
                my_image.paste(im=img_zombie7, box=(tuple(zombie.spawnPos-32)), mask=img_zombie7)
            elif zombie.zPos < 24:
                my_image.paste(im=img_zombie8, box=(tuple(zombie.spawnPos-32)), mask=img_zombie8)
            elif zombie.zPos < 27:
                my_image.paste(im=img_zombie9, box=(tuple(zombie.spawnPos-32)), mask=img_zombie9)
            elif zombie.zPos < 31:
                my_image.paste(im=img_zombie10, box=(tuple(zombie.spawnPos-32)), mask=img_zombie10)
            elif zombie.zPos < 35:
                my_image.paste(im=img_zombie11, box=(tuple(zombie.spawnPos-32)), mask=img_zombie11)
            elif zombie.zPos < 40:
                my_image.paste(im=img_zombie12, box=(tuple(zombie.spawnPos-32)), mask=img_zombie12)
            elif zombie.zPos < 45:
                my_image.paste(im=img_zombie13, box=(tuple(zombie.spawnPos-32)), mask=img_zombie13)
            elif zombie.zPos < 50:
                my_image.paste(im=img_zombie14, box=(tuple(zombie.spawnPos-32)), mask=img_zombie14)
            else:
                my_image.paste(im=img_zombie15, box=(tuple(zombie.spawnPos-32)), mask=img_zombie15)

            zombie.move() # 좀비 Move
            
            if zombie.spawnPos[1] > 210: # 좀비가 아래 상태바 통과 시 attack
                zombie.Attack(zombie, my_enemy, my_character)
                if len(my_character.hpList) <= 0: # 체력이 0이 되면 Fail
                    Fail()


        # 수류탄 던지기      
        if my_character.nowThrowing == True: 
            if my_character.greTargetPos[1] < throwPos[1]:
                # 수류탄 Draw
                if greRotation == 4: # 수류탄 회전을 위한 변수
                    greRotation = 1
                else:
                    greRotation += 1
                greList = {1 : img_grenade1, 2 : img_grenade2, 3 : img_grenade3, 4 : img_grenade4} # 90도씩 회전된 수류탄들
                my_image.paste(greList[greRotation], tuple(throwPos-20), mask=greList[greRotation])

                
                # 수류탄 xy 좌표 이동
                throwPos[1] -= math.sin(math.radians(my_character.throwAngle)) * 8 * -1 # sin함수를 이용하여 수류탄 위로 이동
                if my_character.greTargetPos[0] < throwPos[0]:
                    throwPos[0] -= math.cos(math.radians(my_character.throwAngle)) * 8 # cos함수를 이용하여 수류탄 좌우로 이동
                elif my_character.greTargetPos[0] > throwPos[0]:
                    throwPos[0] += math.cos(math.radians(my_character.throwAngle)) * 8

            else: # 수류탄 이동 종료 시
                my_image.paste(img_greeffect, tuple(my_character.greTargetPos-75), mask=img_greeffect) # 수류탄 이펙트 Draw
                my_character.collision_check(my_enemy, "gre") # 충돌 확인
                throwPos = np.array([120,210]) # 처음 수류탄 위치 재 설정
                my_character.nowThrowing = False
        
        # 공중 폭격
        if my_character.airbombardment == True:
            randXPos = random.randint(-115,55) # 무작위 폭격 이펙트를 위한 xy값, 한번에 3개씩 폭격
            randYPos = random.randint(-95,35)
            my_image.paste(img_airbombardment, box = (my_character.airplanePos[0]+randXPos, my_character.airplanePos[1]+randYPos), mask=img_airbombardment) # 70x60
            randXPos = random.randint(-115,55)
            randYPos = random.randint(-95,35)
            my_image.paste(img_airbombardment, box = (my_character.airplanePos[0]+randXPos, my_character.airplanePos[1]+randYPos), mask=img_airbombardment) # 70x60
            randXPos = random.randint(-115,55)
            randYPos = random.randint(-95,35)
            my_image.paste(img_airbombardment, box = (my_character.airplanePos[0]+randXPos, my_character.airplanePos[1]+randYPos), mask=img_airbombardment) # 70x60

            my_image.paste(img_airplane, box = (my_character.airplanePos[0]-80, my_character.airplanePos[1]-65), mask=img_airplane) # 160x130 비행기 Draw
            my_character.Airbombardment() # 비행기 이동
            my_character.collision_check(my_enemy, "air") # 충돌 확인

                    
        
        # 상태 바 Draw
        my_image.paste(im=img_statusbar, box=(0,0), mask=img_statusbar)                     
        
        # 점수 Draw
        my_draw.text((160, 0), str(my_character.score), font=fnt, fill=(211,99,110))           
        
        # 수류탄 개수 Draw
        my_draw.text((112, 211), str(my_character.grenades), font=fnt, fill=(211,99,110))      
        
        # 수류탄 카운트 Draw
        if my_character.throwSpeed < 17:
            my_image.paste(im=img_grenadetimer1, box=(0,0), mask=img_grenadetimer1)
        elif my_character.throwSpeed < 34:
            my_image.paste(im=img_grenadetimer2, box=(0,0), mask=img_grenadetimer2)
        elif my_character.throwSpeed < 50:
            my_image.paste(im=img_grenadetimer3, box=(0,0), mask=img_grenadetimer3)
        
        # 체력 Draw
        for hpPos in my_character.hpList:
            my_image.paste(im=img_hp, box=(hpPos), mask=img_hp)                             

        # 총알 Draw
        for bullet in my_character.bulletList:
            my_image.paste(im=img_bullet, box=(tuple(bullet)), mask=img_bullet)              
              
        # 총알이 0개면 Reload
        if len(my_character.bulletList) == 0:
            my_character.weaponState = "reload"
        
        # RELOAD 텍스트 Draw 
        if my_character.weaponState == "reload":
            my_character.ReloadControl()
            my_image.paste(im=img_reload, box=(140, 210),mask=img_reload)            
        
        # 에임 드로우
        my_image.paste(img_aim, tuple(my_character.aimPos-25), mask=img_aim) 

        joystick.disp.image(my_image)
        

        

if __name__ == '__main__':
    main()