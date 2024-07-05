class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def info(self):
        return f"{self.name} (born {self.birth_year
        })"


class Parent(Person):
    def __init__(self, name, birth_year, children=None):
        super().__init__(name, birth_year)
        self.children = children if children is not None else []

    def add_child(self, child):
        if isinstance(child, Child):
            self.children.append(child)
        else:
            print(f"Error: {child} is not of type Child")

    def display_children(self):
        children_info = ", ".join(child.name for child in self.children)
        return f"Children of {self.name}: {children_info}"


class Child(Person):
    def __init__(self, name, birth_year, parents=None):
        super().__init__(name, birth_year)
        self.parents = parents if parents is not None else []

    def add_parent(self, parent):
        if isinstance(parent, Parent):
            self.parents.append(parent)
        else:
            print(f"Error: {parent} is not of type Parent")

    def display_parents(self):
        parents_info = ", ".join(parent.name for parent in self.parents)
        return f"Parents of {self.name}: {parents_info}"


class GrandParent(Person):
    def __init__(self, name, birth_year, children=None):
        super().__init__(name, birth_year)
        self.children = children if children is not None else []

    def add_child(self, child):
        if isinstance(child, Parent):
            self.children.append(child)
        else:
            print(f"Error: {child} is not of type Parent")

    def display_children(self):
        children_info = ", ".join(child.name for child in self.children)
        return f"Children of {self.name}: {children_info}"


# Creating instances
grandfather = GrandParent("Grandfather", 1940)
father = Parent("Father", 1970)
uncle = Parent("Uncle", 1975)
aunt = Parent("Aunt", 1980)
me = Child("Your Name", 1995)
brother = Child("Brother", 1998)
sister = Child("Sister", 2001)
cousin1 = Child("Cousin1", 2005)
cousin2 = Child("Cousin2", 2008)

# Establishing relationships
grandfather.add_child(father)
grandfather.add_child(uncle)
grandfather.add_child(aunt)

father.add_child(me)
father.add_child(brother)
father.add_child(sister)

uncle.add_child(cousin1)
uncle.add_child(cousin2)

# Displaying family tree
print("Family Tree:")
print("-----------")
print(grandfather.info())
print("\t" + grandfather.display_children())
print("\t" + father.info())
print("\t\t" + father.display_children())
print("\t" + uncle.info())
print("\t\t" + uncle.display_children())
print("\t" + aunt.info())
print("\t\t" + aunt.display_children())
print("\t\t" + me.info())
print("\t\t" + brother.info())
print("\t\t" + sister.info())
print("\t\t" + cousin1.info())
print("\t\t" + cousin2.info())
