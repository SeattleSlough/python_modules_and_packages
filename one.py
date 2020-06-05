def func():
    print("FUNC in one.py")


print("TOP LEVEL IN one.py")

if __name__ == "__main__":
    print("ONE.PY is being run directly")
else:
    print("ONE.PY has been imported")

# __main__ = "__main__" is used to organize the execution of code
