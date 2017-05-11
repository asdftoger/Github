'''
Basic example of static class
'''


class Static_test():
    def __init__(self):
        pass
    
    @staticmethod
    def hello():
        print("hello world")
        
X = Static_test()
X.hello()