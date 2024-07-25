import requests
from bs4 import BeautifulSoup


def get_movie_url(title):
    url = f"https://www.imdb.com/find?q={title}&s=tt&exact=true&ref_=fn_tt_ex"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("успешно!!!")

        soup = BeautifulSoup(response.text, "html.parser")
        element = soup.find("a", attrs={"class": "ipc-metadata-list-summary-item__t"}, href=True)

        if element:
            href = element["href"]
            href2 = f"https://www.imdb.com/{href}"
            return href2
        else:
            return f"файл не найден"

    else:
        return f"ошибка"


def get_movie_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("успешно всё")

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("span", attrs={"class": "hero__primary-text"})
        description = soup.find("span", attrs={"data-testid": "plot-l"})

        title = title.text
        description = description.text

        movie_dict = {'title': title, 'description': description}
        return movie_dict

    else:
        return f"файл не найден"


get_movie_url("холодное сердце")


if __name__ == "__main__":
    movie_title = input("Введите название фильма: ")
    movie_url = get_movie_url(movie_title)

    if movie_url:
        print(f"url найденного фильма: {movie_url}")

    movie_info = get_movie_info(movie_url)
    if movie_info:
        print(f"Название: {movie_info['title']}")
        print(f"Описание: {movie_info['description']}")
