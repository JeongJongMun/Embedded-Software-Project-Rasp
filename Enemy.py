import numpy as np
import random

# 64X64 30X64
class Enemy:
    def __init__(self):
        self.zombies_list = []                                      # 좀비 리스트
        self.zombie_spawn_time = 0                                  # 좀비 스폰 시간
        self.first_spawn_position =((50,-30),(90,-30),(130,-30))    # 좀비 스폰 위치
        self.zombie_turn = 0                                        # 좀비 스폰 위치 순서
        
    def ZombieSpawn(self):
        self.zombie_spawn_time += 1
        
        if self.zombie_spawn_time == 60:
            self.zombie_spawn_time = 0
            self.zombie_turn = random.randint(0,2)
            return True
        else:
            return False