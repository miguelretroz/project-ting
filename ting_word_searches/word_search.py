import re


def exists_word(word, instance):
    result = []

    for index in range(len(instance)):
        occurrences = []
        file_data = instance.search(index)
        lines = file_data["linhas_do_arquivo"]

        for line_index, line in enumerate(lines):
            if re.search(rf"(?<!\w){word}(?!\w)", line, flags=re.IGNORECASE):
                occurrences.append({"linha": (line_index + 1)})

        if len(occurrences):
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": occurrences,
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
