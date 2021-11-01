class Runcase():
    def __init__(self):
        print(1)

    def __enter__(self):
        print(2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(3)


if __name__ == '__main__':
    a = Runcase()
    with a:
        pass