from patient_env import PatientEnv
from stable_baselines3.common.env_checker import check_env


env = PatientEnv(2)

check_env(env)