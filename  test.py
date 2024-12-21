import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if 'error' in args:
        print("Error occurred")
        sys.exit(1)
    print(f"Arguments received: {args}")
