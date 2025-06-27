import MyMainPackage.one as one 

print("top level in two.py")

one.func()

if __name__ == '__main__':
    print("Two.py runs directly")
else:
    print("Two.py imported")