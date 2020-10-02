class CountCalls(object):
    def __init__(self, f):
        self.f = f
        self.called = 0
    def __call__(self, *args, **kwargs):
        self.called += 1
        print(self.f.__name__, 'has been called', self.called, 'times')
        return self.f(*args, **kwargs)

@CountCalls
def print_hello():
    print("hello")

if __name__ == '__main__':
    print_hello()
    print_hello()
    print(print_hello.called)