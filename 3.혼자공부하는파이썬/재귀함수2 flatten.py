def flatten(data):
    output=[]
    for item in data:
        if type(item)==list:
            output += flatten(item)
        else:
            output += [item]
           #output.append(item)
    return output

example = [[1,2,3],3,4,5,[4,3,2],8,9]
print("원본",example)
print("변환",flatten(example))