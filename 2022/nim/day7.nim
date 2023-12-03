import strutils
import std/tables

type
    FakeFile = ref object
        name: string
        size: int
        isDirectory: bool
        contents: seq[FakeFile]

proc getSize(fs: Table[string, FakeFile], file_name: string): int =
    let file = fs[file_name]
    if not file.isDirectory:
        return file.size
    for f in file.contents:
        result += getSize(fs, f.name)

proc getFolder(name: string, map: var Table[string, FakeFile]): FakeFile =
    if not map.hasKey(name):
        map[name] = FakeFile(name: name, isDirectory: true, contents: @[])
    return map[name]


proc buildFileSystem(lines: seq[string]): Table[string, FakeFile] =
    var map = initTable[string, FakeFile]()
    var full_path_map = initTable[string, FakeFile]()
    var stack: seq[string] = @[]
    for line in lines:
        if line == "$ cd ..":
            discard stack.pop()
        elif line.startsWith("$ cd"):
            let dir_name = line.split(" ")[2]
            let folder = getFolder(dir_name, map)
            let _ = getFolder(stack.join(""), full_path_map)
            stack.add(folder.name)
        elif line == "$ ls":
            continue
        elif line.startsWith("dir"):
            #directory
            let tokens = line.split(" ")
            let name = tokens[1]
            var f = FakeFile(name: name, isDirectory: true, contents: @[])
            map[name] = f
            map[stack[^1]].contents.add(f)
        elif line.isEmptyOrWhitespace():
            continue
        else:
            #file
            let tokens = line.split(" ")
            let (name, size) = (tokens[1], tokens[0])
            var f = FakeFile(name: name, size: parseInt(size), contents: @[])
            map[name] = f
            map[stack[^1]].contents.add(f)
    return map

proc printFs(f: FakeFile, depth = 0) =
    var space = ""
    for _ in 0 .. depth:
        space = space & " "
    if not f.isDirectory:
        echo space & " " & f.name & " " & f.size.intToStr
    else:
        echo space & " " & f.name
        for c in f.contents:
            printFs(c, depth+1)

let lines = readFile("../input/day7.txt").splitLines()
let fs = buildFileSystem(lines)

proc part1(fs: Table[string, FakeFile]): int =
    result = 0
    for k, v in fs.pairs:
        if v.isDirectory:
            let size = getSize(fs, k)
            if size < 100000:
                echo size, " ", k
                result += size

echo part1(fs)
# printFs(fs["/"], 0)
