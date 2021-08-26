url = input('Put url here: ')
str1 = 'http:'
str2 = 'https:'
if str1 in url:
    print(url[7:url.find('.')])
elif str2 in url:
    print(url[8:url.find('.')])

