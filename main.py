from manim import *
class OtpVid(Scene):
    def construct(self):
        #circle = Circle()  # create a circle
        #circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        #square = Square()  # create a square
        #square.flip(RIGHT)  # flip horizontally
        #square.rotate(-3 * TAU / 8)  # rotate a certain amount

        #self.play(Create(square))  # animate the creation of the square
        #self.play(Transform(square, circle))  # interpolate the square into the circle
        #self.play(FadeOut(square))  # fade out animation
        image = ImageMobject("backdoordark.jpg")
        image.height = 7
        self.add(image)

        text = Text("Alice", font="Xanmono")
        self.play(AddTextLetterByLetter(text))
        self.wait()
        self.remove(text)
