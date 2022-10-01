## Steganography cheat sheet

### NTFS Streams

#### Hide file inside another file

```sh
type c:\calc.exe > c:\readme.txt:calc.exe
```
```sh
mklink executable_link.exe c:\readme.txt:calc.exe
executable_link.exe
```

### White Space Steganography using snow

#### Hide message in text file

```sh
snow -C -m "Secret message" -p "magic" readme.txt readme2.txt
```

#### Retrieve message from text file

```sh
snow -C -p "magic" readme2.txt
```

