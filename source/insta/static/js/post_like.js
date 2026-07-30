let container = document.getElementById('container');

async function makeRequest(url, method = 'GET'){
    let response= await fetch(url, {method: method});
    if (response.ok){
        return await response.json();
    } else {
        let error = await response.json();

        let p = document.createElement('p');

        p.innerText= 'Возникла ошибка';
        p.style.color = 'red';
        container.appendChild(p);
    }
}

async function onClick(event) {
    event.preventDefault();
    event.stopPropagation();

    let link = event.target.closest('a');
    let counterId = link.dataset.likesId;
    let counter = document.getElementById('count-' + counterId);

    let isProfile = link.dataset.profile === 'true';
    let like_style = isProfile
        ? "font-size: 1.5rem; color: mediumpurple;"
        : "font-size: 2rem; color: mediumpurple;";

    let url = link.href;
    let response = await makeRequest(url);
    console.log(response);

    if (response.like) {
        link.innerHTML = `<i class="bi bi-heart-fill" style="${like_style}"></i>`;
    } else {
        link.innerHTML = `<i class="bi bi-heart" style="${like_style}"></i>`;
    }

    counter.innerText = response.count + ' likes';
}

function onload() {
    let links = document.querySelectorAll( "[data-key = 'likes']" );
    for (let link of links){
        link.addEventListener('click', onClick)
    }
}

window.addEventListener('load', onload)