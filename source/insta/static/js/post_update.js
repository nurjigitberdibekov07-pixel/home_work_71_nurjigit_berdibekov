function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrftoken = getCookie('csrftoken');

async function makeRequest(url, method = 'GET', data = null, isFormData = false) {
    let options = {
        method: method,
        headers: {
            'X-CSRFToken': csrftoken,
            'Accept': 'application/json'
        }
    };

    if (data) {
        if (isFormData) {
            options.body = data;
        } else {
            options.headers['Content-Type'] = 'application/json';
            options.body = JSON.stringify(data);
        }
    }


    let response = await fetch(url, options);

    if (response.ok) {
        return await response.json();
    } else {
        let error = await response.json();
        return error
    }
}

async function onClick(event) {
    event.preventDefault();
    event.stopPropagation();

    let form = event.target;
    let formData = new FormData(form);

    let imageInput = form.querySelector('input[type="file"][name="image"]');
    if (imageInput && imageInput.files.length === 0) {
        formData.delete('image');
    }

    let url = form.action;
    let result = await makeRequest(url, 'PATCH', formData, true);

    let resultDiv = document.getElementById('result');

    if (result.error) {
        let errorText = result.error.text ? result.error.text.join(', ') : JSON.stringify(result.error);
        resultDiv.innerText = 'Ошибка: ' + errorText;
        resultDiv.style.color = 'red';
    } else {
        window.location.href = `/posts/7/`;
    }
}

function onload() {
    let form = document.getElementById('form');
    if (form) {
        form.addEventListener('submit', onClick);
    }
}

window.addEventListener('load', onload);