import attr
from home_theater.tuner import Tuner
from home_theater.dvd_player import DvdPlayer


@attr.s
class Amplifier:
    tuner = attr.ib(Tuner)
    dvd_player = attr.ib(DvdPlayer)

    def on(self):
        print("Amplifier on")

    def off(self):
        print("Amplifier off")

    def set_dvd(self, dvd):
        self.dvd_player = dvd

    def set_tuner(self, tuner):
        self.tuner = tuner

    def set_volume(self, volume):
        print(f"volume = {volume}")
