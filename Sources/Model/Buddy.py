from Observable import Observable


class Bone:
    def __init__(self, pt1, pt2, fix):
        self.pt1 = pt1
        self.pt2 = pt2
        self.fix = fix


class Buddy:
    def __init__(self):
        self.myBuddy = Observable(0)
        self.boddy = Bone((0, 0), (0, 1), None)
        self.r_leg = Bone((0, 0), (0.5, 0.5), self.boddy.pt1)
        self.l_leg = Bone((0, 0.5), (0.5, 0), self.boddy.pt1)
        self.r_arm = Bone((0, 0), (0.3, 0.3), self.boddy.pt2)
        self.l_arm = Bone((0, 0.3), (0.3, 0), self.boddy.pt2)

    def update(self):
        self.myBuddy.set({self.boddy,
                         self.r_leg, self.l_leg,
                         self.r_arm, self.l_arm})
