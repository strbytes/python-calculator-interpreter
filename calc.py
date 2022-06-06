from reader import read
import readline


def repl():
    while True:
        try:
            print(read(input(">")).eval())
        except SyntaxError as e:
            print(type(e).__name__, ":", e)
        except (EOFError, KeyboardInterrupt):
            return


if __name__ == "__main__":
    repl()
