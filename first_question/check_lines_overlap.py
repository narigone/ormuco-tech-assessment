#!/usr/bin/env python3

def check_lines_overlap(x1, x2, x3, x4):
    """
    Considering the lines are on the same axis, there are two cases where the lines don't overlap:
    Case 1: Line 1 is completely after Line 2 => X1 > X4
    Case 2: Line 1 is completely before Line 2 => X2 < X3
    Therefore, overlaps happen when NOT(X1 > X4 OR X2 < X3)
    Which can be translated to NOT(X1 > X4) AND NOT (X2 < X3)
    Ergo, X1 <= X4 and X2 >= X3
    """
    return x1 <= x4 and x2 >= x3

if __name__ == '__main__':
    from sys import stdin

    for line in stdin: 
        x1, x2, x3, x4 = [ int(s) for s in line.split( ' ' ) ]

        if check_lines_overlap(x1, x2, x3, x4):
            print( "Yes" )
        else: 
            print( "No" )