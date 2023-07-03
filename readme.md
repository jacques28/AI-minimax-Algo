## Project4 Tic-tac-toe with minimax algorithm

This project is a Artificial intelligence project that use the minimax algorithm to make the computer play the best move against the human player

## Installation

To used this project you need to install or import the following packages:
    
    ```python```
    ```random```
    ```math```
    ```time```
   
### Usage

To run the program, run the following command in the terminal:

    ```python tictactoe.py```
    ```X is the computer and O is the human player```

### Functions

The ``print_board`` function prints the board in a 3x3 matrix format

The ``minimax`` function is the minimax algorithm that is used to make the computer play the best move against the human player by calculating the best score for each move and return the best move for the computer to play against the human player

The ``play`` function is the main function that is used to play the game and call the other functions to make the computer play the best move against the human player


### Testing

| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
X makes a move to square 0
| X |   |   |
|   |   |   |
|   |   |   |

O Enter your moves between (0-8): 4
O makes a move to square 4
| X |   |   |
|   | O |   |
|   |   |   |

X makes a move to square 1
| X | X |   |
|   | O |   |
|   |   |   |

O Enter your moves between (0-8): 2
O makes a move to square 2
| X | X | O |
|   | O |   |
|   |   |   |

X makes a move to square 6
| X | X | O |
|   | O |   |
| X |   |   |

O Enter your moves between (0-8): 3
O makes a move to square 3
| X | X | O |
| O | O |   |
| X |   |   |

X makes a move to square 5
| X | X | O |
| O | O | X |
| X |   |   |

O Enter your moves between (0-8): 7
O makes a move to square 7
| X | X | O |
| O | O | X |
| X | O |   |

X makes a move to square 8
| X | X | O |
| O | O | X |
| X | O | X |

No winner!