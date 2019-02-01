def vowel_count(s):
    '''
    (str) -> (str)
    Prints out how many vowels are in a given string, s.
    '''
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
    print("Number of vowels: " + str(count))
    
def word_occur(s, key):
    '''
    (str) -> (str)
    Prints out the number of occurences of word in a given string, s.
    In the excercise key will always be "bob"
    '''
    count = 0
    for i in range(len(s)-2):
        if s[i : i + 3] == 'bob':
            count += 1
    print("Number of times bob occurs is: " + str(count))
    
def alpha_sub(s):
    '''
    (str) -> (str)
    Prints out the longest alphabetically sorted substring in a given string, s.
    '''
    
    found = '' # The longest substring found
    current = '' # The accumulator to be compared with found 
    
    for i in range(len(s)):
        if current == '' or s[i-1] <= s[i]:
            current += s[i]
        elif current[-1] <= s[i]:
            current += s[i]
        elif len(current) > len(found):
            found, current = current, found
            current = s[i]
        else:
            current = s[i]
        
    if len(current) > len(found):
        print('Longest substring in alphabetical order is:', current)
    else: 
        print('Longest substring in alphabetical order is:', found)
        