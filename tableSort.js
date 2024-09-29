let sortDirection = {};

// Function to detect if a column is numeric
function isNumericColumn(columnIndex, rows) {
    for (let row of rows) {
        let cellValue = row.cells[columnIndex].innerText.trim();
        if (cellValue && isNaN(cellValue)) {
            return false;  // If any cell is not a number, it's a text column
        }
    }
    return true;  // If all cells are numbers, it's a numeric column
}

// General sort function for any table and column
function sortTable(team_gamelogs, columnIndex) {
    let table = document.getElementById(team_gamelogs);
    let rows = Array.from(table.rows).slice(1);  // Skip the header row
    let dir = sortDirection[team_gamelogs + columnIndex] === "asc" ? "desc" : "asc";  // Track sorting direction

    // Determine if the column is numeric
    let isNumeric = isNumericColumn(columnIndex, rows);

    rows.sort((a, b) => {
        let x = a.cells[columnIndex].innerText.trim();
        let y = b.cells[columnIndex].innerText.trim();

        if (isNumeric) {
            x = parseFloat(x);
            y = parseFloat(y);
        } else {
            x = x.toLowerCase();
            y = y.toLowerCase();
        }

        return dir === "asc" ? (x > y ? 1 : -1) : (x < y ? 1 : -1);
    });

    rows.forEach(row => table.tBodies[0].appendChild(row));

    sortDirection[team_gamelogs + columnIndex] = dir;
}
