#dict_comp function to accept step,stop arguments and return a dictionary using comprehension
def dict_comp(stop,step):
    pass
    '''input integer_____for step,stop'''
    #input function assigned to variables to hold stop and step value
    stop,step=int(input('enter stop value')), int(input('enter step value'))
    
    #list comprehension for the stop, step iteration
    items_list1=[value for  value in range(0,stop) ]
    items_list2=[items_list1[item1:item1+step]for item1 in range(1,len(items_list1),step)]
    
    #dictionary comprehension holding values from stop and step
    items_dict={f'item_{item1 + 1}':item2 for item1,item2 in zip(items_list1,items_list2)}
    items_dict.popitem()
    
    return items_dict

print(dict_comp(0,1))