import turtle
import sys
import os
import random
import json

filename='doc.json'
record=[]
delta=[]
if os.path.exists(filename):
    with open(filename,'r') as fw:
        record=json.loads(fw.read())
        fw.close()

t=turtle.Turtle()
t.ht()
t.up()
turtle.tracer(False)

size=31
win=0
markstart=0
if size%2==0:
    size+=1

def checkaround(i,j):
    global chess
    global size
    if size-i>1 and chess[i+1][j]<0:
        return True
    elif size-i>1 and j>=1 and chess[i+1][j-1]<0:
        return True
    elif j>=1 and chess[i][j-1]<0:
        return True
    elif j>=1 and i>=1 and chess[i-1][j-1]<0:
        return True
    elif i>=1 and chess[i-1][j]<0:
        return True
    elif i>=1 and size-j>1 and chess[i-1][j+1]<0:
        return True
    elif size-j>1 and chess[i][j+1]<0:
        return True
    elif size-i>1 and size-j>1 and chess[i+1][j+1]<0:
        return True
    else:
        return False

def start(size=size):
    chess=[]
    for i in range(size):
        a=[]
        for j in range(size):
            a.append(0)
        chess.append(a)
    return chess

def action(chess,size=size):
    global win
    global delta
    global record
    for i in range(size):
        for j in range(size):
            if chess[i][j]>0:
                chess[i][j]=0
    mark=1
    for i in range(size):
        for j in range(size):
            if chess[i][j]==-1:
                #检测黑子赢
                if size-i>=5:
                    if chess[i][j]==-1 and chess[i+1][j]==-1 and chess[i+2][j]==-1 and chess[i+3][j]==-1 and chess[i+4][j]==-1:
                        win=1
                        draw(chess,'win')
                        return chess
                    if size-j>=5:
                        if chess[i][j]==-1 and chess[i+1][j+1]==-1 and chess[i+2][j+2]==-1 and chess[i+3][j+3]==-1 and chess[i+4][j+4]==-1:
                            draw(chess,'win')
                            win=1
                            return chess
                    if j>=4:
                        if chess[i][j]==-1 and chess[i+1][j-1]==-1 and chess[i+2][j-2]==-1 and chess[i+3][j-3]==-1 and chess[i+4][j-4]==-1:
                            draw(chess,'win')
                            win=1
                            return chess
                if size-j>=5:
                    if chess[i][j]==-1 and chess[i][j+1]==-1 and chess[i][j+2]==-1 and chess[i][j+3]==-1 and chess[i][j+4]==-1:
                        draw(chess,'win')
                        win=1
                        return chess
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]==-2:
                # 检测白子冲四
                if size - i >4 and mark == 1:
                    if chess[i+1][j]==-2 and chess[i+2][j]==-2 and chess[i+3][j]==-2:
                        if chess[i+4][j]>=0:
                            chess[i+4][j]=-2
                            mark=0
                            break
                        elif i>0 and chess[i-1][j]>=0:
                            chess[i-1][j]=-2
                            mark=0
                            break
                    if size-j>4:
                        if chess[i][j]==-2 and chess[i+1][j+1]==-2 and chess[i+2][j+2]==-2 and chess[i+3][j+3]==-2:
                            if chess[i+4][j+4]>=0:
                                chess[i+4][j+4]=-2
                                mark=0
                                break
                            elif i>0 and j>0 and chess[i-1][j-1]>=0:
                                chess[i-1][j-1]=-2
                                mark=0
                                break
                    if j>=4:
                        if chess[i+1][j-1]==-2 and chess[i+2][j-2]==-2 and chess[i+3][j-3]==-2:
                            if chess[i+4][j-4]>=0:
                                chess[i+4][j-4]=-2
                                mark=0
                                break
                            elif i>0 and size-j>1 and chess[i-1][j+1]>=0:
                                chess[i-1][j+1]=-2
                                mark=0
                                break
                if size-j>4 and mark==1:
                    if chess[i][j]==-2 and chess[i][j+1]==-2 and chess[i][j+2]==-2 and chess[i][j+3]==-2:
                        if chess[i][j+4]>=0:
                            chess[i][j+4]=-2
                            mark=0
                            break
                        elif j>0 and chess[i][j-1]>=0:
                            chess[i][j-1]=-2
                            mark=0
                            break
            if chess[i][j]>=0:
                #检测特殊冲四1
                if i>=1 and size-i>3 and mark==1:
                    if chess[i-1][j]==-2 and chess[i+1][j]==-2 and chess[i+2][j]==-2 and chess[i+3][j]==-2:
                        chess[i][j]=-2
                        mark=0
                        break
                    if j>=1 and size-j>3:
                        if chess[i-1][j-1]==-2 and chess[i+1][j+1]==-2 and chess[i+2][j+2]==-2 and chess[i+3][j+3]==-2:
                            chess[i][j]=-2
                            mark=0
                            break
                    if size-j>1 and j>=3:
                        if chess[i-1][j+1]==-2 and chess[i+1][j-1]==-2 and chess[i+2][j-2]==-2 and chess[i+3][j-3]==-2:
                            chess[i][j]=-2
                            mark=0
                            break
                if j>=3 and size-j>1 and mark==1:
                    if chess[i][j+1]==-2 and chess[i][j-1]==-2 and chess[i][j-2]==-2 and chess[i][j-3]==-2:
                        chess[i][j]=-2
                        mark=0
                        break
                #检测特殊冲四2
                if i>=2 and size-i>2 and mark==1:
                    if chess[i-2][j]==-2 and chess[i-1][j]==-2 and chess[i+1][j]==-2 and chess[i+2][j]==-2:
                        chess[i][j]=-2
                        mark=0
                        break
                    if j>=2 and size-j>2:
                        if chess[i-2][j-2]==-2 and chess[i-1][j-1]==-2 and chess[i+1][j+1]==-2 and chess[i+2][j+2]==-2:
                            chess[i][j]=-2
                            mark=0
                            break
                        if chess[i-2][j+2]==-2 and chess[i-1][j+1]==-2 and chess[i+1][j-1]==-2 and chess[i+2][j-2]==-2:
                            chess[i][j]=-2
                            mark=0
                            break
                if j>=2 and size-j>2 and mark==1:
                    if chess[i][j-1]==-2 and chess[i][j-1]==-2 and chess[i][j+1]==-2 and chess[i][j+2]==-2:
                        chess[i][j]=-2
                        mark=0
                        break
                #检测特殊冲四3
                if i>=3 and size-i>1 and mark==1:
                    if chess[i-3][j]==-2 and chess[i-2][j]==-2 and chess[i-1][j]==-2 and chess[i+1][j]==-2:
                        chess[i][j]=-2
                        mark=0
                        break
                    if j>=1 and size-j>3:
                        if chess[i-3][j+3]==-2 and chess[i-2][j+2]==-2 and chess[i-1][j+1]==-2 and chess[i+1][j-1]==-2:
                            chess[i][j]=-2
                            mark=0
                            break
                    if j>=3 and size-j>1:
                        if chess[i-3][j-3]==-2 and chess[i-2][j-2]==-2 and chess[i-1][j-1]==-2 and chess[i+1][j+1]==-2:
                            chess[i][j]=-2
                            mark=0
                            break
                if size-j>3 and j>=1 and mark==1:
                    if chess[i][j-1]==-2 and chess[i][j+1]==-2 and chess[i][j+2]==-2 and chess[i][j+3]==-2:
                        chess[i][j]=-2
                        mark=0
                        break
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]==-1:
                #检测黑子冲四
                if size-i>4 and mark==1:
                    if chess[i+1][j]==-1 and chess[i+2][j]==-1 and chess[i+3][j]==-1:
                        if chess[i+4][j]>=0:
                            chess[i+4][j]=-2
                            mark=0
                            break
                        elif i>0 and chess[i-1][j]>=0:
                            chess[i-1][j]=-2
                            mark=0
                            break
                    if size-j>4:
                        if chess[i+1][j+1]==-1 and chess[i+2][j+2]==-1 and chess[i+3][j+3]==-1:
                            if chess[i+4][j+4]>=0:
                                chess[i+4][j+4]=-2
                                mark=0
                                break
                            elif i>0 and j>0 and chess[i-1][j-1]>=0:
                                chess[i-1][j-1]=-2
                                mark=0
                                break
                    if j>=4:
                        if chess[i+1][j-1]==-1 and chess[i+2][j-2]==-1 and chess[i+3][j-3]==-1:
                            if chess[i+4][j-4]>=0:
                                chess[i+4][j-4]=-2
                                mark=0
                                break
                            elif i>0 and size-j>1 and chess[i-1][j+1]>=0:
                                chess[i-1][j+1]=-2
                                mark=0
                                break
                if size-j>4 and mark==1:
                    if chess[i][j+1]==-1 and chess[i][j+2]==-1 and chess[i][j+3]==-1:
                        if chess[i][j+4]>=0:
                            chess[i][j+4]=-2
                            mark=0
                            break
                        elif j>0 and chess[i][j-1]>=0:
                            chess[i][j-1]=-2
                            mark=0
                            break
            if chess[i][j]>=0:
                #检测特殊冲四1
                if i>=1 and size-i>3 and mark==1:
                    if chess[i-1][j]==-1 and chess[i+1][j]==-1 and chess[i+2][j]==-1 and chess[i+3][j]==-1:
                        chess[i][j]=-2
                        mark=0
                        break
                    if j>=1 and size-j>3:
                        if chess[i-1][j-1]==-1 and chess[i+1][j+1]==-1 and chess[i+2][j+2]==-1 and chess[i+3][j+3]==-1:
                            chess[i][j]=-2
                            mark=0
                            break
                    if size-j>1 and j>=3:
                        if chess[i-1][j+1]==-1 and chess[i+1][j-1]==-1 and chess[i+2][j-2]==-1 and chess[i+3][j-3]==-1:
                            chess[i][j]=-2
                            mark=0
                            break
                if j>=3 and size-j>1 and mark==1:
                    if chess[i][j+1]==-1 and chess[i][j-1]==-1 and chess[i][j-2]==-1 and chess[i][j-3]==-1:
                        chess[i][j]=-2
                        mark=0
                        break
                #检测特殊冲四2
                if i>=2 and size-i>2 and mark==1:
                    if chess[i-2][j]==-1 and chess[i-1][j]==-1 and chess[i+1][j]==-1 and chess[i+2][j]==-1:
                        chess[i][j]=-2
                        mark=0
                        break
                    if j>=2 and size-j>2:
                        if chess[i-2][j-2]==-1 and chess[i-1][j-1]==-1 and chess[i+1][j+1]==-1 and chess[i+2][j+2]==-1:
                            chess[i][j]=-2
                            mark=0
                            break
                        if chess[i-2][j+2]==-1 and chess[i-1][j+1]==-1 and chess[i+1][j-1]==-1 and chess[i+2][j-2]==-1:
                            chess[i][j]=-2
                            mark=0
                            break
                if j>=2 and size-j>2 and mark==1:
                    if chess[i][j-1]==-1 and chess[i][j-1]==-1 and chess[i][j+1]==-1 and chess[i][j+2]==-1:
                        chess[i][j]=-2
                        mark=0
                        break
                #检测特殊冲四3
                if i>=3 and size-i>1 and mark==1:
                    if chess[i-3][j]==-1 and chess[i-2][j]==-1 and chess[i-1][j]==-1 and chess[i+1][j]==-1:
                        chess[i][j]=-2
                        mark=0
                        break
                    if j>=1 and size-j>3:
                        if chess[i-3][j+3]==-1 and chess[i-2][j+2]==-1 and chess[i-1][j+1]==-1 and chess[i+1][j-1]==-1:
                            chess[i][j]=-2
                            mark=0
                            break
                    if j>=3 and size-j>1:
                        if chess[i-3][j-3]==-1 and chess[i-2][j-2]==-1 and chess[i-1][j-1]==-1 and chess[i+1][j+1]==-1:
                            chess[i][j]=-2
                            mark=0
                            break
                if size-j>3 and j>=1 and mark==1:
                    if chess[i][j-1]==-1 and chess[i][j+1]==-1 and chess[i][j+2]==-1 and chess[i][j+3]==-1:
                        chess[i][j]=-2
                        mark=0
                        break
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]==-2:
                # 检测白子活三
                if size-i>3 and mark==1 and i>0:
                    if chess[i+1][j]==-2 and chess[i+2][j]==-2:
                        if chess[i+3][j]>=0 and chess[i-1][j]>=0:
                            chess[i+3][j]=-2
                            mark=0
                            break
                    if size-j>3 and j>0:
                        if chess[i+1][j+1]==-2 and chess[i+2][j+2]==-2:
                            if chess[i+3][j+3]>=0 and chess[i-1][j-1]>=0:
                                chess[i+3][j+3]=-2
                                mark=0
                                break
                    if j>=3 and size - j > 1:
                        if chess[i + 1][j - 1] == -2 and chess[i + 2][j - 2] == -2:
                            if chess[i + 3][j - 3] >= 0 and chess[i - 1][j + 1] >= 0:
                                chess[i + 3][j - 3] = -2
                                mark = 0
                                break
                if size - j>3 and mark == 1 and j > 0:
                    if chess[i][j] == -2 and chess[i][j + 1] == -2 and chess[i][j + 2] == -2:
                        if chess[i][j + 3] >= 0 and chess[i][j - 1] >= 0:
                            chess[i][j + 3] = -2
                            mark = 0
                            break
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]==-1:
                #检测黑子活三
                if size-i>3 and mark==1 and i>=1:
                    if chess[i][j]==-1 and chess[i+1][j]==-1 and chess[i+2][j]==-1:
                        if chess[i+3][j]>=0 and chess[i-1][j]>=0:
                            chess[i+3][j]=-2
                            mark=0
                            break
                    if size-j>3 and j>=1:
                        if chess[i][j]==-1 and chess[i+1][j+1]==-1 and chess[i+2][j+2]==-1:
                            if chess[i+3][j+3]>=0 and chess[i-1][j-1]>=0:
                                chess[i+3][j+3]=-2
                                mark=0
                                break
                    if j>=3 and size-j>1:
                        if chess[i][j]==-1 and chess[i+1][j-1]==-1 and chess[i+2][j-2]==-1:
                            if chess[i+3][j-3]>=0 and chess[i-1][j+1]>=0:
                                chess[i+3][j-3]=-2
                                mark=0
                                break
                if size-j>3 and mark==1 and j>0:
                    if chess[i][j]==-1 and chess[i][j+1]==-1 and chess[i][j+2]==-1:
                        if chess[i][j+3]>=0 and chess[i][j-1]>=0:
                            chess[i][j+3]=-2
                            mark=0
                            break
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]==-2:
                # 检测白子特殊活三
                if size-i>4 and mark==1 and i>=1:
                    if (chess[i+1][j]==-2 or chess[i+2][j]==-2) and chess[i+3][j]==-2 and (chess[i+4][j]>=0 or chess[i-1][j]>=0):
                        if chess[i + 1][j] >= 0:
                            chess[i + 1][j] = -2
                            mark = 0
                            break
                        elif chess[i + 2][j] >= 0:
                            chess[i + 2][j] = -2
                            mark = 0
                            break
                    if size - j > 4 and j>=1:
                        if (chess[i + 1][j + 1] == -2 or chess[i + 2][j + 2] == -2) and chess[i + 3][j + 3] == -2 and (chess[i-1][j-1]>=0 or chess[i+4][j+4]>=0):
                            if chess[i + 1][j + 1] >= 0:
                                chess[i + 1][j + 1] = -2
                                mark = 0
                                break
                            elif chess[i + 2][j + 2] >= 0:
                                chess[i + 2][j + 2] = -2
                                mark = 0
                                break
                    if j>=4 and size-j>1:
                        if (chess[i + 1][j - 1] == -2 or chess[i + 2][j - 2] == -2) and chess[i + 3][j - 3] == -2 and (chess[i+4][j-4]>=0 or chess[i-1][j+1]>=0):
                            if chess[i+1][j-1] >= 0:
                                chess[i+1][j-1] = -2
                                mark=0
                                break
                            elif chess[i + 2][j - 2] >= 0:
                                chess[i + 2][j - 2] = -2
                                mark = 0
                                break
                if size-j>4 and mark==1 and j>=1:
                    if (chess[i][j + 1] == -2 or chess[i][j + 2] == -2) and chess[i][j + 3] == -2 and (chess[i][j+4]>=0 or chess[i][j-1]>=0):
                        if chess[i][j + 1] >= 0:
                            chess[i][j + 1] = -2
                            mark = 0
                            break
                        elif chess[i][j + 2] >= 0:
                            chess[i][j + 2] = -2
                            mark = 0
                            break
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]==-1:
                #检测黑子特殊活三
                if size-i>4 and mark==1 and i>=1:
                    if (chess[i+1][j]==-1 or chess[i+2][j]==-1) and chess[i+3][j]==-1 and (chess[i+4][j]>=0 or chess[i-1][j]>=0):
                        if chess[i+1][j]>=0:
                            chess[i+1][j]=-2
                            mark=0
                            break
                        elif chess[i+2][j]>=0:
                            chess[i+2][j]=-2
                            mark=0
                            break
                    if size-j>4 and j>=1:
                        if (chess[i+1][j+1]==-1 or chess[i+2][j+2]==-1) and chess[i+3][j+3]==-1 and (chess[i+4][j+4]>=0 and chess[i-1][j-1]>=0):
                            if chess[i+1][j+1]>=0:
                                chess[i+1][j+1]=-2
                                mark=0
                                break
                            elif chess[i+2][j+2]>=0:
                                chess[i+2][j+2]=-2
                                mark=0
                                break
                    if j>=4 and size-j>1:
                        if (chess[i+1][j-1]==-1 or chess[i+2][j-2]==-1) and chess[i+3][j-3]==-1 and (chess[i+4][j-4]>=0 or chess[i-1][j+1]>=0):
                            if chess[i+1][j-1]>=0:
                                chess[i+1][j-1]=-2
                                mark=0
                                break
                            elif chess[i+2][j-2]>=0:
                                chess[i+2][j-2]=-2
                                mark=0
                                break
                if size-j>4 and j>=1 and mark==1:
                    if (chess[i][j+1]==-1 or chess[i][j+2]==-1) and chess[i][j+3]==-1 and (chess[i][j+4]>=0 or chess[i][j-1]>=0):
                        if chess[i][j+1]>=0:
                            chess[i][j+1]=-2
                            mark=0
                            break
                        elif chess[i][j+2]>=0:
                            chess[i][j+2]=-2
                            mark=0
                            break
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]>=0:
                # 检测白子双活三
                summ=0
                if i>=3 and size-i>1 and mark==1:
                    if chess[i-1][j]==-2 and chess[i-2][j]==-2 and chess[i-3][j]!=-1 and chess[i+1][j]!=-1:
                        summ+=1
                    if j>=3 and size-j>1:
                        if chess[i-1][j-1]==-2 and chess[i-2][j-2]==-2 and chess[i-3][j-3]!=-1 and chess[i+1][j+1]!=-1:
                            summ+=1
                    if size-j>3 and j>=1:
                        if chess[i-1][j+1]==-2 and chess[i-2][j+2]==-2 and chess[i-3][j+3]!=-1 and chess[i+1][j-1]!=-1:
                            summ+=1
                if size-i>3 and i>=1 and mark==1:
                    if chess[i+1][j]==-2 and chess[i+2][j]==-2 and chess[i+3][j]!=-1 and chess[i-1][j]!=-1:
                        summ+=1
                    if j>=3 and size-j>1:
                        if chess[i+1][j-1]==-2 and chess[i+2][j-2]==-2 and chess[i+3][j-3]!=-1 and chess[i-1][j+1]!=-1:
                            summ+=1
                    if size-j>3 and j>=1:
                        if chess[i+1][j+1]==-2 and chess[i+2][j+2]==-2 and chess[i+3][j+3]!=-1 and chess[i-1][j-1]!=-1:
                            summ+=1
                if j>=3 and size-j>1 and mark==1:
                    if chess[i][j-1]==-2 and chess[i][j-2]==-2 and chess[i][j-3]!=-1 and chess[i][j+1]!=-1:
                        summ+=1
                if size-j>3 and j>=1 and mark==1:
                    if chess[i][j+1]==-2 and chess[i][j+2]==-2 and chess[i][j+3]!=-1 and chess[i][j-1]!=-1:
                        summ+=1
                if summ>=2 and mark==1:
                    chess[i][j]=-2
                    mark=0
                    break
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]>=0:
                # 检测黑子双活三
                summ=0
                if i>=3 and size-i>1 and mark==1:
                    if chess[i-1][j]==-1 and chess[i-2][j]==-1 and chess[i-3][j]!=-2 and chess[i+1][j]!=-2:
                        summ+=1
                    if j>=3 and size-j>1:
                        if chess[i-1][j-1]==-1 and chess[i-2][j-2]==-1 and chess[i-3][j-3]!=-2 and chess[i+1][j+1]!=-2:
                            summ+=1
                    if size-j>3 and j>=1:
                        if chess[i-1][j+1]==-1 and chess[i-2][j+2]==-1 and chess[i-3][j+3]!=-2 and chess[i+1][j-1]!=-2:
                            summ+=1
                if size-i>3 and i>=1 and mark==1:
                    if chess[i+1][j]==-1 and chess[i+2][j]==-1 and chess[i+3][j]!=-2 and chess[i-1][j]!=-2:
                        summ+=1
                    if j>=3 and size-j>1:
                        if chess[i+1][j-1]==-1 and chess[i+2][j-2]==-1 and chess[i+3][j-3]!=-2 and chess[i-1][j+1]!=-2:
                            summ+=1
                    if size-j>3 and j>=1:
                        if chess[i+1][j+1]==-1 and chess[i+2][j+2]==-1 and chess[i+3][j+3]!=-2 and chess[i-1][j-1]!=-2:
                            summ+=1
                if j>=3 and size-j>1 and mark==1:
                    if chess[i][j-1]==-1 and chess[i][j-2]==-1 and chess[i][j-3]!=-2 and chess[i][j+1]!=-2:
                        summ+=1
                if size-j>3 and j>=1 and mark==1:
                    if chess[i][j+1]==-1 and chess[i][j+2]==-1 and chess[i][j+3]!=-2 and chess[i][j-1]!=-2:
                        summ+=1
                if summ>=2 and mark==1:
                    chess[i][j]=-2
                    mark=0
                    break
    for i in range(size*mark):
        for j in range(size):
            #检测白子活二
            if chess[i][j]==-2 and mark==1:
                if i>=2 and size-i>2:
                    if chess[i+1][j]==-2 and chess[i-1][j]>=0 and chess[i-2][j]>=0 and chess[i+2][j]>=0:
                        chess[i-1][j]=-2
                        mark=0
                        break
                    if j>=2 and size-j>2:
                        if chess[i+1][j+1]==-2 and chess[i-1][j-1]>=0 and chess[i-2][j-2]>=0 and chess[i+2][j+2]>=0:
                            chess[i-1][j-1]=-2
                            mark=0
                            break
                        if chess[i+1][j-1]==-2 and chess[i-1][j+1]>=0 and chess[i-2][j+2]>=0 and chess[i+2][j-2]>=0:
                            chess[i-1][j+1]=-2
                            mark=0
                            break
                if j>=2 and size-j>2:
                    if chess[i][j+1]==-2 and chess[i][j-1]>=0 and chess[i][j-2]>=0 and chess[i][j+2]>=0:
                        chess[i][j-1]=-2
                        mark=0
                        break
                #随便下
    cache=start()
    for i in range(size):
        for j in range(size):
            cache[i][j]=chess[i][j]
    for i in range(size*mark):
        for j in range(size):
            if chess[i][j]==-1:
                if mark==1:
                    summ=1
                    x=i
                    y=j
                    while True:
                        x+=1
                        if size-x>0 and chess[x][y]==-1:
                            summ+=1
                            continue
                        break
                    if size-x>0 and chess[x][y]>=0:
                        chess[x][y]+=summ
                    if i>=1 and chess[i-1][j]>=0:
                        chess[i-1][j]+=summ
                    summ=1
                    x=i
                    y=j
                    while True:
                        x+=1
                        y+=1
                        if size-x>0 and size-y>0 and chess[x][y]==-1:
                            summ+=1
                            continue
                        break
                    if size-x>0 and size-y>0 and chess[x][y]>=0:
                        chess[x][y]+=summ
                    if i>=1 and j>=1 and chess[i-1][j-1]>=0:
                        chess[i-1][j-1]+=summ
                    summ=1
                    x=i
                    y=i
                    while True:
                        x+=1
                        y-=1
                        if size-x>0 and y>=0 and chess[x][y]==-1:
                            summ+=1
                            continue
                        break
                    if size-x>0 and y>=0 and chess[x][y]>=0:
                        chess[x][y]+=summ
                    if i>=1 and size-j>1 and chess[i-1][j+1]>=0:
                        chess[i-1][j+1]+=summ
                    summ=1
                    x=i
                    y=j
                    while True:
                        y+=1
                        if size-y>0 and chess[x][y]==-1:
                            summ+=1
                            continue
                        break
                    if size-y>0 and chess[x][y]>=0:
                        chess[x][y]+=summ
                    if j>=1 and chess[i][j-1]>=0:
                        chess[i][j-1]+=summ
    if mark==1:
        for i in record:
            if i[0]==cache and chess[i[1]][i[2]]>=0:
                if chess[i[1]][i[2]]+i[3]<0:
                    for j in range(size):
                        for k in range(size):
                            if chess[j][k]>=0 and j!=i[1] and k!=i[2]:
                                chess[j][k]-=i[3]
                else:
                    chess[i[1]][i[2]]+=i[3]
        maxx=-1
        for i in range(size):
            for j in range(size):
                if chess[i][j]>=maxx+random.randint(0,1) and checkaround(i,j):
                    maxx=chess[i][j]
                    maxxmark=i
                    maxymark=j
        try:
            for i in range(size):
                for j in range(size):
                    if chess[i][j]>0:
                        chess[i][j]=0
            cache1=[start()]
            for i in range(size):
                for j in range(size):
                    cache1[0][i][j]=chess[i][j]
            cache1.append(maxxmark)
            cache1.append(maxymark)
            delta.append(cache1[:])
            chess[maxxmark][maxymark]=-2
        except:
            draw(chess,'same')
            win=1
    return chess

