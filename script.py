import time, os, random
import copy
import json
from datetime import datetime

size = 0
arr = []
previous_states = []

def save_pattern(filename=None):
    """Save current board state to a file"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"pattern_{timestamp}.json"
    
    pattern_data = {
        'size': size,
        'pattern': arr,
        'timestamp': datetime.now().isoformat(),
        'description': f"Saved pattern {size}x{size}"
    }
    
    try:
        with open(filename, 'w') as f:
            json.dump(pattern_data, f, indent=2)
        print(f"Pattern saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving pattern: {e}")
        return False

def load_pattern(filename):
    """Load board state from a file"""
    global arr, size
    try:
        with open(filename, 'r') as f:
            pattern_data = json.load(f)
        
        loaded_size = pattern_data['size']
        loaded_pattern = pattern_data['pattern']
        
        if loaded_size != size:
            print(f"Warning: Loaded pattern size ({loaded_size}) differs from current board size ({size})")
            print("Resizing board to match pattern...")
            size = loaded_size
            
        arr = loaded_pattern
        print(f"Pattern loaded from {filename}")
        if 'description' in pattern_data:
            print(f"Description: {pattern_data['description']}")
        return True
    except FileNotFoundError:
        print(f"File {filename} not found")
        return False
    except Exception as e:
        print(f"Error loading pattern: {e}")
        return False

def list_saved_patterns():
    """List all saved pattern files"""
    import glob
    # Look for patterns in current directory and patterns subfolder
    pattern_files = (glob.glob("*.json") + 
                    glob.glob("patterns/*.json") + 
                    glob.glob("pattern_*.json"))
    # Remove duplicates
    pattern_files = list(set(pattern_files))
    
    if pattern_files:
        print("Available patterns:")
        for i, filename in enumerate(pattern_files, 1):
            print(f"{i}. {filename}")
        return pattern_files
    else:
        print("No saved patterns found")
        return []

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
    print("6. Load from file")
    
    choice = input("Enter choice (0-6): ")
    
    if choice == '0':
        # Random initialization
        arr = [[int((lambda y: (y>0.7))(random.random())) for x in range(size)] for x in range(size)]
    elif choice == '6':
        # Load from file
        pattern_files = list_saved_patterns()
        if pattern_files:
            try:
                file_choice = int(input("Enter file number: ")) - 1
                if 0 <= file_choice < len(pattern_files):
                    if not load_pattern(pattern_files[file_choice]):
                        print("Failed to load pattern, using random")
                        arr = [[int((lambda y: (y>0.7))(random.random())) for x in range(size)] for x in range(size)]
                else:
                    print("Invalid choice, using random")
                    arr = [[int((lambda y: (y>0.7))(random.random())) for x in range(size)] for x in range(size)]
            except ValueError:
                print("Invalid input, using random")
                arr = [[int((lambda y: (y>0.7))(random.random())) for x in range(size)] for x in range(size)]
        else:
            print("No saved patterns, using random")
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
    print("Press Ctrl+C to exit and save")
    time.sleep(1)
    
    # Simulate
    try:
        while True:
            os.system('clear')
            print(f"Generation: {generation}")
            print("Press Ctrl+C to exit")
            
            # Check if game is over
            game_over, reason = check_game_over()
            if game_over:
                print(f"\n🎮 GAME OVER: {reason}")
                try:
                    save_choice = input("Save final pattern? (y/n): ")
                    if save_choice.lower() == 'y':
                        filename = input("Enter filename (or press Enter for auto-name): ").strip()
                        if filename:
                            save_pattern(filename if filename.endswith('.json') else filename + '.json')
                        else:
                            save_pattern()
                except (EOFError, KeyboardInterrupt):
                    pass
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
    except KeyboardInterrupt:
        print("\n\nGame interrupted!")
        try:
            save_choice = input("Save current pattern? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input("Enter filename (or press Enter for auto-name): ").strip()
                if filename:
                    save_pattern(filename if filename.endswith('.json') else filename + '.json')
                else:
                    save_pattern()
        except (EOFError, KeyboardInterrupt):
            pass
        print("Thanks for playing!")
