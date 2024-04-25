def display_main_menu(): 
    print ("Enter some numbers separated by commas (e.g. 5, 67,320)")


def get_user_input(): 
    num = input()
    newlist = num.split(", ")
    print (newlist)
    floatlist = [float(i) for i in newlist]
    print (floatlist)
    return floatlist 

def calc_avg(common_list):
    avg = sum(common_list)/ len(common_list)
    print (avg)

def find_min_max(commno_list): 
    min_max_list = [min(commno_list), max(commno_list)]
    print (min_max_list)

def main():
    display_main_menu()
    common_list = get_user_input()
    calc_avg(common_list)
    find_min_max(common_list)

if __name__ == "__main__":
    main()
