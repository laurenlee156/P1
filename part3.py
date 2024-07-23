class NamespaceManager:
    def __init__(self):
        self.namespace = {}

    def set_variable(self, name, value):
        self.namespace[name] = value

    def get_variable(self, name):
        if name in self.namespace:
            return self.namespace[name]
        else:
            raise KeyError

    def delete_variable(self, name):
        if name not in self.namespace and type(name) is None:
            raise KeyError
        else:
            del self.namespace[name]

    def list_variables(self):
        name_lst = list(self.namespace.keys())

    def execute_function(self, code):
        return exec(code, self.namespace)

# a = NamespaceManager()
# #print(a.set_variable('a', 1))
# #print(a.get_variable('a'))
# print(a.delete_variable('a'))
# print(a.list_variables())