import media
import fresh_tomatoes

# Create 10 instances for Japanese animations
spirited_away = media.Animation("Spirited Away",
                                "http://www.impawards.com/2002/"
                                "posters/spirited_away.jpg",
                                "https://www.youtube.com/watch?v=ByXuk9QqQkk")

akira = media.Animation("Akira",
                        "https://s-media-cache-ak0.pinimg.com/736x/"
                        "60/81/5e/60815e5067ce8be81c8297655abdd019"
                        "--akira-film-akira-poster.jpg",
                        "https://www.youtube.com/watch?v=pC6Qk5XxGIY")

princess_mononoke = media.Animation("Princess Mononoke",
                                    "http://img12.deviantart.net/ee3c/i/2016/"
                                    "093/e/8/princess_mononoke__alternative_m"
                                    "ovie_poster_by_marioredsigns-d9xm2lk.jpg",
                                    "https://www.youtube.com/watch?"
                                    "v=4OiMOHRDs14")

porco_rosso = media.Animation("Porco Rosso",
                              "http://img.moviepostershop.com/"
                              "porco-rosso-movie-poster-1992-1020670123.jpg",
                              "https://www.youtube.com/watch?v=awEC-aLDzjs")

castle_in_the_sky = media.Animation("Castle in the sky",
                                    "https://thespectatorial.files."
                                    "wordpress.com/2013/12/castleinthesky.jpg",
                                    "https://www.youtube.com/watch?"
                                    "v=McM0_YHDm5A")

ponyo = media.Animation("Ponyo",
                        "https://cdn.traileraddict.com/content"
                        "/walt-disney-pictures/ponyo-5.jpg",
                        "https://www.youtube.com/watch?v=CsR3KVgBzSM")

howls_moving_castle = media.Animation("Howl's Moving Castle",
                                      "http://img.moviepostershop.com/howls-"
                                      "moving-castle-movie-poster-"
                                      "2004-1010261084.jpg",
                                      "https://www.youtube.com/watch?"
                                      "v=iwROgK94zcM")

my_neighbor_totoro = media.Animation("My neighbor Totoro",
                                     "https://d32qys9a6wm9no.cloudfront.net/"
                                     "images/movies/poster/dc/dc2208f9bbd11"
                                     "486d5dbbb9218e03017_500x735."
                                     "jpg?t=1499831918",
                                     "https://www.youtube.com/watch?"
                                     "v=92a7Hj0ijLs")

the_animatrix = media.Animation("The Animatrix",
                                "https://upload.wikimedia.org/wikipedia"
                                "/en/d/d2/The-animatrix-poster.jpeg",
                                "https://www.youtube.com/watch?v=_plomSww2ss")

grave_of_fire_flies = media.Animation("Grave of fire flies",
                                      "http://img.moviepostershop.com/grave"
                                      "-of-the-fireflies-movie-poster"
                                      "-1988-1020773661.jpg",
                                      "https://www.youtube.com/watch?"
                                      "v=4vPeTSRd580")

# Add animations to an array
animations = [spirited_away,
              akira,
              princess_mononoke,
              porco_rosso,
              castle_in_the_sky,
              ponyo,
              howls_moving_castle,
              my_neighbor_totoro,
              the_animatrix,
              grave_of_fire_flies]

# Generate website by calling open_movies_page()
fresh_tomatoes.open_movies_page(animations)
