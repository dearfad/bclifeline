from gym import Env, spaces
import math


class PatientEnv(Env):

    metadata = {"render_modes": "human"}

    def __init__(self, features):
        self.observation_space = spaces.Discrete(features)
        self.action_space = spaces.Discrete(2)
        self._action_dict = {
            0: 'Dead',
            1: 'Alive',
        }

    def reset(self, seed=None):
        return 0

    def step(self, action):
        self.action = action
        self.observation = self._get_observation()
        self.reward = self._get_reward()
        self.done = self._get_done()
        self.info = self._get_info()
        return self.observation, self.reward, self.done, self.info

    def render(self, mode="human", patient=None, ob_age=None):
        self.patient = patient
        self.ob_age = ob_age
        self.start_age = self.patient["age"]
        self.live_year = self.patient["year"]
        self.stop_age = self.patient["age"] + math.floor(self.live_year)
        self.vital = patient["vital"]
        print(
            f"ob_age={self.ob_age}, patient info: start_age={self.start_age}, ", end="")
        print(
            f"live_year={self.live_year}, stop_age={self.stop_age}, vital={self.vital}")
        # time.sleep(1)

    def close(self):
        pass

    def _get_observation(self):
        if self.vital == "Alive":
            if self.ob_age == self.stop_age:
                return "Unknown"
            else:
                return "Alive"
        if self.vital == "Dead":
            if self.ob_age == self.stop_age:
                return "Dead"
            else:
                return "Alive"

    def _get_reward(self):
        if self.observation == "Unknown":
            return 0
        if self.observation == self.action:
            return 1
        else:
            return -1

    def _get_done(self):
        if self.ob_age == self.stop_age:
            return True
        else:
            return False
    
    def _get_info(self):
        return {'info': '...'}


if __name__ == "__main__":
    env = PatientEnv(2)
    print(env.observation_space)
    print(env.action_space)
    print(env._action_dict)
