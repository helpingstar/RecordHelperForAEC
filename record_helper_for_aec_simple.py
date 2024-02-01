class RecordHelperForAEC:
    def __init__(self, env):
        super().__init__(env)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed, options=options)
        return None, None

    def step(self, action):
        super().step(action)
        return None, None, None, None, None
