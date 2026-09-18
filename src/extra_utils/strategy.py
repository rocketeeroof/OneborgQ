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

        if car_location.dist(ball_location) > 1500:
            # We're far away from the ball, let's try to lead it a little bit
            # self.ball_prediction can predict bounces, etc
            ball_in_future = find_slice_at_time(
                sit.ball_prediction, packet.match_info.seconds_elapsed + 5
            )

            # ball_in_future might be None if we don't have an adequate ball prediction right now, like during
            # replays, so check it to avoid errors.
            if ball_in_future is not None:
                target_location = Vec3(ball_in_future.physics.location)

                # BallAnchor(0) will dynamically start the point at the ball's current location
                # 0 makes it reference the ball at index 0 in the packet.balls list
                sit.render.add_line(BallAnchor(0), target_location, sit.render.renderer.cyan)

        # Draw some things to help understand what the bot is thinking
        sit.render.add_line(CarAnchor(sit.own_index), target_location, sit.render.renderer.white)
        
        sit.render.add_string(
            f"Speed: {car_velocity.length():.1f}",
            CarAnchor(sit.own_index),
            1,
            sit.render.renderer.white,
        )
        sit.render.add_line(
            target_location - Vec3(0, 0, 50),
            target_location + Vec3(0, 0, 50),
            sit.render.renderer.cyan,
        )

        if 750 < car_velocity.length() < 800:
            # We'll do a front flip if the car is moving at a certain speed.
            sit.controller.begin_front_flip(packet)
            return sit.controller.active_sequence

        sit.controller.set_steer(steer_toward_target(my_car, target_location))
        sit.controller.set_boost(True)
        sit.controller.set_throttle(1.0)

        return sit.controller.controls