#!/usr/bin/env python
import os
import neat

from os.path import expanduser

from neat.generation import DefaultGeneration

from predefined_experiments import nn_based_experiment


def neat_run():

    num_generations = 100
    num_runs = 5
    config_location = 'configs/config-feedforward'
    base_directory = expanduser("~") + '/Desktop/obstacle_light_neat2/'
    launch_file = 'sim_phototaxis_obst_new_fitness.launch'

    # Create learning configuration.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, config_location)
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         DefaultGeneration,
                         config_path)

    nn_based_experiment(launch_file, config, base_directory, num_generations, num_runs)


if __name__ == '__main__':

    neat_run()
