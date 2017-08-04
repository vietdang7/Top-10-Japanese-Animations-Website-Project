# Import webbrowser to use open()
import webbrowser

# Create class Animation - follow Google guide
class Animation():
    """This class provides structure to store Japanese animations information

    Attributes:
        title (string): store title of the animation
        poster_image_url: store link to poster of the animation
        trailer_youtube_url: store Youtube link of the animation's trailer
    
    """

    # Start __init__
    def __init__(self, movie_title, movie_poster, youtube_url):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = youtube_url

    # Play trailer function
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
