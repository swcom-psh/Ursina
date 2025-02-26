from ursina import * #ursina의 모든 객체(함수, 클래스, 변수 등)를 가져온다.
from ursina.prefabs.first_person_controller import FirstPersonController



__ = False


app = Ursina()

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            speed = 10,
            model = 'cube',
            collider = 'mesh',
            scale = 1,
            position = (0,0,0)
        )
        
class Warp():
    def __init__(self):
        super().__init__(
            
        )

class Exit(Entity):
    def __init__(self, i, j):
        super().__init__(
            model = 'cube',
            scale = (5, 5, 5),
            color = color.black90,
            position = (i*5, 0, j*5),
            collider = 'box'
        )
        self.player = player
        self.text = Text(
            text = 'Escape complete // GG !!',
            scale = 2,
            origin = (0, 0),
            visible = False
        )
    def update(self):
        self.clear()    
    def clear(self):
        dis = (self.player.position - self.position).length()
        print(dis)
        if dis < 3:
            self.player.enabled = False
            self.text.visible = True



def input(key):
    if key == 'escape':
        app.quit()

player = Player()
EditorCamera()

duck = Entity(
    model = 'model/duck.fbx',
    texture = 'images/duck.jpg',
    scale = 0.1,
    rotation = (0,90,0),
    collider = 'mesh'
)

MAP = [
    [11,12,13,14,15,16,17,18,'e',20,22,22,22,22,23,24,25,26,27,28,29,30,31,33,33,22,33,22,33],
    [11,12,13,14,15,16,17,__,__,__,__,__,__,__,23,24,25,26,__,28,__,__,31,__,33,22,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,__,22,__,23,__,__,__,__,28,29,__,__,__,33,22,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,__,22,__,23,__,25,26,__,__,29,__,31,__,33,22,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,__,22,__,23,__,25,__,27,__,29,__,31,__,33,22,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,__,22,__,__,__,__,__,27,__,29,30,31,__,33,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,__,22,22,23,24,__,26,27,__,__,__,31,__,__,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,__,__,__,23,__,__,26,__,28,29,__,31,33,33,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,__,23,24,__,26,__,28,29,__,31,33,33,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,__,__,__,25,26,__,28,29,__,__,__,__,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,22,23,__,25,__,__,28,__,30,31,33,33,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,22,23,__,__,__,27,28,__,__,__,33,33,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,22,23,__,25,26,27,28,29,30,__,33,33,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,22,23,__,25,__,__,__,__,__,__,33,33,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,22,23,__,25,__,27,28,29,30,__,33,33,__,33,22,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,22,23,__,__,__,27,__,__,30,__,33,__,__,__,__,33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,22,23,24,25,26,27,28,__,__,__,33,__,22,33,'e',33],
    [11,12,13,14,15,16,17,18,__,20,22,22,22,22,23,24,25,26,27,28,29,30,__,__,__,__,33,__,33],
    [11,12,13,14,15,16,17,18,19,20,22,22,22,22,23,24,25,26,27,28,29,30,31,33,33,22,33,'p',33]
    
]

for i in range(len(MAP)):
    for j in range( len( MAP[i] ) ):
        if MAP[i][j]:
            if MAP[i][j] =='p':
                player.position = (i * 5, 0, j * 5)
                continue

            if MAP[i][j] == 'e':
                exitdoor = Exit(i,j)
                continue

            if MAP[i][j] =='d':
                duck.position = (i * 5, 0, j * 5)
                continue
            wall = Entity(
                model = 'cube',
                #color = color.red,
                scale = (5 ,5 ,5),
                position = (i * 5, 1, j * 5),
                collider = 'box',
                texture = 'images/wall.jpg'
                )



ground = Entity(
    model = 'plane',
    color = color.gray,
    position = (0, 0, 0),
    scale = (2000, 1, 2000), 
    collider = 'mesh'#물체의 충돌판정 형태를 설정합니다. mesh: 그물망형태
)

app.run()
