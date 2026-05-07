#karla patino
#1-5-2026,  Functions Q4

#old macdonald
def change_name(name):
    if len(name)>4:
        pos_1=name[0]
        pos_2=name[3]
        upper_1=pos_1.upper()
        name=name.replace(pos_1,upper_1)
        upper_2=pos_2.upper()
        name=name.replace(pos_2,upper_2)
        new_name=name
    return new_name
        

name=input('Enter a name:')

x=change_name(name)