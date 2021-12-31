from datetime import datetime, timedelta
import requests


def show_questions_and_links(tag: str, from_date, to_date):
  """Отоброжает вопросы (и ссылки на них) из списка, полученного от функции 'get_questions(from_date: int, to_date: int, tag: str)'."""
  list_of_questions = get_questions(tag, from_date, to_date)
  for questions in list_of_questions:
    print(f'{questions["title"]}\n{questions["link"]}\n')


def get_questions(tag: str, from_date: int, to_date: int) -> list:
  """Возвращает список, с информацией по вопросам, опублекованным с тегом 'tag' в промежутке между датами 'from_date' и 'to_date'."""
  params = {
    'fromdate': from_date,
    'todate': to_date,
    'order': 'desc',
    'sort': 'creation',
    'tagged': tag,
    'site': 'stackoverflow'
  }
  return requests.get('https://api.stackexchange.com/2.3/questions', params=params).json()['items']


def convert_date_to_unix_time(year: int, month: int, day: int) -> int:
  """Возврощает количество секунд, прошедших с 01.01.1970 до 'day'.'month'.'year' с округлением до целых."""
  return round((datetime(year, month, day) - datetime(1970, 1, 1)).total_seconds())
  

if __name__ == "__main__":

    today_in_unix_time = round((datetime.now() - datetime(1970, 1, 1)).total_seconds())
    two_days_ago_in_unix_time = round(((datetime.now() - timedelta(days=2)) - datetime(1970, 1, 1)).total_seconds())

    show_questions_and_links('python', two_days_ago_in_unix_time, today_in_unix_time)

