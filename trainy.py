from agent import Agent
from game import Snake

agent = Agent()
game = Snake()

while True:
    state_old = agent.get_state(game)
    action = agent.act(state_old)
    state_new = agent.get_state(game)

    # === SYSTEM NAGRÓD ===
    reward = 0
    old_dist = abs(game.snake_x - game.food_x) + abs(game.snake_y - game.food_y)
    game.run(action)
    new_dist = abs(game.snake_x - game.food_x) + abs(game.snake_y - game.food_y)

    if new_dist < old_dist:
        reward += 0.2
    if (game.snake_x == game.food_x) and (game.snake_y == game.food_y):
        reward += 1
    if not game.game_status:
        reward -= 2
    else:
        reward -= 0.2

    # print(f"Snake x: {game.snake_x} Snake y: {game.snake_y}")
    # print(f"Food x: {game.food_x} Snake y: {game.food_y}")
    print(reward)
    done = not game.game_status

    agent.remember(state_old, action, reward, state_new, done)
    agent.train_short_memory(state_old, action, reward, state_new, done)

    if done:
        agent.train_long_memory()
        agent.n_games += 1
