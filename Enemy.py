import numpy as np
import random

# 64X64 30X64
class Enemy:
    def __init__(self):
        # Zombie
        self.zombies_list = [] # 좀비 리스트
        self.zombie_spawn_time = 30 # 좀비 스폰 시간
        self.zombie_spawn_position =((50,-30),(90,-30),(130,-30)) # 좀비 스폰 위치
        self.zombie_turn = 0 # 좀비 스폰 위치 순서
        
        # Boss
        self.bossPos = np.array([120,0])
        self.bossCenter = np.array([self.bossPos[0]-50, self.bossPos[1]-50, self.bossPos[0]+50, self.bossPos[1]+50])
        self.bossHp = 100
        self.bossStage = False
        self.rockList = []
        self.rockSpawnTime = 0
        self.rockSpawnPos = ((50,80),(90,80),(130,80))
        self.bossPhase = 1
        
    def ZombieSpawn(self):
        if self.zombie_spawn_time == 50 and self.bossStage == False: # 50 마다 좀비 스폰
            self.zombie_spawn_time = 0
            self.zombie_turn = random.randint(0,2) # 좀비 스폰 위치 랜덤으로 설정
            return True
        else:
            self.zombie_spawn_time += 1
            return False
    
    def BossMove(self):
        if self.bossHp <= 0: # 체력 0되면 보스 물러나기
            self.bossPos[1] -= 3
            self.bossCenter = np.array([self.bossPos[0]-50, self.bossPos[1]-50, self.bossPos[0]+50, self.bossPos[1]+50])
            if self.bossPos[1] < -50:
                return "finish" 
        elif self.bossPos[1] < 80: # 보스 아래로 내려오기
            self.bossPos[1] += 3
            self.bossCenter = np.array([self.bossPos[0]-50, self.bossPos[1]-50, self.bossPos[0]+50, self.bossPos[1]+50])
            
        if self.bossHp <= 0:
            self.bossPos[1] -= 3

    def BossPhaseOne(self, my_weapon):
        if self.rockSpawnTime == 50: # 50 마다 Rock 스폰
            self.rockSpawnTime = 0
            self.zombie_turn = random.randint(0,2) # 스폰 위치 랜덤으로 설정
            return True
        else:
            self.zombie_spawn_time += 1
            return False
        

        
    def BossPhaseOTwo(self, my_weapon):
        print("ZombieSpawn")