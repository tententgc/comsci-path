const input = document.querySelector('input');
const addBtn = document.querySelector('#addBtn');
const list = document.querySelector('#list');

addBtn.addEventListener('click', () => {
    const task = input.value.trim();
    if (task) {
        const li = document.createElement('li');
        const span = document.createElement('span');
        span.textContent = task;
        const delBtn = document.createElement('button');
        delBtn.textContent = 'Delete';
        delBtn.addEventListener('click', () => {
            li.remove();
        });
        li.appendChild(span);
        li.appendChild(delBtn);
        list.appendChild(li);
        input.value = '';
    }
});

input.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        addBtn.click();
    }
});
