/**
 * Author: Lisa Aiken, 2014
 * This Tic Tac Toe game allows the Human player to choose
 * to play against a Novice, Intermediate, or Expert
 * Computer Player.
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BOARD_SIZE 9
#define DIMENSION 3
#define FALSE 0
#define TRUE 1
#define X_WINS 1
#define O_WINS -1
#define DRAW 0
#define NOVICE 0
#define INTERMEDIATE 1
#define EXPERT 2

/* Draws a Tic Tac Toe board based on the BOARD_SIZE and DIMENSION */
void printBoard(char *boardPtr)
{
    int i = 0;
    int j = 0;
    char mark;

    for (i = 0; i < DIMENSION; i++)
    {
        for (j = 0; j < DIMENSION; j++)
        {
            mark = boardPtr[i * DIMENSION + j];
            if (mark != '0')
            {
                printf(" %c ", mark);
            }
            else
            {
                printf(" %d ", i * DIMENSION + j);
            }

            if (j != DIMENSION - 1)
            {
                printf(" | ");
            }
        }

        printf("\n");
        if (i != DIMENSION - 1)
        {
            printf("-----------------");
        }
        printf("\n");
    }
}

/* checkForWin will either return which player won or false */
int checkForWin(const char *boardPtr)
{
    int i = 0;
    int solutions[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 3, 6, 1, 4, 7, 2, 5, 8, 0, 4, 8, 2, 4, 6};
    int numEntries = 24;

    for (i = 0; i < numEntries; i += 3)
    {
        if (boardPtr[solutions[i]] == 'X' && boardPtr[solutions[i + 1]] == 'X' && boardPtr[solutions[i + 2]] == 'X')
        {
            return X_WINS;
        }
        else if (boardPtr[solutions[i]] == 'O' && boardPtr[solutions[i + 1]] == 'O' && boardPtr[solutions[i + 2]] == 'O')
        {
            return O_WINS;
        }
    }

    return FALSE;
}

/* checkForDraw returns TRUE or FALSE if the final state of the board is a draw */
int checkForDraw(const char *boardPtr)
{
    int i = 0;
    for (i = 0; i < BOARD_SIZE; i++)
    {
        if (boardPtr[i] == '0')
        {
            return FALSE;
        }
    }

    return TRUE;
}

/* analyzeBoard returns the heuristic score for the final state of the board */
int analyzeBoard(const char *boardPtr)
{

    int winner = checkForWin(boardPtr);

    if (winner != FALSE)
    {
        return winner;
    }

    return DRAW;
}

/* gameOver will either return TRUE or FALSE */
int gameOver(const char *boardPtr)
{

    int winner = checkForWin(boardPtr);
    int draw = FALSE;
    if (winner == FALSE)
    {

        /**
         * There isn't a winner so it must be a draw.
         * Returns FALSE if it's not a draw and TRUE if it is. */
        draw = checkForDraw(boardPtr);

        return draw;
    }

    /* There is a winner */
    return TRUE;
}

int miniMax(char player, char *boardPtr)
{

    char localBoard[BOARD_SIZE];
    char availableMoves[BOARD_SIZE];
    int numAvailableMoves = 0;
    int i = 0;
    int j = 0;
    int score = 0;
    int endGame = 0;
    int nextAvailableMove = 0;
    int best_value = 0;

    /* Check to see if the game is over */
    endGame = gameOver(boardPtr);

    if (endGame == TRUE)
    {
        int value = analyzeBoard(boardPtr);
        return value;
    }

    /* Make a copy of the board */
    for (i = 0; i < BOARD_SIZE; i++)
    {
        localBoard[i] = boardPtr[i];
        if (boardPtr[i] == '0')
        {
            /* Populate the array of available moves */
            availableMoves[j] = i;
            j++;
            numAvailableMoves++;
        }
    }

    if (player == 'X')
    {
        /* Max player */
        best_value = -2;

        for (i = 0; i < numAvailableMoves; i++)
        {
            /* Get the next available move and place player's mark */
            nextAvailableMove = availableMoves[i];

            localBoard[nextAvailableMove] = 'X';
            score = miniMax('O', localBoard);

            localBoard[nextAvailableMove] = '0';

            if (score > best_value)
            {
                best_value = score;
            }
        }

        return best_value;
    }
    else
    {
        /* Min player */
        best_value = 2;

        for (i = 0; i < numAvailableMoves; i++)
        {
            /* Get the next available move and place player's mark */
            nextAvailableMove = availableMoves[i];

            localBoard[nextAvailableMove] = 'O';
            score = miniMax('X', localBoard);

            localBoard[nextAvailableMove] = '0';
            if (score < best_value)
            {
                best_value = score;
            }
        }

        return best_value;
    }
}

