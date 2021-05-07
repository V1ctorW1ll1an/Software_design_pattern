# Welcome to Facade Pattern!

***Hey! I'm Victor, and I will explain through this directory, some concepts and implementation of the FACADE project pattern.***


# What is Facade?
***Facade is a structural design pattern that provides a simplified interface for a library, a framework, or any complex set of classes.***


## The problem

*Okay, after a brief definition of what a facade pattern is, let's watch a movie and relax, the hard work here is over, isn't it ?!
But, before watching the movie, we need to do some tasks:*

 1.  *turn on a popcorn machine*
 2.  *put the popcorn machine to work*
 3.  *dim the lights*
 4.  *down the screen*
 5.  *turn on the projector*
 6.  *configure the input of the projector to the DVD*
 7.  *put the projector in wide-screen mode*
 8.  *connect the audio amplifier*
 9.  *configure the amplifier input for the DVD*
 10. *configure the amplifier for surround sound*
 11.  *adjust the amplifier volume*
 12.  *turn on the DVD player*
 13.  *press 'play' on the DVD player*

*Well, after doing all these tasks, I wonder if it’s really worth watching a movie.
Can you imagine listening to a CD or radio, will the process be equally complex?*

## Let's see examples of some classes and methods

```python
# turns on the popcorn machine and activates the production of popcorn
	popper.on() 
	popper.pop() 
	
	# attenuates the lights to 10%
	lights.dim(10) 

	screen.down() # down the screen
	
	# turns on the projector 
	projector.on()
	projector.set_input(dvd)

	# Turn on the amplifier, set it to DVD and set the volume to 5.
	amp.on()
	amp.set_dvd(dvd)
	amp.set_volume(5)
	
	# Turn on the DVD player, and FINALLY play the movie
	dvd.on()
	dvd.play(movie)
```

## Solution

*Thinking about these problems, I created a class diagram with our HomeTheaterFacade.*

![enter image description here](https://user-images.githubusercontent.com/47677499/116305766-9efa8900-a77a-11eb-8602-33af9ec9106e.jpg)



 ***If you need the resources of the complex subsystem they will be there, but when you only need a simple interface, the facade will play that role.***

## It's code time

*Let's start by creating our classes, each with its own responsibility.*
>
>
***Tuner class***

```python
 class Tuner:  
      
     def on(self):  
     print("tuner on")  
      
      def off(self):  
     print("tuner off")  
      
      def set_frequency(self, frequency):  
     print(f"frequency set to {frequency}")
```

***Screen class***

```python
class Screen:  
  
 def up(self):  
 print("screen up")  
  
  def down(self):  
 print("screen down")
```


***Projector class***

```python
class Projector:  
  
 def on(self, movie):  
 print(f"projecting the movie {movie}")  
  
  def off(self):  
 print("projector off")
```

***Popcorn Machine class***

```python
class PopcornMachine:  
 def on(self):  
 print("Popcorn machine on")  
  
  def off(self):  
 print("Popcorn machine off")  
  
  def pop(self):  
 print("Popping Popcorn")
```

***DVD Player class***

```python
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
```
 ***Amplifier class***

```python
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
```
 ***Ambient Light class***

```python
class AmbientLight:  
 def on(self):  
 print("Light on")  
  
  def off(self):  
 print("Light off")  
  
  def dim(self, number):  
 print(f"Lights {number}%")
```

*All the classes we created above are example classes, which can be more complex classes, so it is important to use the facade pattern, the facade does not encapsulate the classes, it creates only an interface to deal with all the complex logic without having to expose for your user.*

*So, it's time to create our facade class to handle all the complexity of these classes and display them as a single, simple and easy-to-use class.*

***Facade Class***
```python
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
```
*As we can see, all the logic and work to watch the movie or stop watching it is in our "HomeTheaterFacade", the only job we have now is to call the facade methods and they guarantee the execution of all the complex logic and work arduous.*

*Now just create an instance of our "Home Theater Facade" class and call the method `watch_movie ()` or `end_movie ()`.*

```python
home_theater_facade = HomeTheaterFacade()  
  
home_theater_facade.watch_movie("hackers", 2, 20, 50)  
home_theater_facade.end_movie()
```
*Nothing prevents a facade from incorporating its own "intelligence" other than using the subsystem. For example, although our home theater facade does not incorporate any new behavior, it is smart enough to know that the popcorn machine must be turned on before starting to produce popcorn.*
*It is normal to confuse the facade design pattern with the Adapter pattern, the difference between the two patterns is not in the number of classes they "involve", but in their "intention". The purpose of the Adapter pattern is to change an interface to make it compatible with what the customer expects. The intention of the Facade pattern is to provide a simplified interface for a subsystem.*


***Well, thank you to everyone who took the time to read this brief explanation of this simple yet powerful pattern.***
