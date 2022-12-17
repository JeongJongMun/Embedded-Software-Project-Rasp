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
        self.rock = False
        self.phaseOneTime = 0
        self.rockPos = np.array([120,80])
        self.rockCenter = np.array([self.rockPos[0]-50, self.rockPos[1]-50, self.rockPos[0]+50, self.rockPos[1]+50])
        self.bossPhase = 0
        
    def ZombieSpawn(self):
        if self.zombie_spawn_time == 50 and self.bossStage == False: # 50 마다 좀비 스폰
            self.zombie_spawn_time = 0
            self.zombie_turn = random.randint(0,2) # 좀비 스폰 위치 랜덤으로 설정
            return True
        else:
            self.zombie_spawn_time += 1
            return False
    
    def BossMove(self):
        if self.bossPos[1] < 80:
            self.bossPos[1] += 3
        else:
            self.bossPhase = 1

    def BossPhaseOne(self, my_weapon):
        if self.phaseOneTime == 50:
            self.rock = True
            self.phaseOneTime = 0
        else:
            self.phaseOneTime += 1
        
        if self.rock == True:
            self.rockPos[1] += 1
            self.rockCenter = np.array([self.rockPos[0]-50, self.rockPos[1]-50, self.rockPos[0]+50, self.rockPos[1]+50])

            if self.rockPos[1] > 210:
                my_weapon.hp_list.pop() # 체력 감소
                self.rock = False
                self.rockPos = self.bossPos

        
    def BossPhaseOTwo(self):
        print("ZombieSpawn")