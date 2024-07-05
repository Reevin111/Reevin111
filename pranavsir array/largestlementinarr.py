a=[22,16,34,66,41,81,99,63]
max_element=a[0]
for i in range(len(a)):
    if a[i]>max_element:
        max_element=a[i]
print(max_element)