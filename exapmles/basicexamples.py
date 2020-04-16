# decorator example
def outer_div(func):  
    def inner(x,y):  
        if(x<y):  
            x,y = y,x  
            return func(x,y)
    return inner  
@outer_div
def divide(x,y):  
    print(x/y)  


def logo():
    thickness = 9 #int(input()) #This must be an odd number ex: 5
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

def welcome_mat_design():
    n, m = map(int,input().split())
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

if __name__ == "__main__":
    #divide(2,4)  
    #logo()
    welcome_mat_design()