pi= 3.14
def number_input():
    output = input("숫자 입력>")
    return float(output)
def get_circumference(radius):
    return 2 * pi * radius
def get_circle_area(radius):
    return pi * radius * radius

#코드본문
radius = number_input()
print(get_circumference(radius))
print(get_circle_area(radius))
