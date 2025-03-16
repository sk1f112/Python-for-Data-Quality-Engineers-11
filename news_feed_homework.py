from datetime import datetime

class NewsFeed:
    FILE_NAME = "news_feed.txt"  # Назва файлу для збереження записів

    def __init__(self):
        pass

    def publish(self, content):
        #Додає запис у текстовий файл
        with open(self.FILE_NAME, "a", encoding="utf-8") as file:
            file.write(content + "\n" + "-" * 40 + "\n")

    def run(self):
        #Головний цикл вибору та додавання записів
        while True:
            print("\nОберіть тип запису:")
            print("1. Новина")
            print("2. Приватне оголошення")
            print("3. Користувацький запис")
            print("4. Вийти")

            choice = input("Введіть ваш вибір: ")

            if choice == "1":
                self.publish(News().get_content())
            elif choice == "2":
                self.publish(PrivateAd().get_content())
            elif choice == "3":
                self.publish(CustomRecord().get_content())
            elif choice == "4":
                print("Вихід...")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

class News:
    #Клас для створення новини
    def __init__(self):
        self.text = input("Введіть текст новини: ")
        self.city = input("Введіть місто: ")
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Поточна дата та час

    def get_content(self):
        #Формує текст запису
        return f"Новина: {self.text}\nМісто: {self.city}\nОпубліковано: {self.date}"

class PrivateAd:
    #Клас для створення приватного оголошення
    def __init__(self):
        self.text = input("Введіть текст оголошення: ")
        self.expiration_date = input("Введіть дату закінчення (YYYY-MM-DD): ")
        self.days_left = (datetime.strptime(self.expiration_date,
                                            "%Y-%m-%d") - datetime.now()).days  # Обчислення днів до закінчення

    def get_content(self):
        #Формує текст запису
        return f"Приватне оголошення: {self.text}\nДіє до: {self.expiration_date}\nЗалишилось днів: {self.days_left}"

class CustomRecord:
    #Клас для створення унікального запису

    def __init__(self):
        self.text = input("Введіть текст запису: ")
        self.author = input("Введіть ваше ім'я: ")
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Поточна дата та час

    def get_content(self):
        #Формує текст запису
        return f"Користувацький запис від {self.author}:\n{self.text}\nОпубліковано: {self.timestamp}"

if __name__ == "__main__":
    news_feed = NewsFeed()
    news_feed.run()