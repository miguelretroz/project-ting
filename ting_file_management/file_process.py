from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        curr_file = instance.search(index)
        if curr_file["nome_do_arquivo"] == path_file:
            return None

    lines = txt_importer(path_file)
    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(processed_data)
    print(processed_data)

    return processed_data


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
