from datetime import datetime

class BasicClass:
    # Base class for all posts
    def __init__(self, text):
        self.text = self._validate_input(text, "Enter post text: ")

    def _validate_input(self, value, prompt):
        # Input is not empty
        while not value.strip():
            print("Input cannot be empty.")
            value = input(prompt)
        return value.strip()

    def get_content(self):
        raise NotImplementedError("Please implement this method")

    def publish(self, file):
        file.write(self.get_content() + "\n" + "-" * 40 + "\n")

class News(BasicClass):
    # News post with city and automatic date
    def __init__(self):
        super().__init__(input("Enter news text: "))
        self.city = self._validate_input(input("Enter city: "), "Enter city: ")
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_content(self):
        return f"News: {self.text}\nCity: {self.city}\nPublished: {self.date}"

class PrivateAd(BasicClass):
    # Private ad post with expiration date and remaining days
    def __init__(self):
        super().__init__(input("Enter ad text: "))
        self.expiration_date = self._get_valid_date()
        self.days_left = (self.expiration_date - datetime.now()).days

    def _get_valid_date(self):
        while True:
            date_str = input("Enter expiration date (YYYY-MM-DD): ")
            try:
                exp_date = datetime.strptime(date_str, "%Y-%m-%d")
                if exp_date <= datetime.now():
                    print("Expiration date must be in the future.")
                else:
                    return exp_date
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

    def get_content(self):
        return f"Private Ad: {self.text}\nExpires: {self.expiration_date.strftime('%Y-%m-%d')}\nDays left: {self.days_left}"

class UniquePublish(BasicClass):
    # User-generated post with author name
    def __init__(self):
        super().__init__(input("Enter custom post text: "))
        self.author = self._validate_input(input("Enter your name: "), "Enter your name: ")
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_content(self):
        return f"Custom Post by {self.author}:\n{self.text}\nPublished: {self.timestamp}"

class NewsFeed:
    # Main class for news feed
    FILE_NAME = "news_feed_homework.txt"

    def __init__(self):
        self._file = open(self.FILE_NAME, "a", encoding="utf-8")

    def create_post(self, post_type):
        post_types = {"1": News, "2": PrivateAd, "3": UniquePublish}
        if post_type in post_types:
            post = post_types[post_type]()
            post.publish(self._file)
        else:
            print("Invalid choice")

    def close_file(self):
        self._file.close()
        print("File closed successfully.")

    def run(self):
        while True:
            print("Select post type:")
            print("1. News")
            print("2. Private Ad")
            print("3. Unique publish")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "4":
                print("Your exit was successful")
                self.close_file()
                break
            else:
                self.create_post(choice)

if __name__ == "__main__":
    news_feed = NewsFeed()
    news_feed.run()
