def gridworld_policy_evaluation(policy: dict, gamma: float, threshold: float) -> list[list[float]]:
    """
    Evaluate state-value function for a policy on a 5x5 gridworld.
    
    Args:
        policy: dict mapping (row, col) to action probability dicts
        gamma: discount factor
        threshold: convergence threshold
    Returns:
        5x5 list of floats
    """
    # Your code here
    size = 5
    
    # inisialisasi V
    V = [[0.0 for _ in range(size)] for _ in range(size)]
    
    actions = ['up', 'down', 'left', 'right']
    
    def is_terminal(i, j):
        return (i == 0 and j == 0) or \
               (i == 0 and j == size-1) or \
               (i == size-1 and j == 0) or \
               (i == size-1 and j == size-1)
    
    def get_next_state(i, j, action):
        if action == 'up':
            return (max(i-1, 0), j)
        elif action == 'down':
            return (min(i+1, size-1), j)
        elif action == 'left':
            return (i, max(j-1, 0))
        elif action == 'right':
            return (i, min(j+1, size-1))
    
    while True:
        delta = 0
        new_V = [row[:] for row in V]
        
        for i in range(size):
            for j in range(size):
                
                if is_terminal(i, j):
                    continue  # tetap 0
                
                v = 0.0
                
                for action, prob in policy[(i, j)].items():
                    ni, nj = get_next_state(i, j, action)
                    
                    reward = -1
                    v += prob * (reward + gamma * V[ni][nj])
                
                new_V[i][j] = v
                delta = max(delta, abs(v - V[i][j]))
        
        V = new_V
        
        if delta < threshold:
            break
    
    return V