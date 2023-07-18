// Check if dark mode is enabled and update the UI accordingly
function updateDarkModeUI() {
    const body = document.querySelector('body');
    const container = document.querySelector('.container');
    const formGroupLabels = document.querySelectorAll('.form-group label');
    const formControls = document.querySelectorAll('.form-control');
    const modeIcon = document.getElementById('mode-icon');

    if (localStorage.getItem('darkMode') === 'true') {
        body.classList.add('dark-mode');
        container.classList.add('dark-mode');
        formGroupLabels.forEach((label) => label.classList.add('dark-mode'));
        formControls.forEach((control) => control.classList.add('dark-mode'));
        modeIcon.classList.remove('bi-moon');
        modeIcon.classList.add('bi-sun');
    } else {
        body.classList.remove('dark-mode');
        container.classList.remove('dark-mode');
        formGroupLabels.forEach((label) => label.classList.remove('dark-mode'));
        formControls.forEach((control) => control.classList.remove('dark-mode'));
        modeIcon.classList.remove('bi-sun');
        modeIcon.classList.add('bi-moon');
    }
}

// Toggle dark mode and update the UI
function toggleDarkMode() {
    const currentMode = localStorage.getItem('darkMode') === 'true';
    localStorage.setItem('darkMode', !currentMode);
    updateDarkModeUI();
}

// Attach event listener to mode toggle button
const modeToggle = document.getElementById('mode-toggle');
modeToggle.addEventListener('click', toggleDarkMode);

// Update the UI on initial page load
updateDarkModeUI();
