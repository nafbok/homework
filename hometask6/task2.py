def key_list_dict(dict):
    key_value = list()
    for key, value in dict.items():
        str1 = 'string'
        if type(key) == type(str1):
            key_value.append(value)
    return key_value

school_dict = {'school1': 'Itea',
               'school2': 'Step',
               3: 'QALight',
               4: 'SkillUp',
               'school5': 'Hillel'}
print(key_list_dict(school_dict))