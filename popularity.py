from multiprocessing.sharedctypes import Value
from pydoc import text
import sys

def popularity(text): 
    check_text=list(text)
    set_from_text=set(check_text)
    list_from_set=list(set_from_text)
    list_from_set.sort()
    dict_from_set={}
    rez_list=[]
    for x in list_from_set:
        i=0
        for y in check_text:
            if x==y:
                i=i+1
                dict_from_set[x]=i
    v=list(set(dict_from_set.values()))
    v.sort()
    v.reverse()
    for z in v:
        for keys, values in dict_from_set.items():
            if z==values:
                rez_list.append(keys)
    print(rez_list)
inp_text='aab aaa aac aab aac aaa x'
text=inp_text.lower().split(' ')
popularity(text)