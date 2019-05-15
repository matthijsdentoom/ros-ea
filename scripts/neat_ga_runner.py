#!/usr/bin/env python
import os
import rospy

import neat

from os.path import expanduser
from ros_robot_experiment import ROSSimultaneRobotExperiment
from message_parsing import NEATROSEncoder



def neat_run():

    experiment_name = 'NEAT'
    num_generations = 100
    num_runs = 5
    config_location = 'config-feedforward'

    # Create learning configuration.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, config_location)
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    try:
        experiment = ROSSimultaneRobotExperiment(config, None, num_generations, NEATROSEncoder, experiment_name,
                                                 base_directory=expanduser("~") + '/Desktop/obstacle_light_neat2/')

        for i in range(num_runs):
            experiment.run(experiment_name + str(i))

    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':

    neat_run()
