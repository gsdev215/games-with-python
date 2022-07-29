import random

def world_gen():
    world1 = [[0 for x in range(1,50)]  for y in range(1,10)]
    return world1

def world_gen2(world):
    if x < 6:
        world[x+1][y] = 2
    

def world_gen_to_text(world2,x,y):
    display = f""
    n=0
    world2[y][x] = 1
    for i in world2:
        l =0 
        for k in world2[n]:
            if world2[n][l] == 0:
                display = display+ "#"
            else:
                display = display + "."
            l = l + 1
        n = n + 1
        display= f"{display}\n"
    world2[y][x] = 0
    del world2
    return display
    

x=random.randint(1,48)
y=random.randint(1,8)

world = world_gen()

print(world_gen_to_text(world,x,y))
while True:

    q = input(str(f"x for quit w for up , a for left,s for down,d for left \n enter:"))
    if q =="x":
        break
    if q == "w":
        y = y - 1
    if q == "a":
        x = x - 1
    if q == "s":
        y = y + 1
    if q == "d":
        x = x+ 1
    print(world_gen_to_text(world,x,y))