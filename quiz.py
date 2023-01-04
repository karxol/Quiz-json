from json import load

correct_answers = 0
with open('quiz.json',encoding='utf8') as questions_file:
    questions = load(questions_file)
    

    for question in questions:
        print(question['question'])
        for index,answer in enumerate(question['answers']):
            print(index, answer['text'])

        user_answer = int(input('Podaj poprawną odpowiedz: '))
        try:
            is_correct_anwer = question['answers'][user_answer]['correct']
            if is_correct_anwer:
                correct_answers += 1
        except IndexError:
            pass



        print('----'*10)


print("Twoja liczba poprawych odpowiedz: ", correct_answers)