def is_leap(year): 
        if year%4==0 or year/1000==0:
                return True
        else:
            return False

year = int(input("Enter year:"))
print(is_leap(year))