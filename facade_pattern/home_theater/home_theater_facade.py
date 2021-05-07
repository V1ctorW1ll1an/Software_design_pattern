import attr
from home_theater.amplifier import Amplifier
from home_theater.tuner import Tuner
from home_theater.dvd_player import DvdPlayer
from home_theater.projector import Projector
from home_theater.ambient_light import AmbientLight
from home_theater.screen import Screen
from home_theater.popcorn_machine import PopcornMachine


@attr.s
class HomeTheaterFacade:
    tuner = Tuner()
    dvd_player = DvdPlayer()
    amplifier = Amplifier(dvd_player, tuner)
    projector = Projector()
    ambient_light = AmbientLight()
    screen = Screen()
    popcorn_machine = PopcornMachine()

    def watch_movie(self, movie, dim, frequency, volume):
        print("Get ready to watch a movie...")
        self.popcorn_machine.on()
        self.popcorn_machine.pop()
        self.ambient_light.dim(dim)
        self.screen.down()
        self.tuner.set_frequency(frequency)
        self.projector.on(movie)
        self.amplifier.on()
        self.amplifier.set_dvd(self.dvd_player)
        self.amplifier.set_volume(volume)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.popcorn_machine.off()
        self.ambient_light.on()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.dvd_player.off()
