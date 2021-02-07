let numbers = [-4000, -18, 0, 2.718, 3, 5, 7, 10, 15, 60, 100, 909, 13455, 238463, 2982342837435];

for(let i = 0; i < numbers.length; i++) {
    if((numbers[i] !== 0) && (numbers[i] % 3 == 0) && (numbers[i] % 5 == 0)) {
        console.log("FizzBuzz");
    } else if((numbers[i] !== 0) && (numbers[i] % 3 == 0)) {
        console.log("Fizz");
    } else if((numbers[i] !== 0) && (numbers[i] % 5 == 0)) {
        console.log("Buzz");
    } else if(numbers[i] == 2.718) {
        console.log("The exponential constant is not divisible by any number!");
    } else {
        console.log("This number is not divisible by 3 or 5!");
    }
}