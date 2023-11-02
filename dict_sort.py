color_dict={ 'red':'#FF0000',
            'green':'#000000',
            'black':'#000000',
            'white':'#FFFFFF' }
my_keys=list(color_dict.keys())
print(my_keys)
my_keys.sort()
sorted_dict={i: color_dict[i] for i in my_keys}
print(sorted_dict)