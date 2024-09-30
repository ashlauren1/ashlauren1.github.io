// Placeholder data for players and teams
const data = [
    { name: "Auston Matthews", url: "/players/matthau01.html" },
    { name: "Sidney Crosby", url: "/players/crosbsi01.html" },
    { name: "Toronto Maple Leafs", url: "/teams/TOR.html" },
    { name: "Arizona Coyotes", url: "/teams/ARI.html" },
    // Add more player and team data here
];

// Function to show suggestions
function showSuggestions(input) {
    const suggestionsBox = document.getElementById('suggestions');
    suggestionsBox.innerHTML = '';  // Clear previous suggestions

    if (input.length === 0) {
        suggestionsBox.style.display = 'none';
        return;
    }

    const filteredData = data.filter(item => item.name.toLowerCase().includes(input.toLowerCase()));

    if (filteredData.length === 0) {
        suggestionsBox.style.display = 'none';
        return;
    }

    filteredData.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item.name;
        li.onclick = () => {
            window.location.href = item.url;
        };
        suggestionsBox.appendChild(li);
    });

    suggestionsBox.style.display = 'block';
}
