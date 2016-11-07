#parent class
class Video():
    def __init__(self, duration, image, storyline,
                    title):
        self.duration = duration
        self.image = image
        self.storyline = storyline
        self.title = title

#movie subclass
class Movie(Video):
    def __init__(self, duration, image, storyline,title, link):
        Video.__init__(self, duration, image, storyline, title)
        self.link = link
#tvshow subclass
class TVShow(Video):
    def __init__(self, duration, image, storyline,
                    title, episode, season):
        Video.__init__(self, duration, image, storyline, title)
        self.episode = episode
        self.season = season
