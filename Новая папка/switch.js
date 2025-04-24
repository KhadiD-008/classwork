/* let mainDiv = document.querySelector('main')
let changeButton = document.querySelector('button')

mainDiv.classList.add('alert')

changeButton.addEventListener('click', () => {
    mainDiv.classList.remove('alert')
    mainDiv.classList.add('alert1')
}) */

    let pRed = document.createElement('p')
    let h3 = document.createElement('h3')
    let div = document.createElement('div')
    let h1 = document.createElement('h1')
    let p = document.createElement('p')
    document.body.append(pRed, h3, div)
    div.append(h1, p)

    pRed.textContent = 'Привет, я красный!';
    pRed.style.color ='red';

    h3.textContent = 'Я синий h3';
    h3.style.color = 'blue';

    h1.textContent = 'Я div блок';
    p.textContent = 'Я тоже!';