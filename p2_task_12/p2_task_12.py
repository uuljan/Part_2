text = "The story of this novel happened in January 1967 on Friday in the evening from 18.30 till 1.30."
                
if text.count('f') > 1:  
    print(text.find('f'))  
    print(text.rfind('f'))  
elif text.count('f') == 1:
    print("Индекс одного 'f' -- ", text.find('f'))
else:                         
    print(text.find('f'))  
