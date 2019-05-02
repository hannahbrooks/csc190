from binary_tree import*
from tree import*
x=binary_tree(1)
print(x.ConvertToTree())

x.AddLeft(binary_tree(2))
y=binary_tree(3)
y.AddLeft(binary_tree(4))
y.AddRight(binary_tree(5))
x.AddRight(y)
print(x.Get_Level_Order())

x=tree(1000)
print(isinstance(x, tree))
y=tree(2000)
z=tree(3000)
x.AddSuccessor(y)
x.AddSuccessor(z)
c=tree(5)
z.AddSuccessor(c)
print(x.Get_Level_Order())
print(x.ConvertToBinaryTree())
print(x.Print_DepthFirst())

print(x.Get_Level_Order())
