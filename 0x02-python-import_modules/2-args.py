from sys import argv

if __name__ == "__main__":

    def no_of_argu(*args):
    # using len() method in args to count
        return (len(args))
    i = 1
    args = len(argv) - 1

    print(f"{args:d} {'argument' if args == 1 else 'arguments'}", end="")
    print(f"{'.' if args == 0 else ':'}")
    while (i <= args):
        print(f"{i}: {argv[i]}")
        i += 1

no_of_argu()
