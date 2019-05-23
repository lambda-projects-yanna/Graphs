from room import Room
from player import Player
from world import World

import random

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value): 
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

stack = Stack()

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.

# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}]}

roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}

world.loadGraph(roomGraph)

# UNCOMMENT TO VIEW MAP
world.printRooms()

player = Player("Name", world.startingRoom)

# Code here

traversalPath = []
traversalGraph = {}

while len(traversalGraph) < 2:
    currentRoom = player.currentRoom.id

    print(f"Current room: {currentRoom} - Explored {len(traversalGraph)} rooms, {len(traversalPath)} steps")

    if currentRoom not in traversalGraph:
        exits = {}
        print(player.currentRoom.getExits())
        print(player.currentRoom.id)
        for e in player.currentRoom.getExits():
            exits[e] = "?"
        traversalGraph[currentRoom] = exits
    exits = traversalGraph[currentRoom]
    print(f"    Exits: {exits}")

    dirs = ['n', 's', 'e', 'w']
    oppDirs = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    for way in dirs:
        print(way)

        if way in exits and exits[way] == '?':
            player.travel(way)
            traversalPath.append(way)
            print(traversalPath)
            newRoom = player.currentRoom.id
            print(newRoom)
            exits[way] = newRoom
            print(exits)

            if newRoom not in traversalGraph:
                print('nope')
                newRoom_exits = {}
                print(player.currentRoom.getExits())
                for e in player.currentRoom.getExits():
                    print(e)
                    newRoom_exits[e] = "?"
                    newRoom_exits[oppDirs[way]] = currentRoom
                    traversalGraph[newRoom] = newRoom_exits
            else: 
                traversalGraph[newRoom][oppDirs[way]] = currentRoom
            stack.push(oppDirs[way])

        else:
            backTrackDirection = stack.pop()
            if backTrackDirection is None:
                break
            player.travel(backTrackDirection)
            traversalPath.append(backTrackDirection)

# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)

for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")


# UNCOMMENT TO WALK AROUND

player.currentRoom.printRoomDescription(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    else:
        print("I did not understand that command.")
