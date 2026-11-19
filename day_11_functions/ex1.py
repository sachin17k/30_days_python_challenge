#Quadratic equation is calculated as follows: ax² + bx + c = 0.
#Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):

    d = (b**2- 4*a*c)

    x1= -b +d**0.5/2*a
    x2= -b -d**0.5/2*a
    return x1,x2
root = solve_quadratic_eqn(1,-3,2)
print(root)