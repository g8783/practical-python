# bounce.py
#
# Exercise 1.5
height_i = 100
constant_bounce = 0.6
height_b = height_i 
i = 0
while i < 10:
    height_b = height_b * constant_bounce
    i = i + 1
    print(i, round(height_b,4))