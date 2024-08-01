immutable_var = 1,2,3,"r","y","u"
print(immutable_var)
print(type(immutable_var))
print(immutable_var[0])
#immutable_var[0] = 4
#элементы кортежа, т.е. те которые написаны через запятую изменять нельзя,
#но если эти элементы заплючить в квадратные скобки,
# то это уже будет список. Список изменять можно.
immutable = (2,[3,"r"],4,"y","u")
print(immutable)
immutable[1][0] = 88
print(immutable)

mutable_list = [5,8,2,6,"R","O","MAN"]
print(mutable_list)
mutable_list[0] = 1
mutable_list[4] = 1
print(mutable_list)

