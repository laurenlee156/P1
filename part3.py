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
        try:
            if name in self.namespace:
                del self.namespace[name]
            else:
                raise KeyError
        except TypeError:
            raise TypeError

    def list_variables(self):
        name_lst = list(self.namespace.keys())

    def execute_function(self, code):
        return exec(code, self.namespace)

