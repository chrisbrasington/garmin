
```dataviewjs
const data = await dv.io.csv("garmin_sleep.csv");
const rows = data.values;

const chartData = {
    type: 'line',
    data: {
        labels: rows.map(r => r["sleepStartTimestampGMT"]),
        datasets: [
	        {label: 'Deep Sleep', data: rows.map(r => r["deepSleepSeconds"]/3600), backgroundColor: 'navy', borderColor: 'navy', lineTension: 0.4 },
	        {label: 'Light Sleep', data: rows.map(r => r["lightSleepSeconds"]/3600), backgroundColor: 'skyblue', borderColor: 'skyblue', lineTension: 0.4 },
	        {label: 'REM', data: rows.map(r => r["remSleepSeconds"]/3600), backgroundColor: 'indigo', borderColor: 'indigo', lineTension: 0.4 },
	        {label: 'Awake', data: rows.map(r => r["awakeSleepSeconds"]/3600), backgroundColor: 'lavender', borderColor: 'lavender', lineTension: 0.4 },
        ],
    },
}

window.renderChart(chartData, this.container);
```