from ctypes import cdll
lib = cdll.LoadLibrary('./helloWorld.so')
lib.foo(5)
