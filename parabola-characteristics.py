import math

def direction_value(a):
    if a < 0:
        print("Direction: Downward")
        print("Value: Maximum")
    else:
        print("Direction: Upward")
        print("Value: Minimum")
        
def vertex_symmetry(a,b,c):
    x_vertex = -(b/(2*a))
    y_vertex = a*(x_vertex**2) + b*x_vertex + c
    print(f"Vertex: ({x_vertex},{y_vertex})")
    print(f"Axis of Symmetry: x = {x_vertex}")
    
def disc_inter(a,b,c):
    D = b**2 - 4*a*c
    print(f"Discriminant: D = {D}")
    
    root_1 = (-b + math.sqrt(D)) / 2*a
    root_2 = (-b - math.sqrt(D)) / 2*a
    if D > 0:
        print(f"X-intercepts: ({root_1},0) and ({root_2},0)")
    elif D == 0:
        print(f"X-intercept: ({root_1},0)")
    else:
        print("X-intercepts: None")
    print(f"Y-intercept: (0,{c}.0)")
    
def again():
    print("")
    tryagain = input("Would you like to try again?: ").lower()
    print("-------")
    if tryagain == "yes":
        main()
    
def main():
    print("Hi! Enter the values of a, b and c of a quadratic equation, and I'll display the characteristics of the parabola.")
    print("")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    print("")
    
    direction_value(a)
    vertex_symmetry(a,b,c)
    disc_inter(a,b,c)
    
    again()

main()