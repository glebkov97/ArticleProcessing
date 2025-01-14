import sys

from .genre_definition import execute as define_genre
from .language_detection import execute as detection_language
from .summarization import execute as summarize
from .question_answering import execute as answer_question

sys.path.append('..')

modules = {
    "genre_definition": {
        "function": define_genre,
        "title": "Определение жанра",
        "result_title": "Жанр"
    },
    "language_classification": {
        "function": detection_language,
        "title": "Определение языка",
        "result_title": "Язык"
    },
    "summarization": {
        "function": summarize,
        "title": "Краткий пересказ",
        "result_title": "Содержание"
    },
    "question_answering": {
        "function": answer_question,
        "title": "Ответ на вопрос",
        "result_title": "Ответ"
    }
}

modules_without_functions = {}
for module_name, module in modules.items():
    modules_without_functions[module_name] = module.copy()
    del modules_without_functions[module_name]["function"]
