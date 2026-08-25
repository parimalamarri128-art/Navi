import webbrowser
from urllib.parse import quote


def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def google_search(query):
    url = "https://www.google.com/search?q=" + quote(query)
    webbrowser.open(url)


def youtube_search(query):
    url = "https://www.youtube.com/results?search_query=" + quote(query)
    webbrowser.open(url)