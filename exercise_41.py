class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics


def sing_me_a_song(self):
    for line in self.lyrics:
        print(line)


happy_body = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
happy_body.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