def fun(x,y):
    global chess
    global size
    global win
    global markstart
    global filename
    if chess==start() and markstart==0:
        markstart=1
        if x<0:
            chess[int((size-1)/2)][int((size-1)/2)]=-2
        draw(chess)
    else:
        markstart=0
        if win==0:
            x+=20*(size-1)/2
            y+=20*(size-1)/2
            if x>=0 and y>=0:
                x+=10
                y+=10
                x-=x%20
                y-=y%20
                x=x/20
                y=y/20
            if int(x)>=0 and int(x)<size and int(y)>=0 and int(y)<size and chess[int(x)][int(y)]!=-1 and chess[int(x)][int(y)]!=-2:
                chess[int(x)][int(y)]=-1
                chess=action(chess,size)
                if win!=1:
                    draw(chess)
            #检测白子赢
            if win!=1:
                for i in range(size):
                    for j in range(size):
                        if chess[i][j]==-2:
                            if size-i>=5:
                                if chess[i][j]==-2 and chess[i+1][j]==-2 and chess[i+2][j]==-2 and chess[i+3][j]==-2 and chess[i+4][j]==-2:
                                    win=1
                                    draw(chess,'菜!')
                                if size-j>=5:
                                    if chess[i][j]==-2 and chess[i+1][j+1]==-2 and chess[i+2][j+2]==-2 and chess[i+3][j+3]==-2 and chess[i+4][j+4]==-2:
                                        draw(chess,'菜!')
                                        win=1
                                if j>=4:
                                    if chess[i][j]==-2 and chess[i+1][j-1]==-2 and chess[i+2][j-2]==-2 and chess[i+3][j-3]==-2 and chess[i+4][j-4]==-2:
                                        draw(chess,'菜!')
                                        win=1
                            if size-j>=5:
                                if chess[i][j]==-2 and chess[i][j+1]==-2 and chess[i][j+2]==-2 and chess[i][j+3]==-2 and chess[i][j+4]==-2:
                                    draw(chess,'菜!')
                                    win=1
        else:
            if x>0:
                chess=start()
                draw(chess)
                win=0
            else:
                with open(filename,'w') as fw:
                    cache=json.dumps(record)
                    fw.write(cache)
                    fw.close()
                sys.exit()

