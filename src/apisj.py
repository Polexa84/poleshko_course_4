import json
import requests
import os
from src.abstract import APIParser


class ApiSJ(APIParser):
    """Класс для получения данных по API с сайта SuperJob"""
    url = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword, v_count):
        self.keyword = keyword
        self.v_count = v_count

    def get_vacancies(self):
        """Метод для получения и обработки данных с сайта"""
        params = {"count": self.v_count, "page": None,
                  "keyword": self.keyword, "archive": False, }
        headers = {'Host': 'api.superjob.ru',
                   'X-Api-App-Id': os.getenv('SJ_API_KEY'),
                   'Authorization': 'Bearer r.000000010000001.example.access_token',
                   'Content-Type': 'application/x-www-form-urlencoded'}

        sj_list = []

        url = self.url
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        vacancies = data.get("objects")
        for vacancy in vacancies:
            title = vacancy['profession']
            url = vacancy['link']
            if vacancy['payment_from']:
                salary_min = vacancy['payment_from']
            else:
                salary_min = None
            if vacancy['payment_to']:
                salary_max = vacancy['payment_to']
            else:
                salary_max = None
            description = vacancy['candidat']

            sj_dict = {'title': title,
                       'url': url,
                       'salary_min': salary_min,
                       'salary_max': salary_max,
                       'description': description}
            sj_list.append(sj_dict)

        return sj_list

    def make_json_file(self, sj_list):
        """Метод для записи полученных данных в json файл"""
        with open("vacancies_file.json", "w", encoding='UTF-8') as file:
            json.dump(sj_list, file, indent=4, ensure_ascii=False)

    def sort_by_max_salary(self, sj_list):
        """Метод для сортировки экземпляров класса Vacancy по параметру "максимальная зарплата" """
        salary_max_list = []
        for i in sj_list:
            if i['salary_max']:
                salary_max_list.append(i)
        salary_max_list = sorted(salary_max_list, key=lambda x: x['salary_max'], reverse=True)
        return salary_max_list