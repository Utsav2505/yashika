// console.log("hello world yashika");
// function AddThreeNumers(a, b, c) {
//     return (a + b + c);
// }

// let c = AddThreeNumers(1, 2, 4)
// console.log(c)


// var b = "harry"
// {
//     var b = "this";
//     console.log(b)
// }
// console.log(b)


// let a = "yashika";
// var a = "aggarwal";
// console.log(a);


// let a = "kunal"
// {
//     a = "kushwaha";
//     console.log(a);
// }
// console.log(a);


// let a = null;
// let b = 345;
// let c = true;
// let d = BigInt("567");
// let e = "hello";
// let f = Symbol("i am a good symbol");
// let g = undefined;
// console.log(a, b, c, d, e, f, g);

// let h = BigInt('5') + BigInt('6');
// console.log(h);

// console.log(typeof a);
// console.log(typeof b);
// console.log(typeof c);
// console.log(typeof d);
// console.log(typeof e);
// console.log(typeof f);
// console.log(typeof g);
// console.log(typeof h);


// a = prompt("enter your age: ")
// console.log("your age is", a)


// let marks = {
//     harry: 90,
//     shubham: 9,
//     lovish: 56,
//     Monika: 4
// }
// console.log(Object.values(marks).length)

// s = 'harry';
// console.log(s.length)

// s = `harry 'is' is good's`;
// console.log(s)


// let n = [1, 2, 3, 4, 0, 8, 9, 100];
// delete n[0];
// n.sort()
// n.splice(-1, 10, 10)
// console.log(n)



// let arr = Number.parseInt(Math.random());
// let count = 0;
// let a = 0;
// do {
//     count++;
//     a = prompt("enter the guessed no, you thought: ");
//     if (a > arr) {
//         console.log(`you guess is greater than the actual number and u have only ${arr - count} chances left`);

//     }
//     else if (a < arr) {
//         console.log(`you guess is smaller than the actual number and u have only ${arr - count} chances left`);
//     }

//     else if (a == arr) {
//         console.log(`you won the game \n your score is ${100 - count} \n and the number is really ${arr} `);
//         break;

//     }

//     if (count == arr) {
//         console.log("try next time");
//         break; 
//     }
// } while (a != arr);


// let arr = Number.parseInt(Math.random() * 100);
// console.log(arr);


// console.time('a');
// console.error("this is an error message");
// console.assert(5 < 3);
// console.clear();
// ob = { a: 1, b: 2, c: 3 };
// console.table(ob);
// console.info("this is an info ")
// console.timeEnd('a');


// console.time("forloop")
// for (let i = 0; i < 5; i++) {
//     console.log(233);
// }
// console.timeEnd("forloop")


// alert("this is an alert");

// let a = "yashika";
// console.log(a);


//using while loop:-
let characters = ['s', 'w', 'g'];
let runAgain = true;
while (runAgain) {
    let comp = 0;
    let player = 0;
    while (comp + player < 5) {
        let a = Number.parseInt(Math.random() * characters.length);
        let bycomp = characters[a];
        let byplayer = prompt("enter either(s/w/g):-")
        if (bycomp == 's') {
            if (byplayer == 'w') {
                comp++;
                console.log("oops!..u lost");
            }
            else if (byplayer == 'g') {
                player++;
                console.log("ur score increased by one");
            }
            else {
                console.log("u both entered same character..do it again ")
            }

        }
        else if (bycomp == 'w') {
            if (byplayer == 'g') {
                comp++;
                console.log("oops!..u lost");
            }
            else if (byplayer == 's') {
                player++;
                console.log("ur score increased by one");

            }
            else {
                console.log("u both entered same character..do it again ")
            }
        }

        else if (bycomp == 'g') {
            if (byplayer == 's') {
                comp++;
                console.log("oops!..u lost");
            }
            else if (byplayer == 'w') {
                player++;
                console.log("ur score increased by one");
            }
            else {
                console.log("u both entered same character..do it again ")
            }
        }
    }
    (player > comp) ? (`Congratulations!! you won ...ur score is ${player}/5`) : (`sorry!! you lost the match...ur score is ${player}/5`);
    runAgain = confirm("Do You Want to Play again?");
}



