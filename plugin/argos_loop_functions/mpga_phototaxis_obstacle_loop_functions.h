#ifndef MPGA_PHOTOTAXIS_OBSTACLE_LOOP_FUNCTIONS_H
#define MPGA_PHOTOTAXIS_OBSTACLE_LOOP_FUNCTIONS_H

/* ARGoS-related headers */
#include <argos3/core/utility/math/rng.h>
#include <argos3/plugins/robots/foot-bot/simulator/footbot_entity.h>

#include "mpga_phototaxis_loop_functions.h"

#include "ros/ros.h"
#include "std_srvs/Empty.h"
#include "ma_evolution/SimScore.h"

/****************************************/
/****************************************/

using namespace argos;

class CMPGAPhototaxisObstacleLoopFunctions : public CMPGAPhototaxisLoopFunctions
{

public:

    CMPGAPhototaxisObstacleLoopFunctions();

    virtual ~CMPGAPhototaxisObstacleLoopFunctions() = default;

    virtual void Reset() override;

    virtual void SetStartLocation() override;

    virtual void PostStep() override;

    /* Calculates the performance of the robot in a trial */
    virtual Real Score() override;

protected:

    /**
     * Calculate the fitness based on a distance to the object.
     * @param distance      - distance to object.
     * @return              - Fitness based on distance.
     */
    virtual Real calculateFitness(Real distance);

    virtual Real CalculateStepScore();

    Real m_fScore;

    Real m_fMaxDistance;
};

#endif
