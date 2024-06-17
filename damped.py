from manim import *
import numpy as np

class DampedHarmonicMotion(Scene):
    def construct(self):
        # Title
        title = Text("Damped Harmonic Oscillator")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Step-by-step derivation
        equations = [
            MathTex("F = -kx"),  # Hooke's Law
            MathTex("F_d = -c \\frac{dx}{dt}"),  # Damping force
            MathTex("m \\frac{d^2 x}{dt^2} = -kx - c \\frac{dx}{dt}"),  # Total force
            MathTex("m \\frac{d^2 x}{dt^2} + c \\frac{dx}{dt} + kx = 0")  # Rearranged equation
        ]
        
        for eq in equations:
            self.play(Write(eq))
            self.wait(2)
            self.play(FadeOut(eq))

        characteristic_eq = MathTex("m r^2 + cr + k = 0")
        self.play(Write(characteristic_eq))
        self.wait(2)
        self.play(FadeOut(characteristic_eq))

        roots = MathTex("r = \\frac{-c \\pm \\sqrt{c^2 - 4mk}}{2m}")
        self.play(Write(roots))
        self.wait(2)
        self.play(FadeOut(roots))

        cases = [
            ("Underdamped (c^2 < 4mk)", "r = \\alpha \\pm i\\beta", "x(t) = e^{-\\alpha t} (A \\cos(\\beta t) + B \\sin(\\beta t))"),
            ("Critically damped (c^2 = 4mk)", "r = -\\frac{c}{2m}", "x(t) = (A + Bt) e^{-\\frac{c}{2m} t}"),
            ("Overdamped (c^2 > 4mk)", "r_1, r_2 = \\frac{-c \\pm \\sqrt{c^2 - 4mk}}{2m}", "x(t) = A e^{r_1 t} + B e^{r_2 t}")
        ]
        
        for case in cases:
            case_title = Text(case[0])
            case_roots = MathTex(case[1])
            case_solution = MathTex(case[2])
            self.play(Write(case_title))
            self.wait(1)
            self.play(Transform(case_title, case_roots))
            self.wait(1)
            self.play(Transform(case_title, case_solution))
            self.wait(2)
            self.play(FadeOut(case_title))

        self.show_plots()
    
    def show_plots(self):
        # Define parameters
        m = 1  # mass
        k = 1  # spring constant
        c_underdamped = 0.5  # damping coefficient for underdamped
        c_critical = 2  # damping coefficient for critically damped
        c_overdamped = 3  # damping coefficient for overdamped

        # Time range
        t = np.linspace(0, 10, 1000)

        # Underdamped case
        alpha_ud = c_underdamped / (2 * m)
        omega_ud = np.sqrt(k / m - alpha_ud**2)
        x_ud = lambda t: np.exp(-alpha_ud * t) * (np.cos(omega_ud * t) + np.sin(omega_ud * t))

        # Critically damped case
        alpha_cd = c_critical / (2 * m)
        x_cd = lambda t: (1 + t) * np.exp(-alpha_cd * t)

        # Overdamped case
        alpha_od1 = (c_overdamped + np.sqrt(c_overdamped**2 - 4 * m * k)) / (2 * m)
        alpha_od2 = (c_overdamped - np.sqrt(c_overdamped**2 - 4 * m * k)) / (2 * m)
        x_od = lambda t: np.exp(-alpha_od1 * t) + np.exp(-alpha_od2 * t)

        # Axes for plotting
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"include_numbers": True}
        )

        labels = axes.get_axis_labels(x_label="t", y_label="x(t)")

        self.play(Create(axes), Write(labels))

        # Create FunctionGraphs
        underdamped_plot = axes.plot(x_ud, color=BLUE)
        critically_damped_plot = axes.plot(x_cd, color=RED)
        overdamped_plot = axes.plot(x_od, color=GREEN)
        
        plots = [
            ("Underdamped", underdamped_plot),
            ("Critically Damped", critically_damped_plot),
            ("Overdamped", overdamped_plot)
        ]
        
        for plot in plots:
            plot_title = Text(plot[0]).to_edge(UP)
            self.play(Write(plot_title))
            self.wait(1)
            self.play(Create(plot[1]))
            self.wait(2)
            self.play(FadeOut(plot[1]), FadeOut(plot_title))

        self.play(FadeOut(axes), FadeOut(labels))

