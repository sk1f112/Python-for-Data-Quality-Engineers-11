import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from function_homework.decomposition_string import (
    normalize_text,
    split_into_sentences,
    capitalize_sentences,
    join_sentences_with_spacing
)

class BasicClass:
    def __init__(self, text=None, from_file=False):
        self.from_file = from_file
        if text:
            self.text = text.strip()
        elif not from_file:
            self.text = input("Enter post text: ").strip()

    def _validate_input(self, value, prompt):
        # Input is not empty
        while not value.strip():
            print("Input cannot be empty.")
            value = input(prompt)
        return self._process_text(value.strip())

    def _process_text(self, text):
        normalized = normalize_text(text)
        sentences = split_into_sentences(normalized)
        capitalized = capitalize_sentences(sentences)
        return join_sentences_with_spacing(capitalized)

    def get_content(self):
        raise NotImplementedError("Subclasses must implement get_content method")

    def publish(self, file):
        file.write(self.get_content() + "\n" + "-" * 40 + "\n")

class News(BasicClass):
    def __init__(self, text=None, city=None, date=None, from_file=False):
        super().__init__(text, from_file)
        if from_file:
            self.city = city if city else "Unknown"
            self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            if city:
                self.city = city
            else:
                self.city = self._validate_input(input("Enter city: "), "Enter city: ")
            if date:
                self.date = date
            else:
                self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_content(self):
        return f"News: {self.text}\nCity: {self.city}\nPublished: {self.date}"

class PrivateAd(BasicClass):
    def __init__(self, text=None, expiration_date=None, from_file=False):
        super().__init__(text, from_file)
        if from_file:
            self.expiration_date = expiration_date
            self.days_left = (self.expiration_date - datetime.now()).days
        else:
            if expiration_date:
                self.expiration_date = expiration_date
                self.days_left = (self.expiration_date - datetime.now()).days
            else:
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
    def __init__(self, text=None, author=None, timestamp=None, from_file=False):
        super().__init__(text, from_file)
        if from_file:
            self.author = author if author else "Anonymous"
            self.timestamp = timestamp if timestamp else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            if author:
                self.author = author
            else:
                self.author = self._validate_input(input("Enter your name: "), "Enter your name: ")
            if timestamp:
                self.timestamp = timestamp
            else:
                self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_content(self):
        return f"Custom Post by {self.author}:\n{self.text}\nPublished: {self.timestamp}"

    def _validate_input(self, value, prompt):
        if not value.strip():
            print(f"{prompt} cannot be empty.")
            return input(prompt).strip()
        return value.strip()

class NewsFeed:
    # Main class for news feed
    FILE_NAME = "news_feed_homework.txt"
    DEFAULT_FOLDER = "posts_folder"

    def __init__(self):
        self._file = open(self.FILE_NAME, "a", encoding="utf-8")

    def create_post(self, post_class, text=None):
        post = post_class(text) if text else post_class()
        post.publish(self._file)

    def close_file(self):
        self._file.close()
        print("File closed successfully.")

    def txt_process(self, post_class):
        while True:
            file_name = input("Enter the file name: ").strip()
            file_path = os.path.join(self.DEFAULT_FOLDER, file_name)

            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read().strip()
                    print(f"Loaded content from file: {file_content}")
                    self.create_post(post_class, file_content)
                os.remove(file_path)
                print(f"File {file_path} has been successfully processed and deleted.")
                return
            else:
                print(f"File {file_path} does not exist. Please enter the correct file name.")

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
            elif choice in {"1", "2", "3"}:
                self._process_with_file_check({"1": News, "2": PrivateAd, "3": UniquePublish}[choice])
            else:
                print("Invalid choice")

    def _process_with_file_check(self, post_class):
        while True:
            use_file = input("Do you want to load data from a file? (yes/no): ").strip().lower()

            if use_file == "yes":
                while True:
                    file_type = input("Enter file type (.txt / .json / .xml): ").strip().lower()

                    if file_type == ".txt":
                        self.txt_process(post_class)
                        return
                    elif file_type == ".json":
                        processor = JsonPostProcessor()
                        processor.process()
                        return
                    elif file_type == ".xml":
                        processor = XmlPostProcessor()
                        processor.process()
                        return
                    else:
                        print("Invalid file type. Choose from .txt, .json, .xml.")
            elif use_file == "no":
                self.create_post(post_class)
                return
            else:
                print("Please enter 'yes' or 'no'.")

