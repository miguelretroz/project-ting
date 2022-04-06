import re


def format_occurrence(word, path_file, occurrences, list):
    if len(occurrences):
        list.append({
            "palavra": word,
            "arquivo": path_file,
            "ocorrencias": occurrences,
        })


def exists_word(word, instance, insert_content=False):
    result = []

    for index in range(len(instance)):
        occurrences = []
        file_data = instance.search(index)
        lines = file_data["linhas_do_arquivo"]

        for line_index, line in enumerate(lines):
            if re.search(rf"(?<!\w){word}(?!\w)", line, flags=re.IGNORECASE):
                occurrence_content = {
                    "linha": (line_index + 1)
                }

                if insert_content:
                    occurrence_content["conteudo"] = line
                occurrences.append(occurrence_content)

        format_occurrence(
            word, file_data["nome_do_arquivo"], occurrences, result)

    return result


def search_by_word(word, instance):
    return exists_word(word, instance, insert_content=True)
