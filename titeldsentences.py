my_string = str(input('enter yor sent: ')).split('.')
index_counter = 0

for sentence in my_string:
    sentence_list = sentence.split()
    
    index_counter += 1
    for i in range(1,len(sentence_list)):
        index_counter += 1
        if sentence_list[i].istitle() or sentence_list[i].isupper():
            print(f' {index_counter}  {sentence_list[i]} ')
            
            
            
            
            