class JsonPostProcessor:
    def __init__(self, output_file="news_feed_homework.txt"):
        self.output_file = output_file
        self.file_path = None

    def process(self):
        while True:
            self.file_path = input("Enter the full path to the JSON file (or just file name if it's in current directory): ").strip()

            if not self.file_path:
                print("File path cannot be empty. Please enter a valid file path.")
                continue

            if not os.path.exists(self.file_path):
                print(f"File '{self.file_path}' does not exist. Please enter a valid file path.")
                continue

            break

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            multiple = input("Does the JSON file contain multiple records? (yes/no): ").strip().lower()
            if multiple == "no":
                data = [data]
            elif multiple == "yes":
                pass
            else:
                print("Invalid JSON structure for selected mode.")
                return

            with open(self.output_file, "a", encoding="utf-8") as outfile:
                for record in data:
                    self._process_record(record, outfile)

            self._delete_file(success=True)

        except Exception as e:
            print(f"Error while processing the file: {e}")
            self._delete_file(success=False)

    def _process_record(self, record, file):
        post_type = record.get("type")
        text = record.get("text")

        if not post_type or not text:
            print("Skipping record due to missing 'type' or 'text'.")
            return

        text = self._format_text(text)

        if post_type == "News":
            city = record.get("city", "Unknown")
            date = record.get("date")
            post = News(text=text, city=city, date=date)

        elif post_type == "PrivateAd":
            try:
                exp_date = datetime.strptime(record["expiration_date"], "%Y-%m-%d")
                post = PrivateAd(text=text, expiration_date=exp_date)
            except Exception:
                print("Skipping ad: Invalid expiration date format.")
                return

        elif post_type == "UniquePublish":
            author = record.get("author", "Anonymous")
            timestamp = record.get("timestamp")
            post = UniquePublish(text=text, author=author, timestamp=timestamp)

        else:
            print(f"Unknown post type: {post_type}")
            return

        post.publish(file)
        print(f"Post of type '{post_type}' published successfully.")

    def _format_text(self, text):
        normalized = normalize_text(text)
        sentences = split_into_sentences(normalized)
        capitalized = capitalize_sentences(sentences)
        return join_sentences_with_spacing(capitalized)

    def _delete_file(self, success: bool):
        abs_default_folder = os.path.abspath("posts_folder")
        abs_file_path = os.path.abspath(self.file_path)

        if not success:
            print(f"File {self.file_path} was not deleted because processing failed.")
            return

        if os.path.commonpath([abs_default_folder]) not in abs_file_path:
            print(f"File {self.file_path} was processed but not deleted (outside of posts_folder).")
            return

        try:
            os.remove(self.file_path)
            print(f"File {self.file_path} deleted after successful processing.")
        except Exception as e:
            print(f"Failed to delete file: {e}")


