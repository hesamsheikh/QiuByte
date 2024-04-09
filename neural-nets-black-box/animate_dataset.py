from manim import *
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

num_samples = 500
inner_radius = 1
outer_radius = 4
noise_level = 0.4

# Generate inner circle data with noise
theta_inner = np.linspace(0, 2*np.pi, num_samples)
x_inner = inner_radius * np.cos(theta_inner) + np.random.normal(0, noise_level, size=num_samples)
y_inner = inner_radius * np.sin(theta_inner) + np.random.normal(0, noise_level, size=num_samples)
labels_inner = np.zeros(num_samples)

# Generate outer circle data with noise
theta_outer = np.linspace(0, 2*np.pi, num_samples)
x_outer = outer_radius * np.cos(theta_outer) + np.random.normal(0, noise_level, size=num_samples)
y_outer = outer_radius * np.sin(theta_outer) + np.random.normal(0, noise_level, size=num_samples)
labels_outer = np.ones(num_samples)

# Concatenate data
X = np.concatenate([np.column_stack([x_inner, y_inner]), np.column_stack([x_outer, y_outer])])
y = np.concatenate([labels_inner, labels_outer])

class DatasetAnimation(Scene):
    def construct(self):
        # Add all points to the scene
        points = VGroup(*[Dot().move_to(np.append(X[i], 0)) for i in range(X.shape[0])])

        # Create VGroups for inner and outer circle points
        inner_points = VGroup(*[point for i, point in enumerate(points) if y[i] == 0])
        outer_points = VGroup(*[point for i, point in enumerate(points) if y[i] == 1])
        self.add(inner_points, outer_points)

        self.wait(1)  # Wait for 1 second after adding all points

        # Animate the color change of inner circle points to red
        self.play(ApplyMethod(inner_points.set_color, RED), run_time=1)

        self.wait(2)  # Wait for 1 second after coloring inner circle points

        # Animate the color change of outer circle points to blue
        self.play(ApplyMethod(outer_points.set_color, BLUE), run_time=1)

        self.wait(2)  # Wait for 1 second after coloring outer circle points