#searchResults {
    position: absolute;
    background-color: white;
    border: 1px solid #ccc;
    width: 100%;
    max-height: 200px;
    overflow-y: auto;
    z-index: 1000;
}

#searchResults div {
    padding: 10px;
    cursor: pointer;
}

#searchResults div:hover, .highlighted {
    background-color: #f1f1f1;
}

#searchResults a {
    text-decoration: none;
    color: black;
    display: block;
}


let players = [];
let teams = [];
let selectedIndex = -1; // For keeping track of selected suggestion

// Fetch players and teams data
fetch('/assets/players.json')
    .then(response => response.json())
    .then(data => {
        players = data;
    })
    .catch(error => console.error('Error loading players data:', error));

fetch('/assets/teams.json')
    .then(response => response.json())
    .then(data => {
        teams = data;
    })
    .catch(error => console.error('Error loading teams data:', error));

// Handle key navigation and suggestions
document.getElementById('searchBar').addEventListener('keydown', function(event) {
    const resultsContainer = document.getElementById('searchResults');
    const suggestions = resultsContainer.querySelectorAll('div');

    if (suggestions.length === 0) return;  // Add this line to avoid errors if there are no suggestions

    if (event.key === 'ArrowDown') {
        selectedIndex = (selectedIndex + 1) % suggestions.length;
        highlightSuggestion(suggestions);
    } else if (event.key === 'ArrowUp') {
        selectedIndex = (selectedIndex - 1 + suggestions.length) % suggestions.length;
        highlightSuggestion(suggestions);
    } else if (event.key === 'Enter') {
        if (selectedIndex >= 0 && suggestions[selectedIndex]) {
            window.location.href = suggestions[selectedIndex].querySelector('a').href;
        } else {
            handleSearch();  // Perform full search if no suggestion selected
        }
        event.preventDefault();  // Prevent form submission
    }
});

function highlightSuggestion(suggestions) {
    suggestions.forEach((suggestion, index) => {
        suggestion.classList.toggle('highlighted', index === selectedIndex);
    });
}

function performSearch() {
    const input = document.getElementById('searchBar').value.toLowerCase();
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = ''; // Clear previous results
    selectedIndex = -1; // Reset selected suggestion index

    if (input.length === 0) {
        return; // Do nothing if input is empty
    }

    // Filter players and teams based on input
    const filteredPlayers = players.filter(player => 
        player.name.toLowerCase().startsWith(input) || player.eng_name.toLowerCase().startsWith(input)
    );

    const filteredTeams = teams.filter(team => 
        team.name.toLowerCase().startsWith(input) || team.aliases.some(alias => alias.toLowerCase().startsWith(input))
    );

    // Display suggestions for players
    filteredPlayers.forEach(player => {
        const resultItem = document.createElement('div');
        resultItem.innerHTML = `<a href="${player.url}">${player.name}</a>`;
        resultItem.addEventListener('click', () => window.location.href = player.url);
        resultsContainer.appendChild(resultItem);
    });

    // Display suggestions for teams
    filteredTeams.forEach(team => {
        const resultItem = document.createElement('div');
        resultItem.innerHTML = `<a href="${team.url}">${team.name}</a>`;
        resultItem.addEventListener('click', () => window.location.href = team.url);
        resultsContainer.appendChild(resultItem);
    });

    resultsContainer.style.display = 'block';
}

function handleSearch() {
    const input = document.getElementById('searchBar').value.toLowerCase();
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = ''; // Clear previous results

    // Filter players and teams
    const filteredPlayers = players.filter(player => 
        player.name.toLowerCase().includes(input) || player.eng_name.toLowerCase().includes(input)
    );

    const filteredTeams = teams.filter(team => 
        team.name.toLowerCase().includes(input) || team.aliases.some(alias => alias.toLowerCase().includes(input))
    );

    // Display all results on a new search results page
    let resultsHTML = '';
    filteredPlayers.forEach(player => {
        resultsHTML += `<div><a href="${player.url}">${player.name}</a></div>`;
    });

    filteredTeams.forEach(team => {
        resultsHTML += `<div><a href="${team.url}">${team.name}</a></div>`;
    });

    // Redirect or display the results somewhere on the page
    window.location.href = `/search-results?q=${input}`;  // Example redirect to a results page

    // Alternatively, you can append these results to a container on the same page:
    // document.getElementById('searchResultsContainer').innerHTML = resultsHTML;
}

document.addEventListener('click', function(event) {
    const searchBar = document.getElementById('searchBar');
    const resultsContainer = document.getElementById('searchResults');

    // Hide search results if clicked outside of the search bar or results
    if (!searchBar.contains(event.target) && !resultsContainer.contains(event.target)) {
        resultsContainer.style.display = 'none';
    }
});
