import peachy

class Lever(peachy.Entity):
    
    def __init__(self, x, y, on_pull, lock):
        peachy.Entity.__init__(self, x, y)
        self.group = 'interact lever'
        self.width = 10
        self.height = 10
        self.pulled = False
        self.on_pull = on_pull
        self.lock = lock

        self.sprite = peachy.utils.splice_image('assets/img/lever.png', 10, 10)

    def render(self):
        if self.pulled:
            peachy.graphics.draw(self.sprite[1], self.x, self.y)
        else:
            peachy.graphics.draw(self.sprite[0], self.x, self.y)

    def pull(self):
        if not self.pulled:
            exec self.on_pull
            self.pulled = True
        elif not self.lock:
            exec self.on_pull
            self.pulled = False
