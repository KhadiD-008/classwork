

/*alert("hello world!")
confirm("Yes or no?")
let personAge = prompt("Age")
if (personAge > 18) {
console.log (personAge)
} else if (personAge == 18) {
    console.log ("normal")
} else {
    console.log ("nope")
}*/
/*let counter = 0
/*while (counter < 100) {
    counter = counter + 1
    console.log(counter)
}*/
/*for (let i = 10; i>= 1; i--) {
    console.log(i)
} */

    
   /* for ( let i = 1; i <= 100 ; i++ ) {
        let a = ""  
        if (i % 3 == 0) a += "Fizz"
        if (i % 5 == 0) a += "Buzz"
        console.log(a || i);
    } */

 /* let width = prompt ("Длина")
 let height = prompt ("Ширина")

      //1)
 function S () {
    let s = width * height
    console.log (s)
 }
 S()
      //2)
  function s (width, height) {
    console.log (width * height)
 }
 s (width, height) или s (promt(), promt()) */

 //массив array
 let array1 = [0, 1, 2, 3, 4, 5]
 function a(array) {
       let result = 0
       for (let i=0; i < array.length; i++) {
        result += array[i]
       }
       console.log (result)
 }
  a(array1)
