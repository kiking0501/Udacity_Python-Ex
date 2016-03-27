import Ex6_media
import fresh_tomatoes
toy_story = Ex6_media.Movie("Toy Story",
                           "A story of a boy and his toys that come to life",
                           "https://yt3.ggpht.com/-FI0u1v-lTJo/AAAAAAAAAAI/AAAAAAAAAAA/msi0wk3w3BQ/s100-c-k-no/photo.jpg",
                           "https://www.youtube.com/watch?v=x9EF-r4LMUI")
#print(toy_story.storyline)

avator = Ex6_media.Movie("Avatar",
                         "A marine on an alien planet",
                         "https://yt3.ggpht.com/-FI0u1v-lTJo/AAAAAAAAAAI/AAAAAAAAAAA/msi0wk3w3BQ/s100-c-k-no/photo.jpg",
                         "https://www.youtube.com/watch?v=x9EF-r4LMUI")
#print(avator.storyline)
#avator.show_trailor()

movie = [toy_story, avator]
fresh_tomatoes.open_movies_page(movie)
