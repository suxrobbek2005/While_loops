
// let oddNumber = 1

// console.log("1 dan 100 gacha bo'lgan sonlar ichida toq sonlar qatori")
// while (oddNumber <= 100){
//     if(oddNumber % 2 == 1){
//         console.log(oddNumber)
//     }
//     oddNumber = oddNumber + 1
// }


function oddNumber(number){
    console.log("1 dan 100 gacha bo'lgan sonlar ichidan faqat toqlari")
    while (number < 100){
        if(number % 2 == 1){
            console.log(number)
        }
        number++
    }
}

oddNumber(1)