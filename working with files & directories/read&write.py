# read from text file
with open('data.txt', 'r',encoding='utf-8') as f:
    data = f.read()
    print(data)


# write on text file
with open('data.txt','w',encoding='utf-8') as f:
    data+='كيف الحال'
    f.write(data)
