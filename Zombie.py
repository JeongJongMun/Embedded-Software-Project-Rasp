import numpy as np
import random

# 64X64 30X64
class Zombie:
    def __init__(self, position):
        self.spawn_position = np.array([position[0],position[1]]) # 스폰 위치
        self.zPos = 0 # Z 값 = 이미지 크기 키우기 위함
        self.position = np.array([self.spawn_position[0], self.spawn_position[1], self.spawn_position[0] + 64, self.spawn_position[1] + 64]) # 좀비 타격 판정 범위
        self.hp = 10
        self.LR = 0 # 좌우 와리가리 체크 변수
        self.moveSpeed = random.randint(2,5)

        
    def move(self):
        self.spawn_position[1] += self.moveSpeed # 이동 속도
        self.zPos += 1 # Z 값 = 이미지 크기 키우기 위함
        if self.LR == 20:
            self.LR = 0
        elif self.LR > 10:
            self.spawn_position[0] -= 2
            self.LR += 1
        else:
            self.spawn_position[0] += 2
            self.LR += 1
        # 좀비 타격 판정 범위 갱신
        self.position = np.array([self.spawn_position[0], self.spawn_position[1], self.spawn_position[0] + 64, self.spawn_position[1] + 64])
        

    def attack(self): # 아래 상태바 통과시 공격
        if self.spawn_position[1] > 210:
            return True
                