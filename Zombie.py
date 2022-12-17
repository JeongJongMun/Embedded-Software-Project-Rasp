import numpy as np
import random

# 64X64 30X64
class Zombie:
    def __init__(self, position):
        self.spawn_position = np.array([position[0],position[1]]) # 스폰 위치
        self.zPos = 0 # Z 값 = 이미지 크기 키우기 위함
        self.LR = 0 # 좌우 이동 체크 변수
        self.moveSpeed = random.randint(2,5) # 랜덤 이동속도
        # 좀비 타격 판정 범위
        self.center = np.array([self.spawn_position[0]-32, self.spawn_position[1]-32,
                                self.spawn_position[0]+32, self.spawn_position[1]+32])

    def move(self):
        self.spawn_position[1] += self.moveSpeed # 아래로 이동
        self.zPos += 1 # Z 값 = 이미지 크기 키우기 위함
        if self.LR == 20:
            self.LR = 0
        elif self.LR > 10: # 왼쪽으로 이동
            self.spawn_position[0] -= 2
            self.LR += 1
        else: # 오른쪽을 이동
            self.spawn_position[0] += 2
            self.LR += 1
        # 좀비 타격 판정 범위 갱신
        self.center = np.array([self.spawn_position[0]-32, self.spawn_position[1]-32,
                                self.spawn_position[0]+32, self.spawn_position[1]+32])
        

    def Attack(self,zombie, my_enemy, my_weapon): # 아래 상태바 통과시 공격
            my_enemy.zombies_list.remove(zombie)
            my_weapon.hp_list.pop() # 체력 감소
                