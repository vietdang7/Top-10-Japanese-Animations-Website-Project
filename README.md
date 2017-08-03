# Top 10 Japanese Animations Website Project
The website is created from a `Python`data structure. The topic is chosen based my personal interest.

## Code Example
Here are some lines of example code:
1. media.py:
```
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


```
2. enterainment_center.py:
```
import media
import fresh_tomatoes

# Create 10 instances for Japanese animations
spirited_away = media.Animation("Spirited Away",
                                "http://www.impawards.com/2002/posters/spirited_away.jpg",
                                "https://www.youtube.com/watch?v=ByXuk9QqQkk")

akira = media.Animation("Akira",
                        "https://s-media-cache-ak0.pinimg.com/736x/60/81/5e/60815e5067ce8be81c8297655abdd019--akira-film-akira-poster.jpg",
                        "https://www.youtube.com/watch?v=pC6Qk5XxGIY")
...

# Add animations to an array
animations = [spirited_away, akira, princess_mononoke, porco_rosso, castle_in_the_sky,
              ponyo, howls_moving_castle, my_neighbor_totoro, the_animatrix, grave_of_fire_flies]

# Generate website by calling open_movies_page()
fresh_tomatoes.open_movies_page(animations)
```
## Why I create this project?
This is one of projects of Full Stack Udacity Nanodegree. Main reason is to evaluate the skills I have learnt so far.

## Installation
breifly instruction for installation

## Testing
How steps of testing

## Contributors

## License

