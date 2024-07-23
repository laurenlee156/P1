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
        if self.namespace is not None:
            if name in self.namespace:
                self.namespace.pop(name)
            else:
                raise KeyError

    def list_variables(self):
        return list(self.namespace.keys())

    def execute_function(self, code):
        return exec(code, self.namespace)

# a = NamespaceManager()
# a.namespace = {'a': 10, 'b': 20}
# # print(a.namespace)
# # #print(a.delete_variable('a'))
# # #print(a.namespace)
# # # # print(a.namespace)
# print(a.list_variables())
