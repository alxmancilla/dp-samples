class Component(object):
    def __init__(self):
        pass

    def component_function(self):
        pass


class Leaf(Component):
    def __init__(self):
        Component.__init__(self)

    def component_function(self):
        print("some function")


class Composite(Component):
    def __init__(self):
        Component.__init__(self)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        map(lambda x: x.component_function(), self.children)

if __name__ == "__main__":
	c = Composite()
	l = Leaf()
	l_two = Leaf()
	c.append_child(l)
	c.append_child(l_two)
	c.component_function()
