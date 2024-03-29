import json

import requests


class HeadHunterApi:
    """Создаем класс для получения вакансий и компаний с сайта HeadHunter"""
    url = 'https://api.hh.ru/vacancies'
    header = {'User-Agent': 'Myapp'}
    file_to_save = 'hh-vacancies.json'

    def __init__(self, employer_id=None):
        self.params = {"employer_id": employer_id, "area": "2", "only_with_vacancies": True}

    def get_vacancies(self):
        """Отправляем запрос на API для получения вакансий в JSON"""
        response = requests.get(self.url, headers=self.header, params=self.params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            print('Ошибка', response.status_code, 'в получении данных c сайта HeadHunter')

    def save_to_json(self, data) -> None:
        """Получает список вакансий с указанием названия компании, названия вакансии, зарплаты, ссылки на вакансию"""

        with open(self.file_to_save, 'w', encoding='utf-8') as file:
            data_list = []
            for dict_ in data:
                temp_dict = {'company_id': dict_['employer']['id'], 'company': dict_['employer']['name'],
                             'employee': dict_['name'], 'city': dict_['area']['name'],
                             'salary': dict_.get('salary'), 'url': dict_['alternate_url'],
                             'requirement': dict_['snippet']['requirement']}
                data_list.append(temp_dict)
            json.dump(data_list, file, ensure_ascii=False, indent=4)