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

        self.set_speech_service(GTTSService(lang="en", tld="com",global_speed=1.25))


        bg = ImageMobject("backdoordark.jpg")

        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])

        # Stretch to fill the entire frame
        bg.stretch_to_fit_width(config.frame_width)
        bg.stretch_to_fit_height(config.frame_height)

        #image.height = 7
        self.add(bg)

        aliceup = Text("alice", font="Xanmono").to_edge(UP)
        bobdown = Text("bob", font="Xanmono").to_edge(DOWN)
        open_mail = SVGMobject("mail_open.svg")
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
            self.play(AddTextLetterByLetter(plaintext),run_time=tracker.duration * 0.15)
            self.play(FadeTransformPieces(plaintext, plaincode.shift(DOWN)),run_time=tracker.duration * 0.7)
            self.play(FadeOut(plaincode),run_time=tracker.duration * 0.15)

        with self.voiceover(text="You could use a straddling checkerboard to do this.") as tracker:
            checkerboard = ImageMobject("checkerboard.png").scale_to_fit_width(config.frame_width)
            self.play(FadeIn(checkerboard))
            self.wait(1)
            self.play(FadeOut(checkerboard))
        
        key = Text("3150704", font="Xanmono")
        plaincode = Text("6603457", font="Xanmono")

        with self.voiceover(text="Then subtract each digit in your key from a digit in the same position from your message.") as tracker:
            self.play(AddTextLetterByLetter(key))
            self.play(FadeOut(key[:6]),key[6].animate.scale(3.5).to_edge(RIGHT))

            self.play(AddTextLetterByLetter(plaincode.shift(UP * 2)))
            self.play(FadeOut(plaincode[:6]),plaincode[6].animate.scale(3.5).to_corner(UR))
            
            hbar = Rectangle(height=0.05, width=config.frame_width,stroke_color=WHITE,fill_opacity=1.0).next_to(key,DOWN)
            minus = Text("-",font="Xanmono")
            self.play(FadeIn(minus.scale(3).to_edge(LEFT)),FadeIn(hbar))
            three = Text("3",font="Xanmono")
            self.play(FadeIn(three.scale(3.5).to_corner(DR)))

            self.play(FadeOut(key[6]),FadeOut(plaincode[6]),FadeOut(hbar),FadeOut(minus), FadeOut(three))
        
        key = Text("3150704", font="Xanmono")
        plaincode = Text("6603457", font="Xanmono")

        with self.voiceover(text="If the key digit is more than the message digit, add ten to the message digit.") as tracker:
            self.play(AddTextLetterByLetter(key))
            self.play(FadeOut(key[:4]),FadeOut(key[5:]),key[4].animate.scale(3.5).to_edge(RIGHT))

            self.play(AddTextLetterByLetter(plaincode.shift(UP * 2)))
            self.play(FadeOut(plaincode[:4]),FadeOut(plaincode[5:]),plaincode[4].animate.scale(3.5).to_corner(UR))
            
            hbar = Rectangle(height=0.05, width=config.frame_width,stroke_color=WHITE,fill_opacity=1.0).next_to(key,DOWN)
            minus = Text("-",font="Xanmono")
            ten = Text("+1",font="Xanmono")
            self.play(FadeIn(minus.scale(3).to_edge(LEFT)),FadeIn(ten.scale(1.75).to_corner(UL)),FadeIn(hbar))
            three = Text("7",font="Xanmono")
            self.play(FadeIn(three.scale(3.5).to_corner(DR)))

            self.play(FadeOut(key[4]),FadeOut(plaincode[4]),FadeOut(hbar),FadeOut(minus), FadeOut(three),FadeOut(ten))
            
        ciphertext = Text("3553753", font="Xanmono")
        closed = SVGMobject("mail_closed.svg").to_edge(UP).shift(DOWN)
        with self.voiceover(text="Then send the digits you get from the subtractions to your friend.") as tracker:
            self.play(AddTextLetterByLetter(ciphertext.to_edge(UP)))
            self.play(FadeIn(open_mail.to_edge(UP).shift(DOWN)))
            self.play(ShrinkToCenter(ciphertext))

            
            self.play(Transform(open_mail,closed))
            self.remove(closed)
            self.play(AddTextLetterByLetter(aliceup))
            self.play(AddTextLetterByLetter(bobdown))
            
            self.play(open_mail.animate.to_edge(DOWN).shift(UP))
            #self.play()
            
            #self.wait()
            self.play(FadeOut(open_mail),FadeOut(VGroup(aliceup,bobdown)))

        ciphertext = Text("3553753", font="Xanmono")
        closed = SVGMobject("mail_closed.svg")
        open_mail = SVGMobject("mail_open.svg").to_edge(DOWN).shift(UP)
        key = Text("3150704", font="Xanmono").shift(DOWN)
        plaincode = Text("6603457", font="Xanmono")

        with self.voiceover(text="If you receive a message like this from your friend, add back each digit from the key into what they sent. Do not carry between digits.") as tracker:
            self.play(FadeIn(closed.to_edge(DOWN).shift(UP)))
            self.play(Transform(closed,open_mail))
            self.remove(open_mail)
            self.play(GrowFromCenter(ciphertext))
            self.play(FadeOut(closed))
            self.play(ciphertext.animate.shift(UP))
            plus = Text("+",font="Xanmono")
            hbar = Rectangle(height=0.05, width=config.frame_width,stroke_color=WHITE,fill_opacity=1.0).next_to(key,DOWN)
            self.play(FadeIn(plus),FadeIn(key),FadeIn(hbar))
            self.play(AddTextLetterByLetter(plaincode.next_to(hbar,DOWN)))
            self.play(FadeOut(plus),FadeOut(hbar),FadeOut(key),FadeOut(ciphertext))

        
        plaintext = Text("GO EAST", font="Xanmono")

        with self.voiceover(text="Then you can turn the digit code back into a message you can read.") as tracker:
            self.play(plaincode.animate.move_to(ORIGIN),run_time=tracker.duration * 0.15)
            #self.play(AddTextLetterByLetter(plaincode))
            self.play(FadeTransformPieces(plaincode, plaintext.shift(DOWN)),run_time=tracker.duration * 0.7)
            self.play(FadeOut(plaintext),run_time=tracker.duration * 0.15)
        

        with self.voiceover(text="Make sure the key is longer than or equal to the code from the message.") as tracker:
            arrow_1 = Arrow(start=LEFT, end=RIGHT,tip_shape=StealthTip, color=GREEN).scale_to_fit_width(config.frame_width).to_edge(UP)
            key = Text("3150704", font="Xanmono").to_edge(UP).shift(DOWN)
            plaincode = Text("6603457", font="Xanmono").to_edge(UP).shift(DOWN * 3)
            arrow_2 = Arrow(start=LEFT, end=RIGHT,tip_shape=StealthTip, color=GREEN).scale_to_fit_width(config.frame_width).next_to(plaincode,UP)
            self.play(GrowArrow(arrow_1, point_color=RED),AddTextLetterByLetter(key))
            self.play(GrowArrow(arrow_2, point_color=RED),AddTextLetterByLetter(plaincode))
            self.play(FadeOut(Group(arrow_1,arrow_2,key,plaincode)))
            
        closed = SVGMobject("mail_closed.svg").shift(UP * 2)
        with self.voiceover(text="Then the message will be just as secret as the key.") as tracker:
            box2 = SurroundingRectangle(closed, color=WHITE)
            self.play(FadeIn(closed),run_time=tracker.duration * 0.3)

            equals = Text("=", font="Xanmono").scale(2)
            self.play(FadeIn(box2),FadeIn(equals),run_time=tracker.duration * 0.4)

            keyIcon.shift(DOWN * 2)

            box = SurroundingRectangle(keyIcon, color=WHITE)
            self.play(FadeIn(keyIcon),FadeIn(box),run_time=tracker.duration * 0.3)
            

            self.play(FadeOut(box),FadeOut(box2),FadeOut(keyIcon),FadeOut(closed),FadeOut(equals))







            



            

            



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
