def max(x,y):
    if x >= y: 
        return  x
    else: 
        return y
print(max(4,7))
z=max(8,5)
print(z)

def shortes_string(x,y): 
    if len(x) <= len(y):
        return x
    else: 
        return y
print(shortes_string("hola","holas"))
z = shortes_string("melos", "melo")
print(z)