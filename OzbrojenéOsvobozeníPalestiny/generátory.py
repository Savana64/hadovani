it = iter([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))



def generate2():
    """generates 2 numbers"""
    print('A')
    yield 0
    print('B')
    yield 1
    print('C')

generate2()
it = generate2()
next(it)
next(it)
import contextlib

@contextlib.contextmanager
def ctx_manager():
    print('Entering')
    yield 123
    print('Exiting')


with ctx_manager() as obj:
    print('Inside context, with', obj)