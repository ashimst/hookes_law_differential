from manim import *

class HookeLawScene(Scene):
    def construct(self):
        # Statement of Hooke's Law
        statement = Tex("Hooke's Law:", font_size=48)
        statement.to_edge(UP)
        self.play(Write(statement))
        self.wait(1)

        law_text = Tex(
            r"The force ($F$) exerted by a spring is proportional to",
            r"the displacement ($x$) from its equilibrium position,",
            r"with a proportionality constant ($k$):"
        )
        law_text.scale(0.8)
        law_text.next_to(statement, DOWN, buff=1)
        self.play(Write(law_text))
        self.wait(2)

        formula = MathTex(r"F = -k \cdot x")
        formula.scale(1.8)
        formula.next_to(law_text, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(3)

        # Fade out statement and law text
        self.play(FadeOut(statement), FadeOut(law_text), FadeOut(formula))
        self.wait(1)

        # Explanation of terms
        # Creating spring and block
        spring = DashedLine(UP, DOWN, color=BLUE)
        spring.move_to(ORIGIN)
        block = Square(side_length=1, color=GREEN)
        block.move_to(spring.get_end())

        self.play(Create(spring), Create(block))
        self.wait(1)

        # Arrow for displacement
        arrow = Arrow(ORIGIN, 2*DOWN, color=RED)
        arrow.next_to(block, DOWN, buff=0.2)
        self.play(Create(arrow))
        self.wait(0.5)

        # Label for displacement
        displacement_label = MathTex("x", color=RED)
        displacement_label.next_to(arrow, DOWN, buff=0.1)
        self.play(Write(displacement_label))
        self.wait(0.5)

        # Force arrow
        force_arrow = Arrow(ORIGIN, 2*UP, color=YELLOW)
        force_arrow.next_to(block, UP, buff=0.2)
        self.play(Create(force_arrow))
        self.wait(0.5)

        # Label for force
        force_label = MathTex(r"F = -k \cdot x", color=YELLOW)
        force_label.next_to(force_arrow, UP, buff=0.1)
        self.play(Write(force_label))
        self.wait(2)

        # Fade out example demonstration
        self.play(FadeOut(spring), FadeOut(block),
                  FadeOut(arrow), FadeOut(displacement_label),
                  FadeOut(force_arrow), FadeOut(force_label))
        self.wait(1)
