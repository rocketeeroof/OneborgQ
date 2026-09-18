
from rlbot.flat import ControllerState

class controller():
    def __init__(self):
        self.controls = ControllerState()
        self.history = []

    def set_controls(self, controls, name = ""):
        '''
        Set the controls and history
        '''
        self.controls = controls
        self.history.append([self.controls, name])

    def set_steer(self, steer, name = "Steer"):
        self.controls.steer = steer
        self.history.append([self.controls, name])

    def set_throttle(self, throttle, name = "Throttle"):
        self.controls.throttle = throttle
        self.history.append([self.controls, name])

    def set_pitch(self, pitch, name = "Pitch"):
        self.controls.pitch = pitch
        self.history.append([self.controls, name])

    def set_yaw(self, yaw, name = "Yaw"):
        self.controls.yaw = yaw
        self.history.append([self.controls, name])

    def set_roll(self, roll, name = "Roll"):
        self.controls.roll = roll
        self.history.append([self.controls, name])

    def set_jump(self, jump, name = "Jump"):
        self.controls.jump = jump
        self.history.append([self.controls, name])

    def set_boost(self, boost, name = "Boost"):
        self.controls.boost = boost
        self.history.append([self.controls, name])

    def set_handbrake(self, handbrake, name = "Handbrake"):
        self.controls.handbrake = handbrake
        self.history.append([self.controls, name])

    def clear_controls(self):
        '''
        Clear the controls
        '''
        self.controls = ControllerState()
        self.history = []