let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
let activeTaskIndex = JSON.parse(localStorage.getItem("activeTaskIndex"));

window.onload = function () {
    renderTasks();
};

function addTask() {
    const input = document.getElementById("taskInput");
    const text = input.value.trim();

    if (!text) return;

    tasks.push({
        text: text,
        completed: false,
        timeSpent: null
    });

    input.value = "";
    saveTasks();
    renderTasks();
}

function selectTask(index) {
    activeTaskIndex = index;

    localStorage.setItem("activeTaskIndex", JSON.stringify(index));
    localStorage.setItem("taskStartTime", Date.now());

    renderTasks();
}

function deleteTask(index) {
    if (activeTaskIndex === index) {
        localStorage.removeItem("activeTaskIndex");
        localStorage.removeItem("taskStartTime");
        activeTaskIndex = null;
    }

    tasks.splice(index, 1);

    if (activeTaskIndex !== null && index < activeTaskIndex) {
        activeTaskIndex--;
        localStorage.setItem("activeTaskIndex", JSON.stringify(activeTaskIndex));
    }

    saveTasks();
    renderTasks();
}

function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function renderTasks() {
    const list = document.getElementById("taskList");
    list.innerHTML = "";

    tasks.forEach((task, index) => {
        const li = document.createElement("li");

        li.innerHTML = `
            <span 
                onclick="selectTask(${index})"
                class="${task.completed ? 'done' : ''} ${activeTaskIndex === index ? 'active-task' : ''}"
            >
                ${task.completed ? "✔ " : ""}${task.text}
                ${task.timeSpent ? `<br><small>⏱ ${task.timeSpent}</small>` : ""}
            </span>

            <button onclick="deleteTask(${index})">✕</button>
        `;

        list.appendChild(li);
    });
}
