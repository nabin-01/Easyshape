from easyshape import *
import turtle


def main():
    while True:
        print("[L]ine")
        print("[A]rc")
        print("[T]ext")
        print("[S]ettings")
        print("[E]xit")
        op = input("enter option: ")
        try:
            if op == "L":
                x1 = int(input("Line > x1: "))
                y1 = int(input("Line > y1: "))
                x2 = int(input("Line > x2: "))
                y2 = int(input("Line > y2: "))
                line(x1, y1, x2, y2)
                if -350 < x1 > 350 or -350 < x2 > 350 or -200 < y1 > 200 or -200 < y2 > 200:
                    print("enter valid value of x and y!")
                a.setpos(x1, y1)
            elif op == "A":
                r = int(input("Enter radius: "))
                angle = int(input("enter angle: "))
                arc(r, angle)
            elif op == "T":
                b = input("enter your text/content: ")
                t_s = int(input("enter your font size:"))
                x = int(input("enter x coordinate: "))
                y = int(input("enter y coordinate: "))
                text(b, t_s, x, y)
            elif op == "S":
                p_c = input("Settings > Pen colour(default no change): ")
                p_t = int(input("Settings > Pen thickness(default no change): "))
                settings(p_c, p_t)
                print("Successfully saved!")
            elif op == "E":
                print("program is exited.")
                exit()
            else:
                print("Invalid option. Enter capital letter.")
        except ValueError:
            print("Value error! Enter valid entry.")
        main()


main()
s.clearscreen()
s.exitonclick()
turtle.done()
