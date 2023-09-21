def test_policy(env, action, random=0):
    if random == 0:

        # Try the new policy to compute the number of times the agent
        # reaches the goal within a fixed number of steps in each episode

        # Set variable goal to 0
        goal = 0

        # Loop pver the number of episodes
        for i in range(100):

            # Reset the environment, this will return the initial state
            c = env.reset()[0]

            # Loop over the maximum number of steps in each episode
            for t in range(10000):

                # Use the step method using the action sequence got from the toptimal policy
                c, reward, done, truncated, info = env.step(action[c])

                # If the reward returned by the environment is 1, then the goal is reached
                if done:
                    if reward == 1:
                        goal += 1
                    break

        print(" Agent succeeded to reach goal {} out of 100 episodes using the optimal policy ".format(goal))


    else:

        # Try the result with a random policy

        # Set variable goal to 0
        goal = 0

        # Loop pver the number of episodes
        for i in range(100):

            # Reset the environment, this will return the initial state
            c = env.reset()

            # Loop over the maximum number of steps in each episode
            for t in range(10000):

                # Use the step method using the action sequence got from the toptimal policy
                try:
                    c, reward, done, truncated, info = env.step(env.action_space.sample())
                    # env.step: Run one timestep of the environment’s dynamics using the agent actions.
                    # c: An element of the environment’s observation_space as the next observation due to the agent actions. 
                except:
                    c, reward, done, truncated, info = env.step(0)

                # If the reward returned by the environment is 1, then the goal is reached
                if done:
                    if reward == 1:
                        goal += 1
                    break

        print(" Agent succeeded to reach goal {} out of 100 episodes using a random policy ".format(goal))
    env.close()
