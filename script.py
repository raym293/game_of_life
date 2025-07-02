import time, os, random
import copy

size = 0
arr = []
previous_states = []

def get_preset_patterns():
    """Return dictionary of preset patterns"""
    patterns = {
        '1': {
            'name': 'Glider',
            'pattern': [
                [0, 1, 0],
                [0, 0, 1],
                [1, 1, 1]
            ]
        },
        '2': {
            'name': 'Blinker (Oscillator)',
            'pattern': [
                [1, 1, 1]
            ]
        },
        '3': {
            'name': 'Block (Static)',
            'pattern': [
                [1, 1],
                [1, 1]
            ]
        },
        '4': {
            'name': 'Toad (Oscillator)',
            'pattern': [
                [0, 1, 1, 1],
                [1, 1, 1, 0]
            ]
        },
        '5': {
            'name': 'Beacon (Oscillator)',
            'pattern': [
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]
            ]
        }
    }
    return patterns

def place_pattern(pattern, start_row, start_col):
    """Place a pattern on the board at specified position"""
    global arr
    for i, row in enumerate(pattern):
        for j, cell in enumerate(row):
            if start_row + i < size and start_col + j < size:
                arr[start_row + i][start_col + j] = cell

def alive(i:int,j:int):
    # Use modulo for wrapping boundaries (toroidal grid)
    wrapped_i = i % size
    wrapped_j = j % size
    return arr[wrapped_i][wrapped_j]

def is_board_empty():
    """Check if all cells are dead"""
    for row in arr:
        for cell in row:
            if cell:
                return False
    return True

def check_game_over():
    """Check if game is over due to static or oscillating patterns"""
    global previous_states
    
    # Check if board is empty
    if is_board_empty():
        return True, "All cells are dead"
    
    # Create a copy of current state
    current_state = copy.deepcopy(arr)
    
    # Check against previous states for static/oscillating patterns
    for i, prev_state in enumerate(previous_states):
        if current_state == prev_state:
            if i == 0:
                return True, "Static pattern detected"
            else:
                return True, f"Oscillating pattern detected (period {i+1})"
    
    # Store current state (keep only last 10 states to detect patterns)
    previous_states.insert(0, current_state)
    if len(previous_states) > 10:
        previous_states.pop()
    
    return False, ""

def play():
    global arr
    # Create a copy of the current state to avoid modifying while reading
    new_arr = [[0 for x in range(size)] for x in range(size)]
    
    for i in range(size):
        for j in range(size):
            count = 0
            count += alive(i-1,j-1)
            count += alive(i,j-1)
            count += alive(i+1,j-1)
            count += alive(i+1,j)
            count += alive(i+1,j+1)
            count += alive(i,j+1)
            count += alive(i-1,j+1)
            count += alive(i-1,j)
            
            # Apply Conway's rules
            if arr[i][j] == 1:  # Currently alive
                if count == 2 or count == 3:
                    new_arr[i][j] = 1  # Stays alive
                else:
                    new_arr[i][j] = 0  # Dies
            else:  # Currently dead
                if count == 3:
                    new_arr[i][j] = 1  # Becomes alive
                else:
                    new_arr[i][j] = 0  # Stays dead
    
    # Update the global array
    arr = new_arr
if __name__ == '__main__':
    # Setup
    size = int(input("Size of board:\n"))
    
    # Initialize empty board
    arr = [[0 for x in range(size)] for x in range(size)]
    
    # Pattern selection
    print("\nChoose starting pattern:")
    print("0. Random")
    patterns = get_preset_patterns()
    for key, pattern_info in patterns.items():
        print(f"{key}. {pattern_info['name']}")
    
    choice = input("Enter choice (0-5): ")
    
    if choice == '0':
        # Random initialization
        arr = [[int((lambda y: (y>0.7))(random.random())) for x in range(size)] for x in range(size)]
    elif choice in patterns:
        # Place selected pattern in center of board
        pattern = patterns[choice]['pattern']
        start_row = (size - len(pattern)) // 2
        start_col = (size - len(pattern[0])) // 2
        place_pattern(pattern, start_row, start_col)
        print(f"Placed {patterns[choice]['name']} pattern")
    else:
        print("Invalid choice, using random pattern")
        arr = [[int((lambda y: (y>0.7))(random.random())) for x in range(size)] for x in range(size)]

    generation = 0
    
    print("\nStarting simulation...")
    print("Press Ctrl+C to exit")
    time.sleep(1)
    
    # Simulate
    while True:
        os.system('clear')
        print(f"Generation: {generation}")
        
        # Check if game is over
        game_over, reason = check_game_over()
        if game_over:
            print(f"\n🎮 GAME OVER: {reason}")
            print("Press Ctrl+C to exit")
            # Display final state
            for i in arr:
                for j in i:
                    print("\033[35m█\033[0m" if j==1 else " ", end="")
                    print("\033[35m█\033[0m" if j==1 else " ", end="")
                print()
            # Wait for user to exit
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                break
        
        play()
        for i in arr:
            for j in i:
                print("\033[35m█\033[0m" if j==1 else " ", end="")
                print("\033[35m█\033[0m" if j==1 else " ", end="")
            print()
        
        generation += 1
        time.sleep(0.1)
