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
        if self.namespace is None or name not in self.namespace:
            raise KeyError
        else:
            del self.namespace[name]

    def list_variables(self):
        name_lst = list(self.namespace.keys())

    def execute_function(self, code):
        return exec(code, self.namespace)

# a = NamespaceManager()
# a.namespace = None
# print(a.namespace)
# print(a.delete_variable('a'))
# print(a.namespace)
