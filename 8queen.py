#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:04:41 2019

@author: robinroy peter
@blogger: robinrobotic.blogspot.com
"""

def backtrack(Q,r):
    if r==len(Q):
        print_chess_board(Q)
    else :
        for j in range(len(Q)):
            legal = True
            for i in range(r):
                if((Q[i]==j)or(Q[i]==j+r-i)or(Q[i]==j-r+i)):
                    legal = False               
            if legal :
                Q[r]=j
                backtrack(Q,r+1)

def print_chess_board(d):
     chess_board=''
     for g in range((len(d)*3+6)):
         chess_board +="+"        
     chess_board += "\n"
     for i in range(len(d)):
         chess_board += "+  "
         for j in range(len(d)):
             if j==d[i]:
                 chess_board += " & "
             else:
                 chess_board += " - "
         chess_board += "  +\n"
     for g in range((len(d)*3+6)):
         chess_board +="+"        
     chess_board += "\n"
     print(chess_board)
             
    
    
def create_chess_board(size):
    mat =[]
    for i in range(size):
        mat.append(0)
    return mat
        

    
if __name__ == '__main__':
    print("==================================================")
    print("== N Queen Problem using Backtracking Algorithm ==")
    print("==            code by Robinroy Peter            ==")
    print("==================================================")
    size =input("input your chess board size : ")
    print("& -> Queen")
    print("- -> Empty slot")
    backtrack(create_chess_board(int(size)),0)
    print("=================================================")
    print("== Feel Free & Visit robinrobotic.blogspot.com ==")
    print("=================================================")
    
    

