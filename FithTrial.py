# Using trig function to calculate it
def speeding_when_straight(steering_angle, heading,speed):
    # speed up when it goes straight
    # when steering_angle and heading are 0 degree
    # and speed is more than 2.0
    reward = 0
    if steering_angle == 0 and \
            heading == 0 and speed > 2.0:
        reward += 0.5
    return reward


def reward_function(params):
    """
    1. keep it center(don't steer to much)
    2. when it needs to go to straight speed up
    :param params: track_width, distance_from_center
                    steering_angle, speed, heading
    :return: reward
    """
    # var
    # all float
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    heading = params['heading']
    # reward var float
    reward = 0.0
    # keeping it center
    # no over steering
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward += 1e-3
    reward += speeding_when_straight(steering_angle, heading, speed)
    return float(reward)
