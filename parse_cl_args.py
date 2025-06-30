import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            for word in arg.split():
                print(word)
    else:
        print("No command-line arguments provided.")

    