# Version Comparison Function

Small function for testing comparing two strings containg versions

## Running from CLI

The program will read 2 strings per line from STDIN, expecting them to be separated by a single space. It will output:
* If versions are equal, will print "Same version"
* If first version is newer than second version, will print "First version is newer than second version"
* If first version is older than second version, will print "First version is older than second version"

It will stop on EOF.

Inputing directly from keyboard:

```
$ ./compare_versions.py
1.2 1.2
Same version
```

Using an input file:
```
$ cat versions.input.txt
1.2 1.2
1.2.1 1.2.2
1.1 1.0.2
1.0.2 1.1

$ ./compare_versions.py < versions.input.txt
Same version
First version is older than second version
First version is newer than second version
First version is older than second version
```

## Importing as a library

The function can also be used as a library

```
from compare_versions import compare_versions

result = compare_versions(first_version, second_version)

if result == 0:
    print("Same version")
elif result == 1:
    print("First version is newer than second version")
else:
    print("First version is older than second version")
```
 
## Authors

* **Raphael Sales** - [narigone](https://github.com/narigone)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
 