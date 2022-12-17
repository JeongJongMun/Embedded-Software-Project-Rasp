import numpy as np
import math

class Character:
    def __init__(self, width, height):
        self.state = None # 에임 움직임 상태
        self.weaponState = None # 무기 상태
        self.airbombardment = False # 현재 공중 폭격 하고있는가 
        
        self.aimPos = np.array([int(width/2), int(height/2)]) # Aim 위치
        self.aimCenter = np.array([self.aimPos[0]-15, self.aimPos[1]-15 , self.aimPos[0]+15, self.aimPos[1]+15]) # Fire 시 충돌 범위
        self.score = 0 # 점수
        self.hpList = [[0,0],[30,0],[60,0]] # 체력 리스트
        
        # Fire
        self.fireSpeed = 0 # 발사 속도 카운트
        self.reloadSpeed = 0 # 재장전 속도 카운트
        self.bulletList = [(-5, 210), (8, 210), (21, 210), (34, 210), (47, 210)] # 총알 위치
        
        # Throw - grenade
        self.throwSpeed = 0 # 수류탄 투척 재사용 대기시간 카운트
        self.grenades = 3 # 수류탄 개수 - 처음에 3개
        self.greTargetPos = 0 # 수류탄 버튼 눌렀을때 에임 위치 저장
        self.greCenter = 0 # 수류탄 터지는 범위
        self.nowThrowing = False # 현재 수류탄이 날라가고 있는가
        self.throwAngle = 0 # greTargetPos까지 거리를 계산하기 위해 각도 저장
        
        # Air Bombardment
        self.airplanePos = np.array([120, 270]) # 비행기 위치
        self.airplaneCenter = np.array([self.airplanePos[0]-200, self.airplanePos[1]-65,
                                        self.airplanePos[0]+200, self.airplanePos[1]+65]) # 비행기 폭격 범위
        self.airbombardmentCount = True # 폭격은 게임당 한번만 가능
        
    # 에임 움직임 함수
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
    
    # 총 재장전 함수
    def Reload(self):
        self.bulletList = [(-5, 210), (8, 210), (21, 210), (34, 210), (47, 210)] # 총알 재장전
        self.weaponState = None
        
    # 재장전 시간 카운트 함수
    def ReloadControl(self):
        if self.reloadSpeed < 30: # 30 마다 재장전
            self.reloadSpeed += 1
        else:
            self.reloadSpeed = 0
            self.Reload()
    
    # 총 발사
    def Fire(self):
        if len(self.bulletList) != 0:
            self.bulletList.pop()
            self.weaponState = "fire"
        
    # 총 발사 속도 카운트 함수
    def FireControl(self):
        if self.fireSpeed < 7: # Fire 속도 == while문이 7번 돌때마다 1발
            self.fireSpeed += 1
        if self.weaponState == "fire": # Fire 시
            self.fireSpeed = 0
            self.weaponState = None
        if self.fireSpeed == 7: # Fire 가능
            return True

    # 수류탄 던지기 함수
    def Throw(self):
        if self.grenades != 0:
            self.weaponState = "throw"
            self.grenades -= 1
            self.greTargetPos = self.aimPos.copy() # 에임의 포지션을 카피
            self.greCenter = np.array([self.greTargetPos[0]-100, self.greTargetPos[1]-100,
                                       self.greTargetPos[0]+100, self.greTargetPos[1]+100]) # 수류탄 폭발 범위 설정
            self.nowThrowing = True
    
    # 수류탄 재사용 대기시간 카운트 함수
    def ThrowControl(self):
        if self.throwSpeed < 50: # Throw 속도 == while문이 50번 돌때마다 1번
            self.throwSpeed += 1
        if self.weaponState == "throw": # Throw 시
            self.throwSpeed = 0
            # 각도 계산
            if self.greTargetPos[0] > 120: # 에임이 중간보다 오른쪽에 있을 경우
                temp = math.atan2(self.greTargetPos[1]-210, self.greTargetPos[0]-120) # 라디안으로 계산
            else: # 에임이 중간보다 왼쪽에 있을 경우
                temp = math.atan2(self.greTargetPos[1]-210, 120-self.greTargetPos[0]) # 라디안으로 계산
            self.throwAngle = math.degrees(temp) # 라디안을 도로 바꿈
            self.weaponState = None
        if self.throwSpeed == 50: # Throw 가능
            return True
        
        
    # 충돌 체크 : 총, 수류탄, 공중 폭격으로 나뉨
    def collision_check(self, my_enemy, check):
        for zombie in my_enemy.zombieList: # 모든 좀비에 대해 충돌 체크
            if check == "aim":
                collision = self.overlap(self.aimCenter, zombie.center, "aim")
            elif check == "gre":
                collision = self.overlap(self.greCenter, zombie.center, "gre")
            elif check == "air":
                collision = self.overlap(self.airplaneCenter, zombie.center, "air")
            
            if collision: # 좀비에 대해 충돌시 100 점
                my_enemy.zombieList.remove(zombie)
                self.score += 100
        
        # 모든 돌에 대해 충돌 체크
        for rock in my_enemy.rockList:
            if check == "aim":
                collision = self.overlap(self.aimCenter, rock.center, "aim")
            elif check == "gre":
                collision = self.overlap(self.greCenter, rock.center, "gre")
            elif check == "air":
                collision = self.overlap(self.airplaneCenter, rock.center, "air")
            
            if collision: # 돌에 대해 충돌시 300 점
                my_enemy.rockList.remove(rock)
                self.score += 300
                
        # 보스 충돌 시
        if my_enemy.bossStage == True:   
            if check == "aim":
                collision = self.overlap(self.aimCenter, my_enemy.bossCenter, "aim")
            elif check == "gre":
                collision = self.overlap(self.greCenter, my_enemy.bossCenter, "gre")
            elif check == "air":
                collision = self.overlap(self.airplaneCenter, my_enemy.bossCenter, "air")
                
            if collision: # 총은 데미지 5, 수류탄은 데미지 10, 공중 폭격은 3의 데미지를 여러번 입힘
                if check == "aim":
                    my_enemy.bossHp -= 5
                elif check == "gre":
                    my_enemy.bossHp -= 10
                elif check == "air":
                    my_enemy.bossHp -= 3
                print("Boss HP : ",my_enemy.bossHp)

    # 겹치는지 확인
    def overlap(self, ego_aimPos, other_aimPos, check): # ego = 자기 자신
        if check == "aim": # 에임은 목표물 안에 에임이 들어가야 겹친다 판정
            return ego_aimPos[0] > other_aimPos[0] and ego_aimPos[1] > other_aimPos[1] \
                 and ego_aimPos[2] < other_aimPos[2] and ego_aimPos[3] < other_aimPos[3]
                 
        else: # 수류탄과 공중 폭격은 공격 범위 안에 목표물이 들어와야 겹친다 판정
            return ego_aimPos[0] < other_aimPos[0] and ego_aimPos[1] < other_aimPos[1] \
                 and ego_aimPos[2] > other_aimPos[2] and ego_aimPos[3] > other_aimPos[3]
    
    # 공중 폭격
    def Airbombardment(self):
        if self.airplanePos[1] > -130: # 비행기 이동
            self.airplanePos[1] -= 5
            self.airplaneCenter = np.array([self.airplanePos[0]-200, self.airplanePos[1]-65, self.airplanePos[0]+200, self.airplanePos[1]+65])

        else: # 이동 완료 시 비행기 위치 재 설정
            self.airplanePos = np.array([120, 270])
            self.airplaneCenter = np.array([self.airplanePos[0]-200, self.airplanePos[1]-65, self.airplanePos[0]+200, self.airplanePos[1]+65])
            self.airbombardment = False