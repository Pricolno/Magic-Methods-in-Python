import sys
import collections
import itertools


# узнаём на каких размерах словарь перевыделяет память
def reallocating_memory():
    data = dict()
    MAX_RANGE = 100000
    last_memory = sys.getsizeof(data)
    for i in range(MAX_RANGE):
        data[i] = i
        if not (last_memory == sys.getsizeof(data)):
            print('Словарь на размере: ' + str(i) + ' перевыделяет память')
            last_memory = sys.getsizeof(data)


# по тексту получить его характеристики
def characteristics_text():
    data_text = 'Написать, код, который, помогает выяснить на каких размерах словарь перевыделяет память Написать ' \
                'функцию, которая для полученного текста возвращает самое популярное слово, самую популярную букву и ' \
                'среднее количество вхождений буквы в слово '
    data_text = data_text.replace('.', '').replace(',', '').lower()
    data_text_word = data_text.split()
    # counter_word = collections.Container()
    # for word in data_text:
    #     counter_word[word] += 1

    most_popular_word = collections.Counter(data_text_word).most_common(1)
    print('Самое популярное слово: ' + str(most_popular_word[0][0]))

    data_text_letter = data_text.replace(' ', '')
    most_popular_letter = collections.Counter(data_text_letter).most_common(1)
    print('Самая популярная буква: ' + str(most_popular_letter[0][0]))

    random_letter = 'т'
    count_word = len(data_text_word)
    count_letter = data_text_letter.count(random_letter)

    print('Среднее вхождение буквы ' + random_letter + ': ' + str(count_letter / count_word))


# все палиндромы с указаным алфавитом и максимальной длиной
def all_palindrome(n):
    alphabet = 'abcdefgk'
    half = n // 2 if n % 2 == 0 else ((n // 2) + 1)

    for half_size_palindrome in range(half + 1):
        for half_palindrome in itertools.combinations_with_replacement(alphabet, half_size_palindrome):
            half_palindrome = ''.join([letter for letter in half_palindrome])
            last_palindrom = half_palindrome[::-1]
            even_palindrom = half_palindrome + last_palindrom
            odd_palindrom = half_palindrome + last_palindrom[1::]
            print(even_palindrom)
            print(odd_palindrom)


if __name__ == '__main__':
    # reallocating_memory()
    # characteristics_text()
    all_palindrome(5)
