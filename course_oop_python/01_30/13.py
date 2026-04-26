class Gun:
    def __init__(self):
        self.n = 1

    def shoot(self):
        if self.n % 2 == 1:
            print('pif')
            self.n = 2
        else:
            print('paf')
            self.n = 1

gun = Gun()
gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
