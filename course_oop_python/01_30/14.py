class Gun:
    def __init__(self):
        self.n = 0

    def shoot(self):

        if self.n % 2 == 0:
            print('pif')
        else:
            print('paf')
        self.n += 1

    def shots_count(self):
        return self.n

    def shots_reset(self):
        self.n = 0


gun = Gun()
print(gun.shots_count())   # 0

gun.shoot()   # pif
gun.shoot()   # paf
print(gun.shots_count())   # 2

gun.shots_reset()
print(gun.shots_count())   # 0

gun.shoot()   # pif
print(gun.shots_count())   # 1