def draw_circle(color):
    t.color('black',color)
    t.fd(7)
    t.lt(90)
    t.down()
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    t.up()
    t.rt(90)
    t.bk(7)
    t.color('black','black')

def draw(chess,winn='continue'):
    global delta
    global record
    global markstart
    t.clear()
    if winn=='continue':
        t.goto(-(size-1)/2*20,-(size-1)/2*20)
        for j in range(2):
            for i in range(size):
                t.down()
                t.lt(90)
                t.fd(size*20-20)
                t.bk(size*20-20)
                t.up()
                t.rt(90)
                t.fd(20)
            t.bk(20)
            t.lt(90)
        t.seth(0)
        for i in range(size):
            for j in range(size):
                if chess[i][j]==-1:
                    t.goto(-(size/2-1/2-i)*20,-(size/2-1/2-j)*20)
                    draw_circle('black')
                elif chess[i][j]==-2:
                    t.goto(-(size/2-1/2-i)*20,-(size/2-1/2-j)*20)
                    draw_circle('white')
        if chess==start() and markstart==0:
            t.home()
            t.write('first?',align='center',font=('仿宋',100,'bold'))
            t.goto(0,-50)
            t.write('click the right side of the screen to start first\nor the left side to start second',align='center',font=('宋体',15,'bold'))
            turtle.update()
    else:
        draw(chess)
        t.home()
        t.write(winn,align='center',font=('仿宋',100,'bold'))
        if winn=='菜!':
            for i in range(len(delta)):
                delta[i].append(-1)
                record.append(delta[i][:])
            delta=[]
        if winn=='win':
            for i in range(len(delta)):
                delta[i].append(-1)
                record.append(delta[i][:])
            delta=[]
        t.goto(0,-50)
        t.write('click the right side of the screen to continue\nor the left side to quit',align='center',font=('宋体',15,'bold'))
        turtle.update()

chess=start()

turtle.onscreenclick(fun)
draw(chess)
turtle.mainloop()
