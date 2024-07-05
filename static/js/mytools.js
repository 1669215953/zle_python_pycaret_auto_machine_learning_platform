window.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.mycheck_button').forEach((checkbox) => {
        checkbox.addEventListener('change', (event) => {
            event.target.style.backgroundColor = event.target.checked ? '#84b52f' : '#ddd';
        });
    });
});