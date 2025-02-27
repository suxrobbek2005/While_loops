// 1 dan 100 gacha bo'lgan sonlarni kvadratlarini chiqaring.

// Natija: 1, 4, 9, 16, ..., 10000

let siccurence = 1
let result = 1

console.log("1 dan 100 gacha bo'lgan sonlarning kvatrati")
while(siccurence <= 100){
    result = siccurence ** 2
    console.log(result)
    siccurence++
}