from pygame import mixer


class sound:  # Sounds
    def __init__(self,
                 directory: str,
                 volume: float = 1.0,
                 play: bool = True,
                 loop: bool = False):
        # Create/Add sounds
        mixer.init()

        self.directory: str = directory
        self.play, self.loop = play, loop
        self.volume: float = volume

        # $ To create $ #
        start = mixer.Sound(self.directory)
        start.set_volume(self.volume)

        # $ Sound Loop $ #
        if self.play:
            if self.loop: start.play(-1)
            else: start.play()
        else: self.start.stop()
