import media
import fresh_tomatoes
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

#create media list and html page
movies = [imitation_game, shutter_island, man_who_knew_infinity]
fresh_tomatoes.open_movies_page(movies)
