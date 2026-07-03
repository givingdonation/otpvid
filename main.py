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
        bg = ImageMobject("backdoordark.jpg")

        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])

        # Stretch to fill the entire frame
        bg.stretch_to_fit_width(config.frame_width)
        bg.stretch_to_fit_height(config.frame_height)

        #image.height = 7
        self.add(bg)

        aliceup = Text("alice", font="Xanmono").to_edge(UP)
        bobdown = Text("bob", font="Xanmono").to_edge(DOWN)
        self.play(AddTextLetterByLetter(aliceup))
        self.play(AddTextLetterByLetter(bobdown))

        closed = SVGMobject("mail_closed.svg").to_edge(UP).shift(DOWN)
        self.play(FadeIn(closed))
        self.play(closed.animate.to_edge(DOWN).shift(UP), run_time=1.5)
        self.play(FadeOut(closed))
        #open_mail = SVGMobject("mail_open.svg")


        self.wait()
        self.play(FadeOut(VGroup(aliceup,bobdown)))
        key = Text("3150704", font="Xanmono")
        self.play(AddTextLetterByLetter(key))
        self.play(FadeOut(key))
        dice = ImageMobject("dice.png").scale(0.25).to_edge(UP)
        self.play(FadeIn(dice))





        
        

        #self.remove(aliceup)
        #self.remove(bobdown)
        

        #body   = Text("This is the detail.").move_to(ORIGIN)
        #self.play(Write(title))
        #self.wait(1)
        #self.play(FadeIn(body, shift=UP * 0.3))
        #self.wait(1.5)
        #self.play(FadeIn(footer))
        #self.wait(1)

        # Fade everything out before next sequence
        #self.play(FadeOut(VGroup(title, body, footer)))
