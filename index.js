let minutes = 25;
let seconds = 0;
let timer;
let isPaused = true;

let activeTaskIndex = JSON.parse(localStorage.getItem("activeTaskIndex"));

window.onload = function () {
    showActiveTask();
};

function setMode(mode) {
    clearInterval(timer);

    if (mode === "work") {
        minutes = 25;
    } else if (mode === "short") {
        minutes = 5;
    } else {
        minutes = 15;
    }

    seconds = 0;
    isPaused = true;
    updateTimer();

    document.querySelectorAll(".mode-switch button")
        .forEach(btn => btn.classList.remove("active"));

    document.getElementById(mode + "Btn").classList.add("active");
}

function updateTimer() {
    const timerElement = document.getElementById("timer");

    timerElement.textContent =
        String(minutes).padStart(2, '0') + ":" +
        String(seconds).padStart(2, '0');

    if (!isPaused) {
        if (seconds > 0) {
            seconds--;
        } else if (minutes > 0) {
            minutes--;
            seconds = 59;
        } else {
            clearInterval(timer);
            timer = null;

            completeTaskIfExists();
        }
    }
}

function togglePauseResume() {
    isPaused = !isPaused;

    if (!timer) {
        timer = setInterval(updateTimer, 1000);
    }
}

function restartTimer() {
    clearInterval(timer);
    timer = null;
    isPaused = true;
    setMode("work");
}

function completeTaskIfExists() {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    let activeTaskIndex = JSON.parse(localStorage.getItem("activeTaskIndex"));
    let taskStartTime = localStorage.getItem("taskStartTime");

    if (activeTaskIndex !== null && taskStartTime) {
        const timeTaken = Math.floor((Date.now() - taskStartTime) / 1000);

        const minutesSpent = Math.floor(timeTaken / 60);
        const secondsSpent = timeTaken % 60;

        const formattedTime = `${minutesSpent}m ${secondsSpent}s`;

        tasks[activeTaskIndex].completed = true;
        tasks[activeTaskIndex].timeSpent = formattedTime;

        localStorage.setItem("tasks", JSON.stringify(tasks));
        localStorage.removeItem("activeTaskIndex");
        localStorage.removeItem("taskStartTime");

        alert(`🎉 Task complete!\n${tasks[activeTaskIndex].text}\nTime: ${formattedTime}`);
    } else {
        alert("Time's up!");
    }

    showActiveTask();
}

function showActiveTask() {
    const taskDisplay = document.getElementById("currentTask");

    if (!taskDisplay) return;

    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    let activeTaskIndex = JSON.parse(localStorage.getItem("activeTaskIndex"));

    if (activeTaskIndex !== null && tasks[activeTaskIndex]) {
        taskDisplay.textContent = "Working on: " + tasks[activeTaskIndex].text;
    } else {
        taskDisplay.textContent = "No task selected";
    }
}

setMode("work");
