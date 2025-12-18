const ctx = document.getElementById('lossChart').getContext('2d');

const chartData = {
    labels: [],
    datasets: []
};

// Initialize Chart.js
const metricChart = new Chart(ctx, {
    type: 'line',
    data: chartData,
    options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        scales: {
            x: { 
                title: { display: false },
                ticks: { display: false },
            },
            y: { 
                title: { display: false }
             }
        }
    },
});

const datasetsMap = {};
let currentMetric = null;

// WebSocket connection
const ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    for (const [key, values] of Object.entries(data)) {
        if (!datasetsMap[key]) {
            const color = `hsl(${Math.random()*360}, 70%, 50%)`;
            const dataset = { label: key, data: [...values], borderColor: color, tension: 0.1, fill: false };
            datasetsMap[key] = dataset;

            const btn = document.createElement("button");
            btn.textContent = key;
            btn.onclick = () => switchMetric(key);
            buttonsContainer.appendChild(btn);

            if (!currentMetric) switchMetric(key);
        } else {
            datasetsMap[key].data = [...values];
        }
    }

    const maxLen = Math.max(...Object.values(datasetsMap).map(ds => ds.data.length));
    chartData.labels = Array.from({length: maxLen}, (_, i) => i+1);

    metricChart.update();
};


function switchMetric(metricName) {
    currentMetric = metricName;
    chartData.datasets = [datasetsMap[metricName]];
    metricChart.update();

    const buttons = buttonsContainer.querySelectorAll("button");
    buttons.forEach(btn => {
        if (btn.textContent === metricName) {
            btn.classList.add("active");
        } else {
            btn.classList.remove("active");
        }
    });
}



// Fullscreen button functionality
const btn = document.getElementById("fullscreenBtn");
const canvas = document.getElementById("lossChart");

btn.addEventListener("click", () => {
    if (canvas.requestFullscreen) {
        canvas.requestFullscreen();
    } else if (canvas.webkitRequestFullscreen) {
        canvas.webkitRequestFullscreen();
    } else if (canvas.msRequestFullscreen) {
        canvas.msRequestFullscreen();
    }
});

document.addEventListener('fullscreenchange', () => {
    lossChart.resize();
});


const buttonsContainer = document.getElementById("buttonsContainer");