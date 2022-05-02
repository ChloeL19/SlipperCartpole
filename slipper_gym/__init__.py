from gym.envs.registration import register

register(
    id='SlipperPacman-v0',
    entry_point='slipper_gym.envs:CartPoleEnv',
)