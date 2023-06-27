import json
import requests
from src.abstract import APIParser


class ApiHH(APIParser):
    url = "https://api.hh.ru/vacancies"

    def __init__(self, keyword, v_count):
        self.keyword = keyword
        self.v_count = v_count

    def get_vacancies(self):
        v_list = []
        params = {
            "text": self.keyword,
            "per_page": self.v_count,
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (HTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }
        response = requests.get(self.url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items")
            for vacancy in vacancies:
                title = vacancy["name"]
                url = vacancy['alternate_url']
                if vacancy["salary"] is None:
                    salary_min = None
                    salary_max = None
                else:
                    salary_min = vacancy["salary"]["from"]
                    salary_max = vacancy["salary"]["to"]

                description = vacancy["snippet"]["requirement"]

                v_dict = {'title': title,
                          'url': url,
                          'salary_min': salary_min,
                          'salary_max': salary_max,
                          'description': description}

                v_list.append(v_dict)
            return v_list

        else:
            raise Exception(f"Ошибка подключения. Код {response.status_code}")

    def make_json_file(self, v_list):
        with open("vacancies_file.json", "w", encoding='UTF-8') as file:
            json.dump(v_list, file, indent=4, ensure_ascii=False)

    def sort_by_max_salary(self, v_list):
        salary_max_list = []
        for i in v_list:
            if i['salary_max'] is not None:
                salary_max_list.append(i)
                salary_max_list = sorted(salary_max_list, key=lambda x: x['salary_max'], reverse=True)
        return salary_max_list