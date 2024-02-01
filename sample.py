from pettingzoo.classic import connect_four_v3
from gymnasium.experimental.wrappers import RecordVideoV0
from record_helper_for_aec import RecordHelperForAEC

env = connect_four_v3.env(render_mode="rgb_array")
######################### reder_mode must be 'rgb_array'###
env = RecordHelperForAEC(env)
env = RecordVideoV0(env, video_folder=".")
###########################################################
env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        mask = observation["action_mask"]
        # this is where you would insert your policy
        action = env.action_space(agent).sample(mask)

    env.step(action)
env.close()
