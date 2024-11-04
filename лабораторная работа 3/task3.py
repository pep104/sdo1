# TODO  Напишите функцию count_letters


# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
main_str = main_str.lower()
dict_count = {}


def count_letters(text):
    for i in text:
        if i.isalpha():
            if i in dict_count:
                dict_count[i] += 1
            else:
                dict_count[i] = 1


count_letters(main_str)

dict_frequency = {}


def calculate_frequency(d_count):
    count = sum([d_count[i] for i in d_count])
    for char_c in d_count:
        dict_frequency[char_c] = dict_count[char_c] / count


calculate_frequency(dict_count)

for ans in dict_frequency:
    if round(dict_frequency[ans], 2) != 0.0:
        print(f'{ans}: {round(dict_frequency[ans], 2)}')
    else:
        print(f'{ans}: {str(dict_frequency[ans])[:4]}')

# TODO Распечатайте в столбик букву и её частоту в тексте
