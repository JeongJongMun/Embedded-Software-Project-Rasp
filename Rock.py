import numpy as np
import random

# 50x50
class Rock:
    def __init__(self, position):
        self.spawnPos = np.array([position[0],position[1]]) # 스폰 위치
        self.moveSpeed = random.randint(2,4) # 랜덤 이동속도
        # 타격 판정 범위
        self.center = np.array([self.spawnPos[0]-50, self.spawnPos[1]-50,
                                self.spawnPos[0]+50, self.spawnPos[1]+50])

    def move(self):
        self.spawnPos[1] += self.moveSpeed # 아래로 이동
        # 타격 판정 범위 갱신
        self.center = np.array([self.spawnPos[0]-50, self.spawnPos[1]-50,
                                self.spawnPos[0]+50, self.spawnPos[1]+50])
        

    def Attack(self, rock, my_enemy, my_weapon): # 아래 상태바 통과시 즉시 사망
            my_enemy.rockList.remove(rock) # 돌을 리스트에서 삭제
            my_weapon.hpList.clear() # 즉시 사망
                