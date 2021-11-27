def not_decreas(number):
    
    for digit in range(len(number)-1):
        
        if number[digit] <= number[digit+1]:
            
            pass
        
        else:
            
            return False
    return True

def adjacent_equal_ddigits(number):
    
    for digit in range(len(number)-1):
        
        if number[digit] == number[digit+1]:
            
            return True
        
    return False


def find_passwords(min_value, max_value):
    
    counter = 0
    
    for number in range(int(min_value),int(max_value)):
        
        data=str(number)
        
        if not_decreas(data) and adjacent_equal_ddigits(data):
            
            counter = counter +1
            
    return counter


passwords = find_passwords('109165', '576723')

print(passwords)
