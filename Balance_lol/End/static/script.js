document.getElementById('team-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const playersInput = document.getElementById('players').value;
    const players = playersInput.split(',').map(player => player.trim());

    if (players.length !== 10) {
        alert("Please enter exactly 10 player names.");
        return;
    }

    try {
        const response = await fetch('/create-teams', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ players })
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(errorData.error || "An error occurred while generating teams.");
            return;
        }

        const data = await response.json();

        // Display team results
        const teamADiv = document.getElementById('team-a');
        const teamBDiv = document.getElementById('team-b');
        const scoreP = document.getElementById('score');

        teamADiv.innerHTML = `
            <h3>Team A</h3>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Nickname</th>
                        <th>Position</th>
                        <th>Win Rate</th>
                        <th>Rank Score</th>
                    </tr>
                </thead>
                <tbody>
                    ${data.team_a.players.map(player => `
                        <tr>
                            <td>${player.name}</td>
                            <td>${player.nickname}</td>
                            <td>${player.main_position}</td>
                            <td>${player.win_rate}%</td>
                            <td>${player.rank_score}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;

        teamBDiv.innerHTML = `
            <h3>Team B</h3>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Nickname</th>
                        <th>Position</th>
                        <th>Win Rate</th>
                        <th>Rank Score</th>
                    </tr>
                </thead>
                <tbody>
                    ${data.team_b.players.map(player => `
                        <tr>
                            <td>${player.name}</td>
                            <td>${player.nickname}</td>
                            <td>${player.main_position}</td>
                            <td>${player.win_rate}%</td>
                            <td>${player.rank_score}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;

        scoreP.innerText = `Total Score: Team A ${data.team_a.total_score} vs Team B ${data.team_b.total_score}`;
        scoreP.style.color = data.team_a.total_score > data.team_b.total_score ? 'green' : 'red';

        document.getElementById('results').classList.remove('hidden');
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
    }
});
