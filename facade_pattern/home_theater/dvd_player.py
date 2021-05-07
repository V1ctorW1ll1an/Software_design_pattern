class DvdPlayer:

    def on(self):
        print("Connected DVD player")

    def off(self):
        print("Disconnected DVD player")

    def play(self, movie):
        print(f"Watching the movie {movie}")

    def stop(self):
        print("dvd player stopped")

    def eject(self):
        print("Ejected DVD player")

    def inject(self):
        print("Injected DVD player")
