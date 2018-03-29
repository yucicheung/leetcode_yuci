# -*- coding : utf-8 -*-
# Depth-First Search
from pprint import pprint

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        rows = len(board)
        cols = len(board[0])
        click = tuple(click)
        
        def neighbors(x, y):
            for dx in xrange(-1,2):
                for dy in xrange(-1,2):
                    if 0<=x+dx<rows and 0<=y+dy<cols:
                        yield (x+dx,y+dy)
                        
        to_see_stack = []
        seen = set()
        
        to_see_stack.append(click)
        while to_see_stack:
            r,c = to_see_stack.pop()
            if board[r][c]=='M':
                board[r][c] = 'X'
            else:
                bombs_adj = sum((board[newr][newc]=='M') for newr,newc in neighbors(r,c))
                if bombs_adj:
                    board[r][c] = str(bombs_adj)
                    # seen.add(board[r][c])
                else:
                    board[r][c] = 'B'
                    for new in neighbors(r,c):
                        if new not in seen and board[new[0]][new[1]] in 'ME':
                            to_see_stack.append(new)
                            seen.add(new)
                        
        return board


