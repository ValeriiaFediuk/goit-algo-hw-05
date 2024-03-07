import timeit
from search_kmp import kmp_search
from search_rabin_karp import rabin_karp_search
from search_boyer_moore import boyer_moore_search


def read_file(file_path):
    with open(file_path, 'r', encoding='cp1251') as file:
        return file.read()


def measure_search_time(func, text, pattern):
    setup_code = f'''
from __main__ import {func.__name__}
'''
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt, setup=setup_code, globals={'text': text, 'pattern': pattern}, number=10)


article1 = read_file("article1.txt")
article2 = read_file("article2.txt")

existing_substring = "Висновки" 
fake_substring = "Філологічний інститут"

if __name__ == '__main__':

    for i, text in enumerate([article1, article2 ]):
        print(f"\nСтаття №{i+1}")
        results = []
        for pattern in [existing_substring, fake_substring ]:
            for search_func in [boyer_moore_search,rabin_karp_search, kmp_search ]:
                time = measure_search_time(search_func, text, pattern)
                results.append((search_func.__name__, pattern, time))

        print(f"{'Алгоритм':<30} | {'Підрядок':<25} | {'Час (секунди)':<15}")
        print('-' * 70)
        for result in results:
            print(f"{result[0]:<30} | {result[1]:<25} | {result[2]:<15.5f}")
