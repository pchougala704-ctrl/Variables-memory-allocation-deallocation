# print("pooja")
# print("ritika")
# print("reena")


# def welcome(name):
#     print("welcome:", name)

# welcome("pooja")
# welcome("ritika")
# welcome("reena")


# def add(a, b):
#     return a + b

# result = add(2, 3)
# print(result)


# def greet():
#     print("hello")
# greet()



# def welcome():
#     print("welcome to Nighan2 labs")

# welcome()


# def welcome(name):
#     print("welcome", name)

# welcome("pooja")


# def add(a, b):
#     print(a + b)

# add(10, 20)



#     print(a + b)
# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result)



# def test():
#     return 10
#     print("hello")


# def calculate(a, b):
#     return a + b, a - b, a * b

# x, y, z = calculate(10, 5)
# print(x)   
# print(y)   
# print(z)   



# def student(name, age):
#     print(name, age)

# student("Pooja", 20)



# student(age=20, name="pooja")



# def student(name, age, course):
#     print(name, age, course)

# student("pooja", age=20, course="BCA") 




# def add(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# print(add(10, 20))
# print(add(10, 20, 30))
# print(add(1, 2, 3, 4, 5))


# def student(**details):
#     print(details)

# student(name="pooja", age=20, course="BCA")



# def example(a, b=10, *args, **kwargs):
#     pass


# def test():
#     x = 10
#     print(x)

# test()



# x = 100

# def test():
#     print(x)

# test()


# def increment():
#     global count
#     count = 1

# increment()


# def test():
#     x = 10

# test()
# print(x)



# def add(a, b):
#     return a + b

# def display():
#     result = add(10, 20)
#     print(result)

# display()



# Python Rainbow Pattern
# import turtle

# pen = turtle.Turtle()
# pen.speed(0)

# colors = ["red", "blue", "green", "purple", "orange"]

# for i in range(100):
#     pen.color(colors[i % len(colors)])
#     pen.forward(i * 5)
#     pen.right(144)

# turtle.done()





# 🌌 Python Magic Spiral

# import turtle

# t = turtle.Turtle()
# t.speed(0)
# turtle.bgcolor("black")

# colors = ["cyan", "magenta", "yellow", "lime", "orange"]

# for i in range(150):
#     t.color(colors[i % 5])
#     t.forward(i * 1.2)
#     t.right(59)

# turtle.done()









# 🌸 Python Digital Flower Generator



import time

print("🌸 DIGITAL FLOWER GENERATOR 🌸\n")
time.sleep(1)

flower = [
    "       🌸",
    "    🌸 🌸 🌸",
    "  🌸 🌸 🌸 🌸 🌸",
    "    🌸 🌸 🌸",
    "       🌸",
    "       |",
    "       |",
    "      / \\",
    "     /   \\",
    "    🌿   🌿"
]

for line in flower:
    print(line)
    time.sleep(0.3)

print("\n✨ A little flower, a little happiness! ✨")
