const board = [[null, null, null], [null, null, null], [null, null, null]];
const humanPlayer = 'X';
const botPlayer = 'O';
let currentPlayer = humanPlayer;
let gameOver = false;

const cells = document.querySelectorAll('.cell');
const message = document.getElementById('message');
const resetButton = document.getElementById('reset');


for (let cell of cells) {
    cell.addEventListener('click', () => {
        if (gameOver || cell.textContent !== '') {
            return;
        }


        const row = cell.dataset.row;
        const col = cell.dataset.col;
        board[row][col] = currentPlayer;
        cell.textContent = currentPlayer;


        if (checkForWin()) {
            message.textContent = `${currentPlayer} wins!`;
            gameOver = true;
            return;
        } else if (checkForTie()) {
            message.textContent = 'Tie game.';
            gameOver = true;
            return;
        }


        currentPlayer = currentPlayer === humanPlayer ? botPlayer : humanPlayer;


        if (currentPlayer === botPlayer) {
            botMove();
        }
    });
}


resetButton.addEventListener('click', () => {
    for (let cell of cells) {
        cell.textContent = '';
    }
    board.forEach((row, i) => {
        row.forEach((col, j) => {
            board[i][j] = null;
        });
    });
    currentPlayer = humanPlayer;
    gameOver = false;
    message.textContent = '';
});

function checkForWin() {
    for (let row of board) {
        if (row[0] !== null && row[0] === row[1] && row[1] === row[2]) {
            return true;
        }
    }


    for (let col = 0; col < 3; col++) {
        if (board[0][col] !== null && board[0][col] === board[1][col] && board[1][col] === board[2][col]) {
            return true;
        }
    }


    if (board[0][0] !== null && board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
        return true;
    }
    if (board[0][2] !== null && board[0][2] === board[1][1] && board[1][1] === board[2][0]) {
        return true;
    }

    return false;
}

function checkForTie() {
    for (let row of board) {
        if (row.includes(null)) {
            return false;
        }
    }
    return true;
}



function botMove() {
    let emptyCells = [];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[i][j] === null) {
                emptyCells.push([i, j]);
            }
        }
    }
    const [row, col] = emptyCells[Math.floor(Math.random() * emptyCells.length)];

    board[row][col] = currentPlayer;
    cells[row * 3 + col].textContent = currentPlayer;

    if (checkForWin()) {
        message.textContent = `${currentPlayer} wins!`;
        gameOver = true;
        return;
    } else if (checkForTie()) {
        message.textContent = 'Tie game.';
        gameOver = true;
        return;
    }
    currentPlayer = humanPlayer;
}
