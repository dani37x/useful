def random_string(size):
    small = string.ascii_lowercase
    big = string.ascii_uppercase
    numbers = string.digits
    s =  small + big  + numbers
    
    random_choices = random.sample(s, size)
    random.shuffle(random_choices)
    
    string_to_return = ''
    for element in random_choices:
        string_to_return += element
    
    return string_to_return
