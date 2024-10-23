# TODO Найдите количество книг, которое можно разместить на дискете
disk_space = 1.44 * 1024 * 1024
count_lists = 100
count_strings = 50
count_chars = 25
space_one_char = 4
ans = disk_space // (count_lists * count_chars * count_strings * space_one_char)

print("Количество книг, помещающихся на дискету:", int(ans))
