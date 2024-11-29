import requests
from bs4 import BeautifulSoup


def main():
    url = "https://edelws.ru/power-pc/edelweiss-msi-gaming/"
    response = requests.get(url)
    print(response.status_code)
    # print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    spoon = soup.find_all("div", class_="detalic__text")
    # print(spoon)

    with open("page.txt", 'a', encoding="UTF-8") as file:
        file.write(''.join([i.text for i in spoon]))


if __name__ == "__main__":
    main()
