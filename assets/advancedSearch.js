let gameData = []; // Load your game data from a JSON file or API

// Fetch game data from a JSON file
fetch('/assets/gamedata.json')
    .then(response => response.json())
    .then(data => {
        gameData = data.games;
    })
    .catch(error => console.error('Error loading game data:', error));

function handleAdvancedSearch() {
    const player1 = document.getElementById('player1').value.toLowerCase();
    const player2 = document.getElementById('player2').value.toLowerCase();
    const team1 = document.getElementById('team1').value.toLowerCase();
    const team2 = document.getElementById('team2').value.toLowerCase();
    const season = document.getElementById('season').value;
    const awayGamesOnly = document.querySelector('input[name="awayGamesOnly"]').checked;
    const excludeTeammate = document.getElementById('excludeTeammate').value.toLowerCase();

    const filteredGames = gameData.filter(game => {
        // Filter by season
        if (season !== 'all' && game.season !== season) return false;
        
        // Filter by player
        if (player1 && !game.players[player1]) return false;
        if (player2 && !game.players[player2]) return false;
        
        // Filter by team
        if (team1 && !(game.teams.home.toLowerCase() === team1 || game.teams.away.toLowerCase() === team1)) return false;
        if (team2 && !(game.teams.home.toLowerCase() === team2 || game.teams.away.toLowerCase() === team2)) return false;
        
        // Filter for away games
        if (awayGamesOnly && game.location !== 'away') return false;
        
        // Exclude specific teammates
        if (excludeTeammate && game.players[excludeTeammate]) return false;
        
        return true;
    });

    displayResults(filteredGames);
}

function displayResults(games) {
    const resultsContainer = document.getElementById('resultsContainer');
    resultsContainer.innerHTML = '';

    if (games.length === 0) {
        resultsContainer.innerHTML = '<p>No matching games found.</p>';
        return;
    }

    games.forEach(game => {
        const gameInfo = document.createElement('div');
        gameInfo.innerHTML = `
            <p>
                <strong>${game.date}</strong>: 
                ${game.teams.away} at ${game.teams.home} 
                - <a href="/boxscores/${game.game_id}.html">View Game Details</a>
            </p>`;
        resultsContainer.appendChild(gameInfo);
    });
}
