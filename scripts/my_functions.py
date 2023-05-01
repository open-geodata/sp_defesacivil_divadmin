def rename_nome(x):
    x = x.title()
    x = x.strip()
    dict_rename = {
        '/': '-',
        ' Do ': ' do ',
        ' Dos ': ' dos ',
    }
    for k, v in dict_rename.items():
        x = x.replace(k, v)
    x = x.replace('  ', ' ')
    return x.strip()


