# Line Overlap Tester

Small function for testing if two lines on the same axis overlap based on their coordinates

## Running from CLI

The program will read 4 integers per line from STDIN, expecting them to be separated by a single space. It will output Yes if the lines overlap or No if that's not the case. It will stop on EOF.

Inputing directly from keyboard:

```
$ ./line_overlap.py
1 5 2 6
Yes
```

Using an input file:
```
$ cat line_overlap.input.txt
1 5 2 6
1 5 6 8
2 6 1 5
1 5 5 6
3 4 5 6

$ ./line_overlap.py < line_overlap.input.txt
Yes
No
Yes
Yes
No
```

## Importing as a library

The function can also be used as a library

```
from line_overlap import line_overlap

x1 = 1
x2 = 5
x3 = 2
x4 = 6

if line_overlap(x1, x2, x3, x4):
    print( "Yes" )
else: 
    print( "No" )
```
 
## Authors

* **Raphael Sales** - [narigone](https://github.com/narigone)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
 