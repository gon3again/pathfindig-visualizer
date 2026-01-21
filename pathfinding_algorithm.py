import pygame
from node import Node
from constants import *



class Pathfinder():
    def __init__(self, grid, start_node, end_node):
        self.grid = grid
        self.start_node:Node = start_node
        self.end_node:Node = end_node
           
            
    def find_path(self):
        #adding unvisited Nodes
        unvisited_nodes:list[Node] = []
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                unvisited_nodes.append(self.grid[x][y])    

        looping = True
        visited_nodes = [self.start_node]

        cur_node = self.start_node
        cur_path = cur_node.get_path()
        #Loop_______________________________________________________
        while looping:
            cur_neighbours = cur_node.get_neighbours()
            for neigh in cur_neighbours:
                neigh.set_dist(cur_node.get_dist()+1,cur_path)#adding distance for neighbour

            unvisited_nodes.remove(cur_node)
            #select lowest distance
            lowest_dist = float("inf")
            lowest_dist_node:Node = None
            for node in unvisited_nodes: 
                if node.get_dist() < lowest_dist:
                    lowest_dist = node.get_dist()
                    lowest_dist_node = node

            print(f"unvisited: {len(unvisited_nodes)}")
            if lowest_dist_node != None:
                
                lowest_dist_node.visit()
                
                
                cur_neighbours = lowest_dist_node.get_neighbours()
                cur_node = lowest_dist_node
            else:
                looping = false
            

        # print(f"low dis node: {lowest_dist_node.distance}")
        # print(f"low dis node: {lowest_dist_node.get_pos()}")



        

