const workTime = 30*1000;
const restTime = 10*1000;
let currentTime = workTime;

const dataPercent = document.querySelectorAll('.data-Percent')[0];
const timer = document.getElementById('timer');


let countdownInterval;
updateCountdown(currentTime)
countdown(currentTime);

function countdown(pTime){
    countdownInterval = setInterval(() => {
        pTime = pTime - 1000;
        if (pTime <= 0)
        {
            clearInterval(countdownInterval);
        }

        //update countdown
        updateCountdown(pTime)
    }, 1000)
}

function updateCountdown(pTime) {
    if(pTime <= 0){
        //turn red, reset angle
        dataPercent.style.setProperty('--angle','360deg');
        dataPercent.style.setProperty('--colour','red');
        timer.innerText = `00:00`;
    } else {
         //calculate angle
    let angle = pTime / workTime *360 + 'deg';
    dataPercent.style.setProperty('--angle', angle); 

    //minutes & seconds
    let minutes = Math.floor(pTime/60/1000).toString().padStart(2,"0");
    let seconds = Math.floor((pTime/1000) % 60).toString().padStart(2, "0");
    timer.innerText = `${minutes}:${seconds}`;
    }

   
}
