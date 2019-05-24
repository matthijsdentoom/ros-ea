#!/usr/bin/env python
import os
from os.path import expanduser

import rospy

import neat

from ros_robot_experiment import ROSRobotExperiment, ROSSimultaneRobotExperiment
from message_parsing import NEATROSEncoder
from run_and_visualize import ScenarioVisualiser
from simulation_control import SimulationController
from tools.draw_functions import draw_nn


def two_layer_run():

    experiment_name = 'NEAT'
    num_generations = 1
    num_runs = 1
    config_location = 'config-feedforward-2-hidden-layers'
    base_directory = expanduser("~") + '/Desktop/two-layer-nn/'

    # Create learning configuration.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, config_location)
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    sim_control = SimulationController('ma_evolution', 'sim_phototaxis_obst_new_fitness.launch', 'feed-forward')

    try:
        sim_control.start_simulators()

        experiment = ROSRobotExperiment(config, num_generations, NEATROSEncoder, experiment_name,
                                                 base_directory=base_directory, cntrl_draw_func=draw_nn)

        for i in range(num_runs):
            experiment.run(experiment_name + str(i))

        sv = ScenarioVisualiser(experiment.sim_controllers, base_directory, NEATROSEncoder)
        sv.visualize_winner_paths()

        sim_control.stop_simulators()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':

    two_layer_run()
