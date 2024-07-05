#sINGLE  LEVEL INHERITANCE
class Parent:
    p_name="Vinayak"
class Child(Parent):
    c_name="Shivansh"
obj=Child()
print("Parent name",obj.p_name)
print("Child name",obj.c_name)










#multi level inheritance
class G_parent:
    g_parent_name="Rajan"
class Parent(G_parent):
    p_name="Reena"

class Child(Parent):
    c_name="Shivansh"
obj=Child()
print("G_parent_name",obj.g_parent_name)
print("Parent name",obj.p_name)
print("Child Name",obj.c_name)

#multiple level inheritance
class Parent1:
    g_parent_name="Rajan"
class Parent2:
    p_name="Reena"
class Child(Parent1,Parent2):
    c_name="Shivansh"

obj=Child()
print("G_parent name",obj.g_parent_name)
print("Parent name",obj.p_name)
print("Child name",obj.c_name)

#Hirarchicle Inheritance
class Parent1:
    g_parent_name="Chatrbhuj"
class Child1(Parent1):
    c_name1="Vinayak"
class Child(Parent1):
    c_name="Shubham"

obj=Child()
print("G_parent_name",obj.g_parent_name)
print("Child name",obj.c_name)

obj1=Child1()
print("G_parent_name",obj1.g_parent_name)
print("Child Name",obj1.c_name1)
