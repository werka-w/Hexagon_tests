a = ['century', 'customer', 'democratic', 'Congress', 'customer', 'evening',
     'often', 'outside', 'reveal', 'weight', 'western', 'century']
b = ['weapon', 'western', 'traditional', 'guess', 'customer', 'exist',
     'democratic', 'Congress', 'evening', 'finish', 'western', 'executive']

def common_words(list1, list2):
    list1_lower = [word.lower() for word in list1]
    list2_lower = [word.lower() for word in list2]
    set_common = set(list1_lower).intersection(list2_lower)
    return list(set_common)

def sorting_by_len(list1):
    return sorted(list1, key=len)

sortedlist = sorting_by_len(common_words(a, b))

print(sortedlist)
