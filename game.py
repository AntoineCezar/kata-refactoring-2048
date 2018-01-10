#!/usr/bin/env python
import random
import sys
from getch import getch


lines = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

lines[random.randint(0, 3)][random.randint(0, 3)] = random.choice([2, 4, 8])

while True:
    print('\x1b[2J')
    for i in range(4):
        if i == 0:
            print('┌──────┬──────┬──────┬──────┐')
            print('│      │      │      │      │')
        else:
            print('│      │      │      │      │')
            print('├──────┼──────┼──────┼──────┤')
            print('│      │      │      │      │')

        for j in range(4):
            if j == 0:
                sys.stdout.write('│')

            if lines[i][j] == 2:
                sys.stdout.write('\033[31m')
            elif lines[i][j] == 4:
                sys.stdout.write('\033[32m')
            elif lines[i][j] == 8:
                sys.stdout.write('\033[33m')
            elif lines[i][j] == 16:
                sys.stdout.write('\033[34m')
            elif lines[i][j] == 32:
                sys.stdout.write('\033[35m')
            elif lines[i][j] == 64:
                sys.stdout.write('\033[36m')
            elif lines[i][j] == 128:
                sys.stdout.write('\033[91m')
            elif lines[i][j] == 256:
                sys.stdout.write('\033[92m')
            elif lines[i][j] == 1024:
                sys.stdout.write('\033[93m')
            elif lines[i][j] == 2048:
                sys.stdout.write('\033[94m')

            if lines[i][j] == 0:
                sys.stdout.write('{:^6}'.format(' '))
            else:
                sys.stdout.write('{:^6}'.format(lines[i][j]))

            sys.stdout.write('\033[0m')
            sys.stdout.write('│')

        print()

    print('│      │      │      │      │')
    print('└──────┴──────┴──────┴──────┘')
    print('\033[32mh: ← j: ↓ k: ↑ l: →\033[31m\nq: quit \033[0m')
    old = [[r for r in l] for l in lines]

    c = getch()
    if c == 'h':
        for i in range(4):
            for j in range(4):
                for k in range(j + 1, 4):
                    if lines[i][k]:
                        if lines[i][j] == lines[i][k]:
                            lines[i][j] = lines[i][j] + lines[i][k]
                            lines[i][k] = 0
                        break
        for i in range(4):
            for j in range(4):
                if lines[i][j]:
                    continue
                for k in range(j + 1, 4):
                    if lines[i][k]:
                        lines[i][j] = lines[i][k]
                        lines[i][k] = 0
                        break
    elif c == 'j':
        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j - 1, -1, -1):
                    if lines[k][i]:
                        if lines[j][i] == lines[k][i]:
                            lines[j][i] = lines[j][i] + lines[k][i]
                            lines[k][i] = 0
                        break
        for i in range(4):
            for j in range(3, -1, -1):
                if lines[j][i]:
                    continue
                for k in range(j - 1, -1, -1):
                    if lines[k][i]:
                        lines[j][i] = lines[k][i]
                        lines[k][i] = 0
                        break
    elif c == 'k':
        for i in range(4):
            for j in range(4):
                for k in range(j + 1, 4):
                    if lines[k][i]:
                        if lines[j][i] == lines[k][i]:
                            lines[j][i] = lines[j][i] + lines[k][i]
                            lines[k][i] = 0
                        break
        for i in range(4):
            for j in range(4):
                if lines[j][i]:
                    continue
                for k in range(j + 1, 4):
                    if lines[k][i]:
                        lines[j][i] = lines[k][i]
                        lines[k][i] = 0
                        break
    elif c == 'l':
        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j - 1, -1, -1):
                    if lines[i][k]:
                        if lines[i][j] == lines[i][k]:
                            lines[i][j] = lines[i][j] + lines[i][k]
                            lines[i][k] = 0
                        break
        for i in range(4):
            for j in range(3, -1, -1):
                if lines[i][j]:
                    continue
                for k in range(j - 1, -1, -1):
                    if lines[i][k]:
                        lines[i][j] = lines[i][k]
                        lines[i][k] = 0
                        break
    elif c == 'q':
        print('\033[33mABANDONNED\033[0m')
        break
    else:
        print(c)
        continue

    for i in range(4):
        for j in range(4):
            if lines[j][i] == 2048:
                print('\033[32mVICTORY\033[0m')
                sys.exit(0)

    f = []
    for i in range(4):
        for j in range(4):
            if lines[i][j] == 0:
                f.append([i, j])
    if f and old != lines:
        i, j = random.choice(f)
        lines[i][j] = random.choice([2, 4, 8])
    if not f:
        print('\033[31mGAME OVER\033[0m')
        break
