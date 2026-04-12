const workTime = 30*1000;
const restTime = 10*1000;
let currentTime = workTime;
let numberOfWorkIntervals = 2;
let currentMode = "Work";

const dataPercent = document.querySelectorAll('.data-Percent')[0];
const timer = document.getElementById('timer');
const modeEl = document.getElementById('mode');

let countdownInterval;
updateCountdown(currentTime)
countdown(currentTime);

function countdown(pTime){
    countdownInterval = setInterval(() => {
        pTime = pTime - 1000;
        if (pTime <= 0 )
        {
            clearInterval(countdownInterval)
            if (numberOfWorkIntervals > 0) {
                switchMode();
            }
        } else {
            //update countdown
            updateCountdown(pTime)

        }
    }, 1000)
}

function updateCountdown(pTime) {
    if(pTime <= 0 && numberOfWorkIntervals == 0){
        //turn red, reset angle
        dataPercent.style.setProperty('--angle','360deg');
        dataPercent.style.setProperty('--colour','red');
        timer.innerText = `00:00`;
        modeEl.innerText = `END: 0`;
    } else {
        //calculate angle
        let angle = pTime / currentTime * 360 + 'deg';
        if (pTime == 0) {
            angle = '360deg';
        }
        let colour = currentMode == "Work" ? 'blue' : 'red'
        dataPercent.style.setProperty('--angle', angle);
        dataPercent.style.setProperty('--color', color);

    //minutes & seconds
    let minutes = Math.floor(pTime/60/1000).toString().padStart(2,"0");
    let seconds = Math.floor((pTime/1000) % 60).toString().padStart(2, "0");
    timer.innerText = `${minutes}:${seconds}`;
    modeEl.innerText = `${currentMode} ; ${numberOfWorkIntervals}`;
    }
} 

function switchMode() {
    currentMode = currentMode == "Work" ? "Rest" : "Work"
    numberOfWorkIntervals = currentMode == "Work" ? numberOfWorkIntervals - 1 : numberOfWorkIntervals;
    currentTime = currentMode == "Work" ? workTime : restTime
    updateCountdown(currentTime)
    countdown(currentTime);
}
