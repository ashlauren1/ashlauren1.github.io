// Global variables to store players and teams data
let playersData = [];
let teamsData = [];

// Fetch players and teams data
async function fetchPlayersData() {
    const response = await fetch('/assets/players.json');
    return await response.json();
}

async function fetchTeamsData() {
    const response = await fetch('/assets/teams.json');
    return await response.json();
}

// Initialize the data by fetching both JSONs
async function initializeSearch() {
    playersData = await fetchPlayersData();
    teamsData = await fetchTeamsData();
}

// Filter through players and teams based on search input
function getSearchSuggestions(query) {
    const lowerCaseQuery = query.toLowerCase();

    // Filter players
    const playerMatches = playersData.filter(player => {
        const playerNameMatches = player.name.toLowerCase().includes(lowerCaseQuery);
        const englishNameMatches = player.english_names.some(name => name.toLowerCase().includes(lowerCaseQuery));
        return playerNameMatches || englishNameMatches;
    });

    // Filter teams
    const teamMatches = teamsData.filter(team => {
        return team.names.some(name => name.toLowerCase().includes(lowerCaseQuery));
    });

    return [...playerMatches, ...teamMatches];
}

// Render search suggestions
function renderSuggestions(suggestions) {
    const suggestionsContainer = document.getElementById('suggestions');
    suggestionsContainer.innerHTML = ''; // Clear previous suggestions

    if (suggestions.length === 0) {
        const noResult = document.createElement('li');
        noResult.textContent = 'No results found';
        suggestionsContainer.appendChild(noResult);
        return;
    }

    // Populate suggestions
    suggestions.forEach(suggestion => {
        const listItem = document.createElement('li');
        listItem.textContent = suggestion.name || suggestion.names[0]; // Player or team name
        listItem.onclick = () => {
            window.location.href = suggestion.url; // Navigate to the page
        };
        suggestionsContainer.appendChild(listItem);
    });
}

// Search entities and show suggestions
function searchEntities() {
    const query = document.getElementById('searchInput').value;

    if (query.length === 0) {
        document.getElementById('suggestions').innerHTML = ''; // Clear suggestions if input is empty
        return;
    }

    const suggestions = getSearchSuggestions(query);
    renderSuggestions(suggestions);
}

// Initialize search data on page load
window.onload = initializeSearch;
