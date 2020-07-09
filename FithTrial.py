# Using trig function to calculate it
import math
def speeding_when_straight(waypoint, x,y):
    # speed up when it goes straight
    # when steering_angle and heading are 0 degree
    # and speed is more than 2.0
    # using rules of second cosine something forgot
    reward = 0
    a = math.sqrt((waypoint[0] - x)**2 + (waypoint[1] - (y-0.3))**2)
    b = 0.3
    c = math.sqrt((waypoint[0] - x)**2 + (waypoint[1] - y)**2)
    A = math.acos(((b**2 + c**2)-a**2)/(2*b*c))
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
    # adding waypoints, x and y 20200708
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    heading = params['heading']
    closest_waypoints = params['closest_waypoints']
    waypoint_ahead = closest_waypoints[1]
    x = params['x']
    y = params['y']
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
    reward += speeding_when_straight(waypoint_ahead,
                                     x,
                                     y)
    return float(reward)
