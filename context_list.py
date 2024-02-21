from link_list import link_list


def get_context_list():
    headers_list = []

    with open('headers.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            header = line
            if header != '':
                header = header.replace('\n', '')
                headers_list.append(header)

    context_list = []

    for header, link in zip(headers_list, link_list):
        context_list.append([header, link])

    return context_list
