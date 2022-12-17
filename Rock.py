import numpy as np
import random

# 50x50
class Rock:
    def __init__(self, position):
        self.spawn_position = np.array([position[0],position[1]]) # 스폰 위치
        self.LR = 0 # 좌우 이동 체크 변수
        self.moveSpeed = random.randint(1,3) # 랜덤 이동속도
        # 타격 판정 범위
        self.center = np.array([self.spawn_position[0]-50, self.spawn_position[1]-50,
                                self.spawn_position[0]+50, self.spawn_position[1]+50])

    def move(self):
        self.spawn_position[1] += self.moveSpeed # 아래로 이동
        # 타격 판정 범위 갱신
        self.center = np.array([self.spawn_position[0]-50, self.spawn_position[1]-50,
                                self.spawn_position[0]+50, self.spawn_position[1]+50])
        

    def Attack(self, rock, my_enemy, my_weapon): # 아래 상태바 통과시 즉시 사망
            my_enemy.rockList.remove(rock)
            my_weapon.hp_list.clear() # 즉시 사망
                