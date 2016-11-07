import media
import fresh_tomatoes
#tv_shows are currently not available, implemented for later date
#instantiate tv_show objects
"""Object traits (in-order): duration, image, storyline, title,
                             episode, season"""

breaking_bad = media.TVShow(
    58,
    "http://www.gstatic.com/tv/thumb/tvbanners/9181462/p9181462_b_v8_aa.jpg",
    "A high school chemistry teacher diagnosed with \
    inoperable lung cancer turns to manufacturing   \
    and selling methamphetamine in order to secure  \
    his family's future.",
    "Breaking Bad",
    1,
    1)

how_i_met_your_mother = media.TVShow(
    30,
    "http://i2.listal.com/image/205965/600full-how-i-met-your-mother-poster.jpg",
    "A father recounts to his children, through a \
    series of flashbacks, the journey he and his  \
    four best friends took leading up to him      \
    meeting their mother.",
    "How I Met Your Mother",
    1,
    1)

#instantiate movie objects
"""Object traits (in-order): duration, image, storyline, title
                             link"""
imitation_game = media.Movie(
    150,
    "http://www.filmmusicnotes.com/wp-content/uploads/2015/01/imitation_game.jpg",
    "Alan Turing tries to crack the enigma code \
    with help from fellow mathematicians.",
    "The Imitation Game",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM")

shutter_island = media.Movie(
    138,
    "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
    "a U.S. marshal investigates the disappearance of \
    a murderess who escaped from a hospital for the   \
    criminally insane.",
    "Shutter Island",
    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

man_who_knew_infinity = media.Movie(
    140,
    "http://www.gridcitymagazine.com/wp-content/uploads/2016/09/The-Man-Who-Knew-Infinity-.jpg",
    " The story of the life and academic career of \
      the pioneer Indian mathematician,            \
      Srinivasa Ramanujan",
    "The Man Who Knew Infinity",
    "https://www.youtube.com/watch?v=oXGm9Vlfx4w")

zootopia = media.Movie(
    150,
    "https://resizing.flixster.com/5Fvk0wdYGnVfTRwTC0uvSCjWes0=/206x305/v1.bTsxMTMxODA2ODtwOzE3MjMwOzEyMDA7NDk5Ozc0MQ",
    "In a city of anthropomorphic animals, a rookie bunny cop \
     and a cynical con artist fox must work together to       \
     uncover a conspiracy.",
    "Zootopia",
    "https://www.youtube.com/watch?v=jWM0ct-OLsM")

big_hero_6 = media.Movie (
    160,
    "https://filmsoundtrackcenter.files.wordpress.com/2014/11/bighero6.jpg",
    "A boy and a robot save the world.",
    "Big Hero 6",
    "https://www.youtube.com/watch?v=z3biFxZIJOQ")

catch_me = media.Movie(
    135,
    "https://upload.wikimedia.org/wikipedia/en/4/4d/Catch_Me_If_You_Can_2002_movie.jpg",
    "The true story of a real fake",
    "Catch Me If You Can",
    "https://www.youtube.com/watch?v=71rDQ7z4eFg")

captain_america = media.Movie(
    132,
    "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
    "The First Avenger",
    "Captain America",
    "https://www.youtube.com/watch?v=JerVrbLldXw")

#create media list and html page
movies = [imitation_game, shutter_island, man_who_knew_infinity, zootopia,
          catch_me, big_hero_6, captain_america]

fresh_tomatoes.open_movies_page(movies)
