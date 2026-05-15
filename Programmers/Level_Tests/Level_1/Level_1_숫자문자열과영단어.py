def solution(s):
    
    my_dict = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    for word,num in my_dict.items():
        s = s.replace(word,num)
        
    
    return int(s)

"""
재풀이
def solution(s):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i,word in enumerate(numbers):
        s = s.replace(word,str(i))
    
    
    return int(s)
    """