# Import webbrowser to use open()
import webbrowser

# Create class Animation - follow Google guide
class Animation():
    """This class provides structure to store Japanese animations information """

    # Start __init__
    def __init__(self, movie_title, movie_poster, youtube_url):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = youtube_url

    # Play trailer function
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
