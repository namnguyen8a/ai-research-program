class FlyingCreature:
    def fly(self):
        return "Can fly"

class MythicalCreature:
    def roar(self):
        return "Can roar"
    
class Griffin(FlyingCreature, MythicalCreature):
    pass

g = Griffin()
print(g.fly())
print(g.roar())