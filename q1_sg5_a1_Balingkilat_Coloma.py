class hero:
    def __init__(self,hero,hp=100):
        self.hero=hero
        self.hp=hp
    def take_damage(self,damage=10):
        self.hp -= damage
hero1=hero("Arthur")
hero2=hero("Morgana")
hero1.take_damage()
print(hero1.hero,"got hit and has",hero1.hp,"hp, but", hero2.hero, "got hit and has", hero2.hp,"hp.")
              
