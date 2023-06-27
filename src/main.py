from src.position import Position
from src.apihh import ApiHH
from src.apisj import ApiSJ


def main():
    """Основная функция"""

    while True:  # Запускаем цикл запросов

        keyword = input("Введи, пожалуйста, ключевое слово для поиска вакансий и через пробел город поиска: ")

        user_input = input("1 - Вакансии с сайта Headhunter. \n"
                           "2 - Вакансии с сайта SuperJob. \n"
                           "3 - поиск на всех сайтах \n"
                           "4 - выход \n")

        if user_input == "4":
            break

        elif user_input == "1":
            Position.all_vacancies = []
            answer1 = input("Максимальное число вакансий для вывода на экран: ")
            hh = ApiHH(keyword, answer1)
            v = hh.get_vacancies()
            if len(v) == 0:
                print("По запросу с заданными параметрами не найдено ни одной вакансии")
                user_input3 = input("Хочешь продолжить поиск? ")
                if user_input3.lower() == "нет" or user_input3 == "ytn":
                    break
                else:
                    continue
            else:
                hh.make_json_file(v)
                Position.position_item(v)
                for item in Position.all_vacancies:
                    print(str(item))

                print("Отсортировать по максимальной зарплате и вывести на экран? да/нет: ")
                user_input2 = input()
                if user_input2.lower() == "нет" or user_input2.lower() == "ytn":
                    continue
                else:
                    Position.all_positions = []
                    smax = hh.sort_by_max_salary(v)
                    Position.position_item(smax)
                    for item in Position.all_positions:
                        print(str(item))

        elif user_input == "2":
            Position.all_positions = []
            answer1 = input("Максимальное число вакансий для вывода на экран: ")
            sj = ApiSJ(keyword, answer1)
            v = sj.get_vacancies()
            if len(v) == 0:
                print("По запросу с заданными параметрами не найдено ни одной вакансии")
                user_input3 = input("Хочешь продолжить поиск? ")
                if user_input3.lower() == "нет" or user_input3 == "ytn":
                    break
                else:
                    continue
            else:
                sj.make_json_file(v)
                Position.position_item(v)
                for item in Position.all_positions:
                    print(str(item))

            print("Отсортировать по максимальной зарплате и вывести на экран? да/нет: ")
            user_input2 = input()
            if user_input2.lower() == "нет" or user_input2.lower() == "ytn":
                continue
            else:
                Position.all_positions = []
                smax = sj.sort_by_max_salary(v)
                Position.position_item(smax)
                for item in Position.all_positions:
                    print(str(item))

        elif user_input == "3":
            Position.all_positions = []
            v = []
            answer1 = input("Максимальное число вакансий для вывода на экран с каждой из платформ: ")
            hh = ApiHH(keyword, answer1)
            sj = ApiSJ(keyword, answer1)
            if len(hh.get_vacancies()) + len(sj.get_vacancies()) == 0:
                print("По запросу с заданными параметрами не найдено ни одной вакансии")
                user_input3 = input("Хочешь продолжить поиск? ")
                if user_input3.lower() == "нет" or user_input3 == "ytn":
                    break
                else:
                    continue
            else:
                for i in (hh, sj):
                    vacancies_json = i.get_vacancies()
                    v.extend(vacancies_json)
                    hh.make_json_file(v)
                    Position.position_item(v)
                    for item in Position.all_positions:
                        print(str(item))
                hh.make_json_file(v)
                Position.position_item(v)
                for item in Position.all_positions:
                    print(str(item))

            print("Отсортировать по максимальной зарплате и вывести на экран? да/нет: ")
            user_input2 = input()
            if user_input2.lower() == "нет" or user_input2.lower() == "ytn":
                continue
            else:
                Position.all_positions = []
                smax = hh.sort_by_max_salary(v)
                Position.position_item(smax)
                for item in Position.all_positions:
                    print(str(item))

        elif user_input == "4":
            break


if __name__ == "__main__":
    main()
