def edit_conten(path):
    with open('text.txt', 'r') as file:
        content = file.read()
    if len(content) == 0:
        return 'File is empty'
    else:
        list_regex = ['.', '!', '?', '!?']
        list_sent = list()
        temp_sub_string = ''
        for el in content:
            if el in list_regex:
                index_el = content.index(el)
                temp_sub_string = content[:index_el + 2]
                first_char_is_up = temp_sub_string[0].title()
                list_sent.append(first_char_is_up + temp_sub_string[1:])
                temp_sub_string = ''
                content = content[index_el + 2:]
    with open('text.txt', 'w') as file:
        file.write(''.join(list_sent))
    return len(list_sent)

print('Number of sentences: ', edit_conten('text.txt'))

