/* let mainDiv = document.querySelector('main')
let changeButton = document.querySelector('button')

mainDiv.classList.add('alert')

changeButton.addEventListener('click', () => {
    mainDiv.classList.remove('alert')
    mainDiv.classList.add('alert1')
}) */

    // let pRed = document.createElement('p')
    // let h3 = document.createElement('h3')
    // let div = document.createElement('div')
    // let h1 = document.createElement('h1')
    // let p = document.createElement('p')
    // document.body.append(pRed, h3, div)
    // div.append(h1, p)

    // pRed.textContent = 'Привет, я красный!';
    // pRed.style.color ='red';

    // h3.textContent = 'Я синий h3';
    // h3.style.color = 'blue';

    // h1.textContent = 'Я div блок';
    // p.textContent = 'Я тоже!';

    let htmlDoc = document.getElementById('htmlDoc')
    let cssDoc = document.getElementById('cssDoc')
    let jsDoc = document.getElementById('jsDoc')
    let text = document.getElementById('text')
    let main = document.getElementById('main')

    htmlDoc.addEventListener('click', () => {
        text.textContent = 'Random text about html';
        htmlDoc.style.color =  'rgb(107, 152, 188)';
        htmlDoc.style.backgroundColor = 'rgb(42, 85, 118)';
        cssDoc.style.color =  'rgb(19, 79, 91)';
        cssDoc.style.backgroundColor = 'rgb(107, 152, 188)';
        jsDoc.style.color =  'rgb(19, 79, 91)';
        jsDoc.style.backgroundColor = 'rgb(107, 152, 188)';
    })
    cssDoc.addEventListener('click', () => {
        text.textContent = 'Random text about css';
        cssDoc.style.color =  'rgb(107, 152, 188)';
        cssDoc.style.backgroundColor = 'rgb(42, 85, 118)';
        htmlDoc.style.color =  'rgb(19, 79, 91)';
        htmlDoc.style.backgroundColor = 'rgb(107, 152, 188)';
        jsDoc.style.color =  'rgb(19, 79, 91)';
        jsDoc.style.backgroundColor = 'rgb(107, 152, 188)';
    })
    jsDoc.addEventListener('click', () => {
        text.textContent = 'Random text about js';
        jsDoc.style.color =  'rgb(107, 152, 188)';
        jsDoc.style.backgroundColor = 'rgb(42, 85, 118)';
        cssDoc.style.color =  'rgb(19, 79, 91)';
        cssDoc.style.backgroundColor = 'rgb(107, 152, 188)';
        htmlDoc.style.color =  'rgb(19, 79, 91)';
        htmlDoc.style.backgroundColor = 'rgb(107, 152, 188)';
    })
 