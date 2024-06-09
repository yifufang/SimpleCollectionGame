take look at the TO DO part.
player class is the player object
item class is the item object

### Note
<p>
in the __init__ section, stores the variables of the class. in player class, the __init__ initializes the player image, and set a height and width for the player. You need to write a player control script. make it move up, right, left, down according to your key press in the update function.

same for item class, it initialize the image, rect.x and rect.y the initial position. you need to assign the speed to them.
in the update function, you need to make the item move at the speed you assign. (they dont need player control, they should move on their own)

the update function happends on every frame, which means update function update based on time. as time goes on, the update function goes on.
</p>

### variables
the following are the varibales you will be using:

self.rect.x: the object's horizontal location
self.rect.y: the object's vertical location
PLAYER_SPEED: 50, given
ITEM_SPEED: 3, given
self.speed_x: the object's horizontal speed
self.speed_y: the object's vertical speed
### task

1. write a player direction cotrol.
for example, the following command moves the player to left with a speed of PLAYER_SPEED which is a constant speed which is given in setting.py

```
if keys[pygame.K_LEFT]:
    self.rect.x -= PLAYER_SPEED
```

2. assign a random speed to an item. using random.choice. (google if you dont know how to assign random value to an integer) the random value assigned should be larger than -ITEM_SPEED, and smaller than ITEM_SPEED. ITEM_SPEED is a constant value given
<br>
3. put the item moving at speed of self.speed_x and self.speed_y
(think about how it should move, when the item moves, the location should be changing right?)
