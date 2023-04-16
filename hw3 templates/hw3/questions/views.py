from django.shortcuts import render

question_list = [{'id': 1, 'question_text': 'What is the meaning of life?'},
                            {'id': 2, 'question_text': 'What is primary: spirit or matter?'},
                            {'id': 3, 'question_text': 'Does free will exist?'}]


def questions(request):
    return render(request, 'questions/links_to_questions.html', context={'question_list': question_list})


def question(request, question_id):
    return render(request, 'questions/question.html', context={'question_list': question_list,
                                                               'question_id': question_id})
