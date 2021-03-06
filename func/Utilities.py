import numpy as np
import pdb


def Curvature(s, PointAndTangent):
    """curvature computation
    s: curvilinear abscissa at which the curvature has to be evaluated
    PointAndTangent: points and tangent vectors defining the map (these quantities are initialized in the map object)
    """
    TrackLength = PointAndTangent[-1, 3] + PointAndTangent[-1, 4]

    # In case on a lap after the first one
    while (s > TrackLength):
        s = s - TrackLength

    # Given s \in [0, TrackLength] compute the curvature
    # Compute the segment in which system is evolving
    index = np.all([[s >= PointAndTangent[:, 3]], [s < PointAndTangent[:, 3] + PointAndTangent[:, 4]]], axis=0)

    i = int(np.where(np.squeeze(index))[0])
    curvature = PointAndTangent[i, 5]

    return curvature


def getAngle(s, epsi, PointAndTangent):
    """curvature computation
    s: curvilinear abscissa at which the curvature has to be evaluated
    PointAndTangent: points and tangent vectors defining the map (these quantities are initialized in the map object)
    """
    TrackLength = PointAndTangent[-1, 3] + PointAndTangent[-1, 4]

    # In case on a lap after the first one
    while (s > TrackLength):
        s = s - TrackLength

    # Given s \in [0, TrackLength] compute the curvature
    # Compute the segment in which system is evolving
    index = np.all([[s >= PointAndTangent[:, 3]], [s < PointAndTangent[:, 3] + PointAndTangent[:, 4]]], axis=0)

    i = int(np.where(np.squeeze(index))[0])

    if i > 0:
        ang = PointAndTangent[i - 1, 2]
    else:
        ang = 0

    if PointAndTangent[i, 5] == 0:
        r = 0
    else:
        r = 1 / PointAndTangent[i, 5]  # Radius of curvature

    if r == 0:
        # On a straight part of the circuit
        angle_at_s = ang + epsi
    else:
        # On a curve
        cumulative_s = PointAndTangent[i, 3]
        relative_s = s - cumulative_s
        spanAng = relative_s / np.abs(r)  # Angle spanned by the circle
        psi = wrap(ang + spanAng * np.sign(r))  # Angle of the tangent vector at the last point of the segment
        # pdb.set_trace()
        angle_at_s = psi + epsi

    return angle_at_s


def wrap(angle):
    if angle < -np.pi:
        w_angle = 2 * np.pi + angle
    elif angle > np.pi:
        w_angle = angle - 2 * np.pi
    else:
        w_angle = angle

    return w_angle
