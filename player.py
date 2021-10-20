import world as w
import mc_objects as mco


class Player:

    def __init__(self, world: w.World) -> None:
        self.health = 10
        self.hunger = 10
        self.max_inv_size = 10
        self.inv = [mco.NO_OBJECT] * self.max_inv_size
        self.inv_count = [0] * self.max_inv_size
        self.selectIndex = 0
        self.currentWorld = world

    def change_health(self, dif: int) -> None:
        self.health += dif

    def change_hunger(self, dif: int) -> None:
        self.hunger += dif

    def select_object(self, new_index: int) -> None:
        if 0 <= new_index <= self.max_inv_size:
            self.selectIndex = new_index

    def add_to_inv(self, mc_object: mco.McObject, pos: int, amount: int) -> None:

        if amount == 0:
            print("No item added.")
        elif amount <= mc_object.max_stack_count:
            if self.inv_count[pos] != 0:
                self.inv_count[pos] += amount
            else:
                self.inv[pos] = mc_object
                self.inv_count[pos] = amount
        else:
            print("Max stack count exceeded.")

    def use(self, x: int, y: int, z: int) -> None:

        holding_obj = self.inv[self.selectIndex]
        holding_obj.use()

        if holding_obj.object_type == "NO_TYPE":

            print("No item selected.")

        elif holding_obj.object_type == "Block":

            self.currentWorld.place(holding_obj, x, y, z)
            self.inv_count[self.selectIndex] -= 1
            if self.inv_count[self.selectIndex] == 0:
                print("No more " + holding_obj.name)
                self.inv[self.selectIndex] = mco.NO_OBJECT

        elif holding_obj.object_type == "Tool":

            print("Can't place a tool in the world.")

        else:
            print("Undefined action.")

    def hit(self, x: int, y: int, z: int):

        holding_obj = self.inv[self.selectIndex]
        holding_obj.hit()

        if holding_obj.object_type == "NO_TYPE":

            print("No item selected.")

        elif holding_obj.object_type == "Block":

            print("Can't hit with a block.")

        elif holding_obj.object_type == "Tool":

            self.currentWorld.hit(holding_obj, x, y, z)

            if mco.Tool(holding_obj).dur == 0:
                print(holding_obj.name + " has broken!")
                self.inv[self.selectIndex] = mco.NO_OBJECT

        else:
            print("Undefined action.")
