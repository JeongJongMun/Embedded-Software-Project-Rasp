import numpy as np
import random

# 64X64 30X64
class Enemy:
    def __init__(self):
        # Zombie
        self.zombieList = [] # 좀비 리스트
        self.zombieSpawnTime = 30 # 좀비 스폰 시간
        self.zombieSpawnPos =((60,-30),(90,-30),(120,-30)) # 좀비 스폰 위치
        self.zombie_turn = 0 # 좀비 스폰 위치 순서
        
        # Boss
        self.bossPos = np.array([120,0]) # 스폰 위치
        self.bossCenter = np.array([self.bossPos[0]-50, self.bossPos[1]-50, self.bossPos[0]+50, self.bossPos[1]+50]) # 충돌 범위
        self.bossHp = 100 # 보스 체력
        self.bossStage = False # 보스 스테이지 시작 -> 일반 좀비 스폰 X
        self.rockList = [] # 보스가 던지는 돌 리스트
        self.rockSpawnTime = 0 # 돌 던지는 간격
        self.rockSpawnPos = ((70,50),(110,50),(150,50)) # 돌의 처음 스폰 위치
        
    # 좀비 스폰 함수
    def ZombieSpawn(self):
        print(self.zombieSpawnTime)
        if self.zombieSpawnTime >= 40 and self.bossStage == False: # 40 마다 좀비 스폰
            self.zombieSpawnTime = random.randint(0,30) # 40 ~ 10 사이 시간 랜덤으로 좀비 스폰
            self.zombie_turn = random.randint(0,2) # 좀비 스폰 위치 랜덤으로 설정
            return True
        elif self.zombieSpawnTime < 40:
            self.zombieSpawnTime += 1
            return False
    
    # 보스 움직임 함수
    def BossMove(self):
        if self.bossHp <= 0: # 체력 0되면 보스 물러나기
            self.bossPos[1] -= 3
            self.bossCenter = np.array([self.bossPos[0]-50, self.bossPos[1]-50, self.bossPos[0]+50, self.bossPos[1]+50])
            if self.bossPos[1] < -50: # 다 물러나면 Finish
                return "finish" 
        elif self.bossPos[1] < 80: # 보스 아래로 내려오기
            self.bossPos[1] += 3
            self.bossCenter = np.array([self.bossPos[0]-50, self.bossPos[1]-50, self.bossPos[0]+50, self.bossPos[1]+50])

    # 보스 돌 던지기 함수
    def BossAttack(self):
        if self.rockSpawnTime == 30: # 30 마다 Rock 스폰
            self.rockSpawnTime = random.randint(1,15) # 30 ~ 15 사이 시간 랜덤으로 돌 던지기
            self.zombie_turn = random.randint(0,2) # 돌 스폰 위치 랜덤으로 설정
            return True
        else:
            self.rockSpawnTime += 1
            return False