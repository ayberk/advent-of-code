import std/tables

type
    Foo = object
        name: string
        contents: seq[Foo]

var map = initTable[string, Foo]()

map["a"] = Foo(name: "a")
echo map["a"]
echo map["a"].contents
map["a"].contents.add(Foo(name: "abc"))
echo map["a"].contents
