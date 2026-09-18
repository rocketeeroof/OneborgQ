from typing import override

from rlbot.flat import BallAnchor, ControllerState, GamePacket
from rlbot.managers import Bot
from rlbot_flatbuffers import CarAnchor

from util.ball_prediction_analysis import find_slice_at_time
from util.boost_pad_tracker import BoostPadTracker
from util.drive import steer_toward_target
from util.sequence import ControlStep, Sequence
from util.vec import Vec3

from extra_utils.controller import controller
from extra_utils.situation import situation

class default_strategy():
    def __init__(self):
        self.x = 0

    def run(self, sit):
        packet = sit.packet
        my_car = packet.players[sit.own_index]
        opposing_car = packet.players[1 - sit.own_index]
        car_location = Vec3(my_car.physics.location)
        car_velocity = Vec3(my_car.physics.velocity)
        ball_location = Vec3(packet.balls[0].physics.location)
        ball_velocity = Vec3(packet.balls[0].physics.velocity)
        goal_location = Vec3(0, 5120 * (1 - 2 * sit.own_team), 0)

        target_location = ball_location

        if 750 < car_velocity.length() < 800:
            # We'll do a front flip if the car is moving at a certain speed.
            return sit.controller.begin_front_flip(packet)

        sit.controller.set_steer(steer_toward_target(my_car, target_location))
        sit.controller.set_boost(True)
        sit.controller.set_throttle(1.0)

        return sit.controller.controls