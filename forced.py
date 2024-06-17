from manim import *

class ForcedVibration(Scene):
    def construct(self):
        # Title
        title = Text("Forced Vibration Using Hooke's Law", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Differential Equation
        equation = MathTex("m \\ddot{x} + c \\dot{x} + k x = F(t)", color=BLUE)
        self.play(Write(equation))
        self.wait(2)
        self.play(FadeOut(equation))

        # Step 1: Solve the Homogeneous Equation
        step1_title = Text("1. Solve the Homogeneous Equation", color=GREEN)
        self.play(Write(step1_title))
        self.wait(1)
        self.play(FadeOut(step1_title))

        hom_eq = MathTex("m \\ddot{x} + c \\dot{x} + k x = 0", color=BLUE)
        self.play(Write(hom_eq))
        self.wait(2)
        self.play(FadeOut(hom_eq))

        char_eq = MathTex("m r^2 + c r + k = 0", color=ORANGE)
        self.play(Write(char_eq))
        self.wait(2)
        self.play(FadeOut(char_eq))

        r_solutions = MathTex("r = \\frac{-c \\pm \\sqrt{c^2 - 4mk}}{2m}", color=PINK)
        self.play(Write(r_solutions))
        self.wait(2)
        self.play(FadeOut(r_solutions))

        # Step 2: Find the Wronskian
        step2_title = Text("2. Find the Wronskian", color=GREEN)
        self.play(Write(step2_title))
        self.wait(1)
        self.play(FadeOut(step2_title))

        wronskian_def = MathTex("W(x_1, x_2) = \\begin{vmatrix} x_1 & x_2 \\\\ \\dot{x}_1 & \\dot{x}_2 \\end{vmatrix}", color=BLUE)
        self.play(Write(wronskian_def))
        self.wait(2)
        self.play(FadeOut(wronskian_def))

        wronskian_example = MathTex("W = x_1 \\dot{x}_2 - x_2 \\dot{x}_1", color=ORANGE)
        self.play(Write(wronskian_example))
        self.wait(2)
        self.play(FadeOut(wronskian_example))

        # Step 3: Particular Solution using Variation of Parameters
        step3_title = Text("3. Particular Solution using Variation of Parameters", color=GREEN)
        self.play(Write(step3_title))
        self.wait(1)
        self.play(FadeOut(step3_title))

        particular_solution = MathTex("x_p(t) = u_1(t)x_1(t) + u_2(t)x_2(t)", color=BLUE)
        self.play(Write(particular_solution))
        self.wait(2)
        self.play(FadeOut(particular_solution))

        u1_eq = MathTex("u_1'(t)x_1 + u_2'(t)x_2 = 0", color=ORANGE)
        self.play(Write(u1_eq))
        self.wait(2)
        self.play(FadeOut(u1_eq))

        u2_eq = MathTex("u_1'(t)\\dot{x}_1 + u_2'(t)\\dot{x}_2 = \\frac{F(t)}{m}", color=PINK)
        self.play(Write(u2_eq))
        self.wait(2)
        self.play(FadeOut(u2_eq))

        # Step 4: General Solution
        step4_title = Text("4. General Solution", color=GREEN)
        self.play(Write(step4_title))
        self.wait(1)
        self.play(FadeOut(step4_title))

        general_solution = MathTex("x(t) = x_h(t) + x_p(t)", color=BLUE)
        self.play(Write(general_solution))
        self.wait(2)
        self.play(FadeOut(general_solution))

        # Step 5: Plot the Solution
        step5_title = Text("5. Plot the Solution", color=GREEN)
        self.play(Write(step5_title))
        self.wait(1)
        self.play(FadeOut(step5_title))

        plot_axes = Axes(
            x_range=[0, 10, 1], y_range=[-2, 2, 0.5],
            x_length=10, y_length=6,
            axis_config={"color": BLUE}
        ).add_coordinates()

        plot_graph = plot_axes.plot(lambda x: 2 * np.exp(-0.1 * x) * np.cos(2 * x), x_range=[0, 10], color=RED)
        plot_label = plot_axes.get_graph_label(plot_graph, label=Tex("x(t)"), x_val=10, direction=UR, color=RED)

        self.play(Create(plot_axes))
        self.play(Create(plot_graph))
        self.play(Write(plot_label))
        self.wait(2)

        self.play(FadeOut(plot_axes), FadeOut(plot_graph), FadeOut(plot_label))

