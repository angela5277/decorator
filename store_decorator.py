
def check_admin(f):

    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)

    return wrapper()

class Store(object):

    @check_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_admin
    def put_food(self, username, food):
        self.storage.put(food)