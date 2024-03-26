# Heart Rate
```dataviewjs
const data = await dv.io.csv("daily.csv");
const rows = data.values;

const chartData = {
    type: 'line',
    data: {
        labels: rows.map(r => r["calendarDate"]),
        datasets: [
	        {label: 'minAvgHeartRate', data: rows.map(r => r["minAvgHeartRate"]), backgroundColor: 'teal', borderColor: 'teal', lineTension: 0.4 },
	        {label: 'maxAvgHeartRate', data: rows.map(r => r["maxAvgHeartRate"]), backgroundColor: 'teal', borderColor: 'teal', lineTension: 0.4 }
        ],
    },
}

window.renderChart(chartData, this.container);
```
# Stress
```dataviewjs
const data = await dv.io.csv("daily.csv");
const rows = data.values;

const chartData = {
    type: 'line',
    data: {
        labels: rows.map(r => r["calendarDate"]),
        datasets: [
			{label: 'Stress Average', 
             data: rows.map(r => {
                 const stressLevel = r["STRESS_TOTAL_averageStressLevel"];
                 return stressLevel !== 0 ? stressLevel : null;
             }), 
             backgroundColor: 'orange', 
             borderColor: 'orange', 
             lineTension: 0.4 
            }
        ],
    },
}

window.renderChart(chartData, this.container);
```

# Awake
```dataviewjs
const data = await dv.io.csv("daily.csv");
const rows = data.values;

const chartData = {
    type: 'line',
    data: {
        labels: rows.map(r => r["calendarDate"]),
        datasets: [
            {label: 'Stress Average Awake', 
             data: rows.map(r => {
                 const stressLevel = r["STRESS_AWAKE_averageStressLevel"];
                 return stressLevel !== 0 ? stressLevel : null;
             }), 
             backgroundColor: 'teal', 
             borderColor: 'teal', 
             lineTension: 0.4 
            }
        ],
    },
}

window.renderChart(chartData, this.container);
```
# Asleep
```dataviewjs
const data = await dv.io.csv("daily.csv");
const rows = data.values;

const chartData = {
    type: 'line',
    data: {
        labels: rows.map(r => r["calendarDate"]),
        datasets: [
            {label: 'Stress Average Asleep', 
             data: rows.map(r => {
                 const stressLevel = r["STRESS_ASLEEP_averageStressLevel"];
                 return stressLevel !== 0 ? stressLevel : null;
             }), 
             backgroundColor: 'green', 
             borderColor: 'green', 
             lineTension: 0.4 
            }
        ],
    },
}

window.renderChart(chartData, this.container);
```
# Steps

```dataviewjs
const data = await dv.io.csv("daily.csv");
const rows = data.values;

const chartData = {
    type: 'line',
    data: {
        labels: rows.map(r => r["calendarDate"]),
        datasets: [
	        {label: 'Steps', data: rows.map(r => r["totalSteps"]), backgroundColor: 'teal', borderColor: 'teal', lineTension: 0.4 }
        ],
    },
}

window.renderChart(chartData, this.container);
```