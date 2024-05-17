from convert import convert
from chose_best_sentence import return_best_sentence

def test():
    with open('fingilish_test_cases.txt', 'r', encoding='utf-8') as file:
        test_cases = file.read().strip().split('\n')

    results = []
    for case in test_cases:
        print(case)
        sentences = convert(case)
        results.append(return_best_sentence(sentences))

    with open('results.txt', 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + '\n')

test()