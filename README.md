# RecordHelperForAEC

This is a wrapper for integrating the AEC-based environment of `pettingzoo` with the `gymnasium.experimental.wrappers.RecordVideoV0` from the `gymnasium` library.

`RecordVideoV0` calls the superclass's `step`/`reset` method and attempts to unpack `obs`, `info` in the current class's `step`/`reset` method. However, an error occurs because the AEC-based environment returns None from the step function.

This simple wrapper resolves the issue, allowing for the recording of the environment with `RecordVideoV0` in the AEC setting.

## Sample

```python
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
```