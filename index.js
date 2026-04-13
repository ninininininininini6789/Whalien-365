let minutes = 25;
let seconds = 0;
let timer;
let isPaused = true;

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
            alert("Time's up!");
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

setMode("work");
