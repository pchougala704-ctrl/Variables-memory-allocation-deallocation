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



# import time

# print("🌸 DIGITAL FLOWER GENERATOR 🌸\n")
# time.sleep(1)

# flower = [
#     "       🌸",
#     "    🌸 🌸 🌸",
#     "  🌸 🌸 🌸 🌸 🌸",
#     "    🌸 🌸 🌸",
#     "       🌸",
#     "       |",
#     "       |",
#     "      / \\",
#     "     /   \\",
#     "    🌿   🌿"
# ]

# for line in flower:
#     print(line)
#     time.sleep(0.3)

# print("\n✨ A little flower, a little happiness! ✨")





# Neon Spiral Art 🌀

# import turtle
# import colorsys

# # Create the screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Neon Spiral Art 🌀")
# screen.setup(width=900, height=800)
# screen.colormode(1.0)
# screen.tracer(0)

# # Create the drawing turtle
# pen = turtle.Turtle()
# pen.speed(0)
# pen.pensize(2)
# pen.hideturtle()

# # Draw the neon spiral
# for i in range(360):
#     hue = (i / 360) % 1.0
#     color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

#     pen.pencolor(color)
#     pen.forward(i * 0.8)
#     pen.right(91)

#     # Update the drawing gradually
#     if i % 5 == 0:
#         screen.update()

# screen.update()

# # Keep the window open
# turtle.done()






# import turtle
# import random
# import math

# # Create the drawing window
# screen = turtle.Screen()
# screen.setup(900, 700)
# screen.bgcolor("black")
# screen.title("Galaxy Art Generator")
# screen.colormode(255)

# pen = turtle.Turtle()
# pen.hideturtle()
# pen.speed(0)
# pen.penup()

# # Galaxy color palette
# colors = [
#     (170, 90, 255),   # Purple
#     (90, 150, 255),   # Blue
#     (255, 110, 190),  # Pink
#     (120, 220, 255),  # Cyan
#     (255, 255, 255),  # White
#     (255, 190, 100)   # Golden
# ]

# # 1. Draw stars in space
# for _ in range(260):
#     x = random.randint(-440, 440)
#     y = random.randint(-330, 330)
#     size = random.choice([2, 2, 3, 4])

#     pen.goto(x, y)
#     pen.dot(size, random.choice(colors))

# # 2. Create four spiral arms
# arms = 4
# points_per_arm = 190

# for arm in range(arms):
#     offset = (2 * math.pi * arm) / arms

#     for i in range(points_per_arm):
#         angle = i * 0.085 + offset
#         radius = 5 + i * 1.05 + random.uniform(-8, 8)

#         x = radius * math.cos(angle) + random.uniform(-7, 7)
#         y = radius * math.sin(angle) * 0.68 + random.uniform(-7, 7)

#         pen.goto(x, y)
#         pen.dot(random.choice([2, 3, 3, 4, 5]),
#                 random.choice(colors))

# # 3. Draw the glowing-looking galaxy center
# pen.goto(0, 0)
# pen.dot(34, (255, 240, 190))
# pen.dot(22, (255, 210, 240))
# pen.dot(10, (255, 255, 255))

# # 4. Add a title
# pen.goto(0, 300)
# pen.color("white")
# pen.write(
#     "GALAXY ART GENERATOR",
#     align="center",
#     font=("Arial", 20, "bold")
# )

# # Display the artwork
# turtle.done()





import time
import random

print("\033[95m")
print("╔══════════════════════════════════╗")
print("║       ✨ MOOD MAGIC ✨           ║")
print("║     Your Feelings Universe       ║")
print("╚══════════════════════════════════╝")
print("\033[0m")

name = input("🌟 Enter your name: ")
text = input("💭 How are you feeling today? ").lower()

moods = {
    "HAPPY 😊": ["happy", "joy", "excited", "great", "wonderful"],
    "SAD 🌧️": ["sad", "lonely", "cry", "upset", "unhappy"],
    "ANGRY 🔥": ["angry", "mad", "furious", "annoyed"],
    "LOVE 💖": ["love", "lovely", "caring", "affection"],
    "FEAR 🌙": ["scared", "afraid", "nervous", "fear"],
    "CALM 🌿": ["calm", "peaceful", "relaxed", "chill"]
}

detected = [
    mood for mood, words in moods.items()
    if any(word in text.split() for word in words)
]

print("\n🔮 Reading your mood...")
for i in range(3):
    print("✨ Discovering feelings" + "." * (i + 1))
    time.sleep(0.5)

if detected:
    mood = detected[0]
else:
    mood = "MYSTERY 🌈"

messages = {
    "HAPPY 😊": "Keep shining! Your smile makes a difference.",
    "SAD 🌧️": "Every storm passes. Be gentle with yourself.",
    "ANGRY 🔥": "Take a deep breath. You deserve some peace.",
    "LOVE 💖": "Spread kindness wherever you go.",
    "FEAR 🌙": "You can take things one small step at a time.",
    "CALM 🌿": "Protect your peace and enjoy this moment.",
    "MYSTERY 🌈": "Every feeling has a story. Keep exploring yours!"
}

print("\n" + "═" * 38)
print(f"  🌟 MOOD REPORT FOR {name.upper()} 🌟")
print("═" * 38)

print(f"\n  Your Mood: {mood}")
print(f"\n  💌 Message: {messages[mood]}")

score = random.randint(60, 100)
filled = score // 10

print("\n  ⚡ Mood Energy Meter")
print("  [" + "█" * filled + "░" * (10 - filled) + f"] {score}%")

print("\n  ✨ Your lucky color:", random.choice(
    ["Purple 💜", "Blue 💙", "Pink 🩷",
     "Green 💚", "Yellow 💛"]
))

print("\n" + "🌈 " * 10)
print("       THANK YOU FOR SHARING! 💖")
print("🌈 " * 10)


