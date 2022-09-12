import metadrive
import gym
import multiprocessing as mp
from multiprocessing import Process, Pipe

def build_env(env_name):
    print(">>> build_env starting...")
    env_config = dict(use_render=False)
    env = gym.make(env_name, config=env_config)
    print(">>> build_env ending...")
    return env

def build_env_asyn(env_name, conn):
    print(">>> build_env_asyn starting...")
    env_config = dict(use_render=False)
    env = gym.make(env_name, config=env_config)
    print(f'in build_env_asyn {id(env)}')
    conn.send(env)
    print(">>> build_env_asyn ending...")

class Evaluator():
    def __init__(self) -> None:
        self.n = 42

    def foo(self):
        print("hello")

def build_evaluator(conn):
    env_name = "MetaDrive-10env-v0"
    env = build_env(env_name)

    while True:
        rec = conn.recv()
        print(rec)
        if rec == "reset":
            print(">>> reset")
            print(len(env.reset()))

        if rec == "stop":
            print(">>> exiting")
            break


def main():
    # env_name = "MetaDrive-validation-v0"

    env_name = "MetaDrive-10env-v0"

    conn11, conn12 = Pipe()
    # conn21, conn22 = Pipe()
    env = build_env(env_name)
    # env2 = None
    # env2 = 
    process = [
        # mp.Process(target=build_env_asyn, args=(env_name, conn12, )),
        # mp.Process(target=build_env_asyn, args=(env_name, conn22, )),

        mp.Process(target=build_evaluator, args=(conn12, )),
    ]

    [p.start() for p in process]  # 开启了两个进程
    conn11.send("reset")
    conn11.send("reset")

    print(">>> in main")
    print(len(env.reset()))

    conn11.send("stop")
    # env2 = conn21.recv()
    # print(id(env2))

    # print(len(env1.reset()))
    # print(len(env2.reset()))

    [p.join() for p in process]   # 等待两个进程依次结束



if __name__ == "__main__":
    main()
