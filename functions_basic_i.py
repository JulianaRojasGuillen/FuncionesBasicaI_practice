#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

#prediction1: 5 ok


#2
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#prediction2: error ok


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#prediction3: 5 ok

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#prediction4: 5 ok

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

#prediction5: 5

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

#prediction6: 3, 5 ok


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#prediction7: 25 ok


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#prediction8: 100 ok


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#prediction9: 7,14,21 ok


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#prediction: 8 ok

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

#prediction11: 500, 500, 300, 500 ok


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#prediction12: 500, 500, 500, 300, 500 ok

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#prediction13: 500, 500, 300, 300 ok


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#prediction14: 1, 3, 2 ok

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

#prediction15: 1, 3, 5, 10 ok