class XmlPostProcessor:
    def __init__(self, output_file="news_feed_homework.txt"):
        self.output_file = output_file
        self.file_path = None

    def process(self):
        while True:
            self.file_path = input(
                "Enter the full path to the XML file (or just file name if it's in current directory): ").strip()

            if not self.file_path:
                print("File path cannot be empty. Please enter a valid file path.")
                continue

            if not os.path.exists(self.file_path):
                print(f"File '{self.file_path}' does not exist. Please enter a valid file path.")
                continue

            break

        try:
            # Ask the user if the XML file contains one or many records
            while True:
                multiple = input("Does the XML file contain multiple records? (yes/no): ").strip().lower()

                if multiple == "no":
                    records = self._process_single_post(self.file_path)
                    break
                elif multiple == "yes":
                    records = self._process_multiple_posts(self.file_path)
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if not records:
                self._delete_file(success=False)
                return

            # Write the records to the output file
            with open(self.output_file, "a", encoding="utf-8") as outfile:
                for record in records:
                    self._process_record(record, outfile)

            self._delete_file(success=True)

        except Exception as e:
            print(f"Error while processing the file: {e}")
            self._delete_file(success=False)

    def _process_single_post(self, file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Assuming the root is a single post
            if root.tag == "post":
                return [root]
            else:
                print("Invalid XML structure. Expected <post> as the root element.")
                return []
        except Exception as e:
            print(f"Error while processing the file: {e}")
            return []

    def _process_multiple_posts(self, file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Assuming the root is <posts> containing multiple <post> elements
            if root.tag == "posts":
                return root.findall("post")
            else:
                print("Invalid XML structure. Expected <posts> as the root element containing <post> elements.")
                return []
        except Exception as e:
            print(f"Error while processing the file: {e}")
            return []

    def _process_record(self, record, file):
        post_type = record.find("type").text
        text = record.find("text").text

        if not post_type or not text:
            print("Skipping record due to missing 'type' or 'text'.")
            return

        text = self._format_text(text)

        if post_type == "News":
            city = record.find("city").text if record.find("city") is not None else "Unknown"
            date = record.find("date").text if record.find("date") is not None else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            post = News(text=text, city=city, date=date, from_file=True)

        elif post_type == "PrivateAd":
            expiration_date = record.find("expiration_date").text
            try:
                exp_date = datetime.strptime(expiration_date, "%Y-%m-%d") if expiration_date else None
                if exp_date and exp_date > datetime.now():
                    post = PrivateAd(text=text, expiration_date=exp_date, from_file=True)
                else:
                    print("Skipping ad: Expiration date must be in the future.")
                    return
            except Exception:
                print("Skipping ad: Invalid expiration date format.")
                return

        elif post_type == "UniquePublish":
            author = record.find("author").text if record.find("author") is not None else "Anonymous"
            timestamp = record.find("timestamp").text if record.find("timestamp") is not None else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            post = UniquePublish(text=text, author=author, timestamp=timestamp, from_file=True)

        else:
            print(f"Unknown post type: {post_type}")
            return

        post.publish(file)
        print(f"Post of type '{post_type}' published successfully.")

    def _format_text(self, text):
        normalized = normalize_text(text)
        sentences = split_into_sentences(normalized)
        capitalized = capitalize_sentences(sentences)
        return join_sentences_with_spacing(capitalized)

    def _delete_file(self, success: bool):
        abs_default_folder = os.path.abspath("posts_folder")
        abs_file_path = os.path.abspath(self.file_path)

        if not success:
            print(f"File {self.file_path} was not deleted because processing failed.")
            return

        if os.path.commonpath([abs_default_folder]) not in abs_file_path:
            print(f"File {self.file_path} was processed but not deleted (outside of posts_folder).")
            return

        try:
            os.remove(self.file_path)
            print(f"File {self.file_path} deleted after successful processing.")
        except Exception as e:
            print(f"Failed to delete file: {e}")


if __name__ == "__main__":
    news_feed = NewsFeed()
    news_feed.run()

class FilePostProcessor:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.default_folder = "posts_folder"

    def process_file(self):
        if not self.file_path:
            return

        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            record = normalize_text(line.strip())
            print(f"Processed Record: {record}")

        self.delete_file()

    def delete_file(self):
        try:
            os.remove(self.file_path)
            print(f"{self.file_path} has been deleted successfully.")
        except Exception as e:
            print(f"Error deleting the file: {e}")

if __name__ == "__main__":
    file_processor = FilePostProcessor()
    file_processor.process_file()

