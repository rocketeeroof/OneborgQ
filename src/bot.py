from typing import override

from rlbot.flat import BallAnchor, ControllerState, GamePacket
from rlbot.managers import Bot
from rlbot_flatbuffers import CarAnchor

from util.ball_prediction_analysis import find_slice_at_time
from util.boost_pad_tracker import BoostPadTracker
from util.drive import steer_toward_target
from util.sequence import ControlStep, Sequence
from util.vec import Vec3

from extra_utils.situation import situation
from extra_utils.strategy import *

class MyBot(Bot):
    active_sequence: Sequence | None = None
    boost_pad_tracker: BoostPadTracker = BoostPadTracker()

    @override
    def initialize(self):
        # Set up information about the boost pads now that the game is active and the info is available
        self.boost_pad_tracker.initialize_boosts(self.field_info)
        self.situation = situation(self.renderer)
        self.strat = default_strategy()

    @override
    def get_output(self, packet: GamePacket) -> ControllerState:
        """
        This function will be called by the framework many times per second. This is where you can
        see the motion of the ball, etc. and return controls to drive your car.
        """

        # Keep our boost pad info updated with which pads are currently active
        self.boost_pad_tracker.update_boost_status(packet)

        if len(packet.balls) == 0:
            # If there are no balls current in the game (likely due to being in a replay), skip this tick.
            return ControllerState()
        # we can now assume there's at least one ball in the match

        self.situation.update(packet, self.field_info, self.ball_prediction, self.index, self.team)

        # This is good to keep at the beginning of get_output. It will allow you to continue
        # any sequences that you may have started during a previous call to get_output.
        if self.situation.controller.active_sequence is not None and not self.situation.controller.active_sequence.done:
            return self.situation.controller.active_sequence.tick(packet)
        self.situation.controller.clear_controls()

        self.strat.run(self.situation)
        # You can set more controls if you want, like controls.boost.
        self.renderer.begin_rendering()
        self.situation.render.render_all()
        self.situation.render.reset()
        self.renderer.end_rendering()

        return self.situation.controller.controls


if __name__ == "__main__":
    # Connect to RLBot and run
    # Having the agent id here allows for easier development,
    # as otherwise the RLBOT_AGENT_ID environment variable must be set.
    MyBot("scumclass/oneborg_q").run()
