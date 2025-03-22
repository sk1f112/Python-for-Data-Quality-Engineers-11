import os
from datetime import datetime
from function_homework.decomposition_string import normalize_text

class Basic_class:
    #Base class for all posts
    def __init__(self, text=None):
        if text:
            self.text = normalize_text(text.strip())
        else:
            self.text = self._validate_input(input("Enter post text: "), "Enter post text: ")

    def _validate_input(self, value, prompt):
        #input is not empty
        while not value.strip():
            print("Input cannot be empty.")
            value = input(prompt)
        return normalize_text(value.strip())

class News(Basic_class):
    #News post with city and automatic date
    def __init__(self, text=None):
        super().__init__(text)
        self.city = self._validate_input(input("Enter city: "), "Enter city: ")
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_content(self):
        #news content
        return f"News: {self.text}\nCity: {self.city}\nPublished: {self.date}"

class PrivateAd(Basic_class):
    #Private ad post with expiration date and remaining day
    def __init__(self, text=None):
        super().__init__(text)
        self.expiration_date = self._get_valid_date()
        self.days_left = (self.expiration_date - datetime.now()).days

    def _get_valid_date(self):
        #Validating date input
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
        #Private ad content
        return f"Private Ad: {self.text}\nExpires: {self.expiration_date.strftime('%Y-%m-%d')}\nDays left: {self.days_left}"

class UniquePublish(Basic_class):
    #User-generated post with author name
    def __init__(self, text=None):
        super().__init__(text)
        self.author = self._validate_input(input("Enter your name: "), "Enter your name: ")
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_content(self):
        #Unique publish content
        return f"Custom Post by {self.author}:\n{self.text}\nPublished: {self.timestamp}"

class NewsFeed:
    #Main class for news feed

    FILE_NAME = "news_feed_homework.txt"
    DEFAULT_FOLDER = "posts_folder"

    def __init__(self):
        self._file = open(self.FILE_NAME, "a", encoding="utf-8")

    def publish(self, content):
        #Writes post content to file
        self._file.write(content + "\n" + "-" * 40 + "\n")

    def close_file(self):
        #Closes the file before exiting
        self._file.close()
        print("File closed successfully.")

    def run(self):
        #Main loop for selecting and adding posts
        while True:
            print("Select post type:")
            print("1. News")
            print("2. Private Ad")
            print("3. Unique publish")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self._process_with_file_check(News)
            elif choice == "2":
                self._process_with_file_check(PrivateAd)
            elif choice == "3":
                self._process_with_file_check(UniquePublish)
            elif choice == "4":
                print("Your exit was successful")
                self.close_file()
                break
            else:
                print("Invalid choice")

    def _process_with_file_check(self, post_class):
        #Content in the file?
        use_file = input("Do you want to load data from a file? (yes/no): ").strip().lower()

        if use_file == "yes":
            file_name = input("Enter the file name: ").strip()

            #Full file path
            file_path = os.path.join(self.DEFAULT_FOLDER, file_name)

            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read().strip()
                    normalized_content = normalize_text(file_content)
                    print(f"Loaded content from file: {normalized_content}")
                    post = post_class(normalized_content)
                    self.publish(post.get_content())
                os.remove(file_path)
                print(f"File {file_path} has been successfully processed and deleted.")
            else:
                print(f"File {file_path} does not exist.")
        else:
            post = post_class()
            self.publish(post.get_content())

class FilePostProcessor:

    def __init__(self, file_path=None):
        self.file_path = file_path or "post.txt"  # Default file path if none provided
        self.default_folder = "posts_folder"  # Default folder

    def process_file(self):
        # Check if the file exists
        if not os.path.exists(self.file_path):
            print(f"Error: {self.file_path} not found.")
            return

        #Open and read the file
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Process each line
        for line in lines:
            record = normalize_text(line.strip())
            print(f"Processed Record: {record}")

        self.delete_file()

    def delete_file(self):
        #Deletes the file if it was successfully
        try:
            os.remove(self.file_path)
            print(f"{self.file_path} has been deleted successfully.")
        except Exception as e:
            print(f"Error deleting the file: {e}")

if __name__ == "__main__":
    news_feed = NewsFeed()
    news_feed.run()

    file_processor = FilePostProcessor()
    file_processor.process_file()
