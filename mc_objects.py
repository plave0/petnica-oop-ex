from dataclasses import dataclass


class McObject:

    def __init__(self, name: str, object_type: str, max_stack_count: int) -> None:
        self.name = name
        self.object_type = object_type
        self.max_stack_count = max_stack_count

    def use(self):
        pass

    def hit(self):
        pass


@dataclass
class ToolType:
    name: str
    dur: int


@dataclass
class BlockType:
    name: str
    tool: ToolType


class Block(McObject):

    def __init__(self, block_type: BlockType) -> None:
        super().__init__(block_type.name, "Block", 64)
        self.tool = block_type.tool

    def use(self):
        pass

    def hit(self):
        pass


class Tool(McObject):

    def __init__(self, tool_type: ToolType) -> None:
        super().__init__(tool_type.name, "Tool", 1)
        self.dur = tool_type.dur

    def use(self):
        pass

    def hit(self):
        self.dur -= 1


class Tools:
    Shovel = ToolType("Shovel", 5)
    Pickaxe = ToolType("Pickaxe", 5)
    NoTool = None


class Blocks:
    Stone = BlockType("Stone", Tools.Pickaxe)
    Grass = BlockType("Grass", Tools.Shovel)
    Air = BlockType("Air", Tools.NoTool)
    NoBlock = None


NO_OBJECT = McObject("NO_OBJ", "NO_TYPE", 0)
