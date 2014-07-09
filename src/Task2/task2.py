_list = [['A', '3'], ['B', '2'], ['C', '3'], ['A', '4'], ['B', '5'], ['C', '6'], ['A', '1'], ['B', '1'], ['C', '1']]
_dict = {}
for element in _list:
    if not element[0] in _dict:
        _dict[element[0]] = int(element[1])
    else:
        _dict[element[0]] += int(element[1])

print _dict