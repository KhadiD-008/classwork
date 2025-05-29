// let fruits = ['mango', 'orange', 'apple', 'blueberry']
// fruits.sort()

// function a() {

//    let ul = document.createElement('ul')

//     fruits.forEach(i => {
//      let li = document.createElement('li');
//      li.textContent = i;
//      ul.appendChild(li);
//    })

//     document.body.appendChild(ul);
// }
// a()

// function b () {

// }

let array1 = [1, 3, 16, 4];
let array2 = [16, 3, 26, 34];

function newArray(arrOne, arrTwo) {
   let array3 = []

    for(i = 0; i < array1.length; i++) {
        for(j = 0; i < array2.length; i++) {
           if(!i == j) {
            array3 = i
           } 
        }
    }
    console.log(array3);
    
    return array3
}
newArray(array1, array2)