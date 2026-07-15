from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class OtpVid(VoiceoverScene):
    def construct(self):
        #circle = Circle()  # create a circle
        #circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        #square = Square()  # create a square
        #square.flip(RIGHT)  # flip horizontally
        #square.rotate(-3 * TAU / 8)  # rotate a certain amount

        #self.play(Create(square))  # animate the creation of the square
        #self.play(Transform(square, circle))  # interpolate the square into the circle
        #self.play(FadeOut(square))  # fade out animation

        self.set_speech_service(GTTSService(lang="en", tld="com"))


        bg = ImageMobject("backdoordark.jpg")

        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])

        # Stretch to fill the entire frame
        bg.stretch_to_fit_width(config.frame_width)
        bg.stretch_to_fit_height(config.frame_height)

        #image.height = 7
        self.add(bg)

        aliceup = Text("alice", font="Xanmono").to_edge(UP)
        bobdown = Text("bob", font="Xanmono").to_edge(DOWN)
        #open_mail = SVGMobject("mail_open.svg")
        with self.voiceover(text="If you want to send your friend a message that is impossible for anyone else to read, do this.") as tracker:
            self.play(AddTextLetterByLetter(aliceup))
            self.play(AddTextLetterByLetter(bobdown))
            closed = SVGMobject("mail_closed.svg").to_edge(UP).shift(DOWN)
            self.play(FadeIn(closed))
            self.play(closed.animate.to_edge(DOWN).shift(UP), run_time=1.5)
            self.play(FadeOut(closed))
            #self.wait()
            self.play(FadeOut(VGroup(aliceup,bobdown)))
        key = Text("3150704", font="Xanmono")
        with self.voiceover(text="Start by making a truly random digit code.") as tracker:
            
            self.play(AddTextLetterByLetter(key), run_time=tracker.duration*0.75)
            self.play(FadeOut(key), run_time=tracker.duration*0.25)
        with self.voiceover(text="You could use dice and a table like this one."):
            dice = ImageMobject("dice.png").scale(0.25).to_edge(UP)
            self.play(FadeIn(dice))
            board = ImageMobject("diceboard.png").scale_to_fit_width(config.frame_width).to_edge(DOWN)
            self.play(FadeIn(board))
            self.play(FadeOut(Group(dice,board)))
        keyIcon = SVGMobject("keyicon.svg")
        onetime = ImageMobject("onetime.png").scale_to_fit_width(config.frame_width).to_edge(DOWN)
        
        with self.voiceover(text="This code is the key you can only use once.") as tracker:
            self.play(AddTextLetterByLetter(key.to_edge(UP)))
            self.play(FadeIn(keyIcon.to_edge(UP).shift(DOWN)))
            self.play(FadeIn(onetime))
            #self.play(FadeOut(key))
            self.play(FadeOut(Group(key,keyIcon,onetime)))


        with self.voiceover(text="You and your friend should memorize or safely store this.") as tracker:
            self.play(FadeIn(keyIcon.move_to(ORIGIN)))
            box = SurroundingRectangle(keyIcon, color=WHITE)
            self.play(FadeIn(box))
            self.play(FadeOut(box),FadeOut(keyIcon))
        
        plaintext = Text("GO EAST", font="Xanmono")
        plaincode = Text("6603457", font="Xanmono")

        with self.voiceover(text="When you want to send a message to your friend, first turn your message into a digit code.") as tracker:
            self.play(AddTextLetterByLetter(plaintext))




        #with self.voiceover(text="") as tracker:



        


            

            
        





        
        

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