/* Randomly selects a move from the available moves. */
void computerMoveNovice(char *boardPtr)
{
    /* Get the available moves */
    int i = 0;
    int numMoves = 0;
    int randonMove = -1;
    int availableMoves[BOARD_SIZE];

    for (i = 0; i < BOARD_SIZE; i++)
    {
        if (boardPtr[i] == '0')
        {
            availableMoves[numMoves] = i;
            numMoves++;
        }
    }

    randonMove = random() % numMoves;

    boardPtr[availableMoves[randonMove]] = 'O';
}

void computerMoveIntermediate(char *boardPtr)
{
    int bestMoves[BOARD_SIZE] = {4, 0, 2, 6, 8, 3, 5, 1, 7};
    int i = 0;

    for (i = 0; i < BOARD_SIZE; i++)
    {
        if (boardPtr[bestMoves[i]] == '0')
        {
            boardPtr[bestMoves[i]] = 'O';
            break;
        }
    }
}

/* Uses the MiniMax algorithm to choose the best move. */
void computerMoveExpert(char *boardPtr)
{
    int i = 0;
    int best_choice = -1;
    int score = -2;
    int expectedResult = -2;
    char player = 'O';
    char other_player = 'X';

    /* Get the available moves */
    for (i = 0; i < BOARD_SIZE; i++)
    {
        if (boardPtr[i] == '0')
        {
            boardPtr[i] = player;
            score = -miniMax(other_player, boardPtr);

            boardPtr[i] = '0';
            if (score > expectedResult)
            {
                best_choice = i;
                expectedResult = score;
            }
        }
    }

    boardPtr[best_choice] = player;
}

void computerMove(int level, char *boardPtr)
{

    if (level == NOVICE)
    {
        computerMoveNovice(boardPtr);
    }
    else if (level == INTERMEDIATE)
    {
        computerMoveIntermediate(boardPtr);
    }
    else if (level == EXPERT)
    {
        computerMoveExpert(boardPtr);
    }
}

int main(void)
{

    int position = -1;
    char player = 'X'; /* First player of the game */
    int endGame = 0;
    char board[BOARD_SIZE] = {'0', '0', '0', '0', '0', '0', '0', '0', '0'};
    int computer_level = -1; /* 0 - Novice, 1 - Intermediate, 2 - Expert */
    srandom(time(NULL));

    printf("Computer: (O), You (X) \n");

    while (computer_level < 0 || computer_level > 2)
    {
        printf("What level do you want to play the computer? 0 - Novice, 1 - Intermediate, 2 - Expert\n");
        scanf("%d", &computer_level);

        if (computer_level == NOVICE)
        {
            printf("You selected to play the novice computer.\n");
        }
        else if (computer_level == INTERMEDIATE)
        {
            printf("You selected to play the intermediate computer.\n");
        }
        else if (computer_level == EXPERT)
        {
            printf("You selected to play the expert computer level.  Good luck!\n");
        }
        else
        {
            printf("Please select the appropriate computer level to play against.\n");
        }
    }

    printf("You go first.\n\n");
    printBoard(board);

    while (endGame == FALSE)
    {
        if (player == 'X')
        {
            do
            {
                printf("Where do you want to place your X? (0 - 8)\n");
                scanf("%d", &position);
                printf("%d\n", position);

                if (position < 0 || position > 8 || board[position] != '0')
                {
                    printf("That is not a valid move.  Please try again.\n");
                }
                else
                {
                    board[position] = 'X';
                    player = 'O';
                }

            } while (position < 0 || position > 8);
        }
        else
        {
            computerMove(computer_level, board);
            player = 'X';
        }

        printBoard(board);

        endGame = gameOver(board);
    }

    endGame = analyzeBoard(board);

    if (endGame == X_WINS)
    {
        printf("Player X wins!\n");
    }
    else if (endGame == O_WINS)
    {
        printf("Player O wins!\n");
    }
    else
    {
        printf("It's a draw!");
    }

    return EXIT_SUCCESS;
}