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


roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}]}



world.loadGraph(roomGraph)

# UNCOMMENT TO VIEW MAP
world.printRooms()

player = Player("Name", world.startingRoom)

# Code here

traversalPath = []
traversalGraph = {}

stack = Stack()
world = World()
roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
world.loadGraph(roomGraph)

world.printRooms()
player = Player("Name", world.startingRoom)



traversalPath = []
traversalGraph = {}
stack = Stack()

dirs = ['n', 's', 'e', 'w']
oppDirs = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

print(len(roomGraph))
while len(traversalGraph) < len(roomGraph):
    prevRoom = player.currentRoom.id
    print('\n starting loop OVER \n')
            
    if prevRoom not in traversalGraph:
        exits = {}
        for way in player.currentRoom.getExits():
            exits[way] = "?"
        traversalGraph[prevRoom] = exits
    exits = traversalGraph[prevRoom]
    print(prevRoom, traversalGraph, '\n \n')
    
    if 'n'

    for way in exits:
        print('looking', {way})
        if exits[way] == '?':
            
            player.travel(way)
            traversalPath.append(way)
            newRoom = player.currentRoom.id
            exits[way] = newRoom
            
            print('directions taken', traversalPath)
            print('exits at room before are:', exits)
            print('new room', newRoom, '\n')
            
            if newRoom in traversalGraph:
                print('YUUUUUP', player.currentRoom.getExits())
                player.travel(random.choice(player.currentRoom.getExits()))
                for way in player.currentRoom.getExits():
                    print(way)

                #player.travel(random.choice(player.currentRoom.getExits()))
                

            

            
            if newRoom not in traversalGraph:
                newRoom_exits = {}
                stack.push(newRoom)
                print(newRoom, 'PREVWOO')
                
                for way in player.currentRoom.getExits():
                    print('exits', player.currentRoom.getExits())
                    if way == oppDirs[traversalPath[-1]]:
                        newRoom_exits[way] = prevRoom
                    else:
                        newRoom_exits[way] = "?"
                        traversalGraph[newRoom] = newRoom_exits
                    print('newroom exits : ', newRoom_exits)

                else:
                    print('END \n TRAVERSAL GRAPH:',traversalGraph, '\n')
                    print(stack.pop())
                    backTrackDirection = stack.pop()
                    if backTrackDirection is None:
                        break
                    else:
                        player.travel(backTrackDirection)
                        traversalPath.append(backTrackDirection)

#####
#                                        #
#      017       002       014           #
#       |         |         |            #
#       |         |         |            #
#      016--015--001--012--013           #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#       |         |                      #
#       |         |                      #
#      009       005                     #
#       |         |                      #
#       |         |                      #
#      010--011--006                     #
#                                        #

#####
          
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

# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
