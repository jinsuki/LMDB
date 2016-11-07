class Video():
    def __init__(self, duration, image, storyline,
                    title, link):
        self.duration = duration
        self.image = image
        self.storyline = storyline
        self.title = title
        self.link = link
        def view_trailer():

class Movie(Video):
    def __init__(self, duration, image, storyline,
                    title, link):
        Video.__init__(self, duration, image, storyline, title, link)

class TVShow(Video):
    def __init__(self, duration, image, storyline,
                    title, link, episode, season):
        Video.__init__(self, duration, image, storyline, title, link)
        self.episode = episode
        self.season = season
