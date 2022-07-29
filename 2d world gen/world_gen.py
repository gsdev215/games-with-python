import random , typing, os ,math

from jsonhandeler import JsonHandeler as jh

from PIL import Image,ImageColor,ImageDraw,ImageFont

class World_gen:
    def world(size:tuple):
        x , y = size[0], size[1]
        data = jh("world.json")
        world = data.fetch_data()
        for i in range(y):
            v = []
            for j in range(x):
                v.append({"type": "a"})
            world.append(v)
        data.save(world)

    def tree(world,val,n):
        p = world
        try:
            p[val-4][n+1]["type"] = "d"
        except:
            return world
        world[val-1][n]["type"] = "b"
        world[val-2][n]["type"] = "b"
        world[val-3][n]["type"] = "b"
        world[val-4][n]["type"] = "b"
        world[val-4][n-1]["type"] = "d"
        world[val-4][n+1]["type"] = "d"
        world[val-5][n]["type"] = "d"
        return world

    def grass_deep(world,val,n):
        p = world
        try:
            p[val+2][n-1]["type"] = "d"
        except:
            return world
        world[val+1][n+1]["type"] = "d"
        world[val+1][n-1]["type"] = "d"
        world[val+2][n-1]["type"] = "d"

        return world

    def cloud(world,val,n):
        p = world
        try:
            p[val-10][n+2]["type"] = "w"
        except:
            return world
        world[val-10][n+1]["type"] = "w"
        world[val-10][n-1]["type"] = "w"
        world[val-10][n+2]["type"] = "w"
        world[val-10][n]["type"] = "w"
        world[val-11][n]["type"] = "w"
        world[val-11][n+1]["type"] = "w"


        return world
    def gen_tern(surface_limit:int,size:tuple):
        sky_start = surface_limit +4
        data = jh("world.json")
        world = data.fetch_data()

        val = random.randint(surface_limit+1,sky_start-1)

        n = 0
        world[val][n]["type"] = "d"
        for k in range(1,1000):
                try:
                    world[val+k][n]["type"] = "s"
                except:
                    break
        for i in range(0,size[0]):
            c = random.choice([1,0,-1])
            n += 1
            val += c
            if n > size[0]-1:
                break
            world[val][n]["type"] = "d"
            world = World_gen.tree(world,val,n) if random.randint(1,7) == 1 else world
            world = World_gen.grass_deep(world,val,n) if random.randint(1,2) == 1 else world
            world = World_gen.cloud(world,val,n) if random.randint(1,10) == 1 else world
            for k in range(1,100):
                try:
                    world[val+k][n]["type"] = "s"
                except:
                    break
        data.save(world)
        #for b in range((size[1]-surface_limit)*size[0]):



size = (100,45)

World_gen.world(size)
World_gen.gen_tern(35,size)

def list_list_px_to_img(List,bg="WHITE"):
    img2=Image.new('RGB', (1000*2, 1000), bg)
    im = ImageDraw.Draw(img2)
    posy = 0
    for i in List:
            posx = 0
            for n in i:
                if n["type"] == "a":
                    c =  ImageColor.getrgb("BLUE")
                elif n["type"] == "d":
                    c = ImageColor.getrgb("GREEN")
                elif n["type"] == "s":
                    c = ImageColor.getrgb("Grey")
                elif n["type"] == "b":
                    c = ImageColor.getrgb("brown")
                elif n["type"] == "w":
                    c = ImageColor.getrgb("white")
                
                im.rectangle((posx*20+1,posy*20+1,posx*20+1+18,posy*20+1+18),c)
                posx += 1
            posy += 1
    return img2

list_list_px_to_img(jh("world.json").fetch_data()).show()
jh("world.json").clear()