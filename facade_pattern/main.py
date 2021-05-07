from home_theater.home_theater_facade import HomeTheaterFacade

if __name__ == '__main__':
    home_theater_facade = HomeTheaterFacade()

    home_theater_facade.watch_movie("hackers", 2, 20, 50)
    print("")
    home_theater_facade.end_movie()
