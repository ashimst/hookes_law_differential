from manim import *

class HookesLawIllustration(Scene):
    def construct(self):
        # Positions for the springs and masses
        natural_pos = UP * 2.5
        equilibrium_pos = ORIGIN
        motion_pos = DOWN * 2.5

        # Adding explanations
        explanation_text = Text("Spring Mass System", t2c={'Spring Mass System': YELLOW}).scale(0.5)
        explanation_text.to_edge(UP)
        self.play(Write(explanation_text))
        self.wait(2)

        # Natural position of the spring
        natural_spring, natural_mass = self.create_spring_with_mass(L=2, num_coils=15, spring_thickness=0.2, mass_scale=1.2)
        natural_spring.move_to(natural_pos)
        natural_mass.move_to(natural_spring.get_end())  # Move mass to the end of the spring
        natural_text = Text("1. Natural position of the spring", t2c={'Natural position': BLUE}).scale(0.5)
        natural_text.next_to(natural_spring, LEFT)

        # Equilibrium position of the spring with mass
        equilibrium_spring, equilibrium_mass = self.create_spring_with_mass(L=2, num_coils=15, spring_thickness=0.2, mass_scale=1.2)
        equilibrium_spring.move_to(equilibrium_pos)
        equilibrium_mass.move_to(equilibrium_spring.get_end())  # Move mass to the end of the spring
        equilibrium_text = Text("2. Equilibrium: mg = ks", t2c={'Equilibrium': BLUE}).scale(0.5)
        equilibrium_text.next_to(equilibrium_spring, LEFT)

        # Spring in motion
        motion_spring, motion_mass = self.create_spring_with_mass(L=3, num_coils=15, spring_thickness=0.2, mass_scale=1.2)
        motion_spring.move_to(motion_pos)
        motion_mass.move_to(motion_spring.get_end())  # Move mass to the end of the spring
        motion_text = Text("3. Spring in motion", t2c={'motion': BLUE}).scale(0.5)
        motion_text.next_to(motion_spring, LEFT)

        # Adding elements to the scene
        self.play(Create(natural_spring), Create(natural_mass), Write(natural_text))
        self.wait(1)
        self.play(Create(equilibrium_spring), Create(equilibrium_mass), Write(equilibrium_text))
        self.wait(1)
        self.play(Create(motion_spring), Create(motion_mass), Write(motion_text))
        self.wait(2)

    def create_spring_with_mass(self, L=2, num_coils=10, spring_thickness=0.1, mass_scale=1.0):
        spring = self.create_spring(L, num_coils, thickness=spring_thickness)
        mass = self.create_mass(scale_factor=mass_scale)
        spring_with_mass = VGroup(spring, mass)
        return spring_with_mass

    def create_spring(self, L=2, num_coils=10, thickness=0.1):
        spring = VMobject()
        points = []
        for i in range(num_coils * 2 + 1):
            x = i / (num_coils * 2) * L
            y = thickness * (-1) ** i
            points.append([x, y, 0])
        spring.set_points_smoothly(points)
        spring.stretch_to_fit_height(thickness)
        return spring

    def create_mass(self, scale_factor=1.0):
        mass = Circle(radius=0.3 * scale_factor, fill_color=RED, fill_opacity=1, stroke_width=0)
        return mass

if __name__ == "__main__":
    scene = HookesLawIllustration()
    scene.render()


