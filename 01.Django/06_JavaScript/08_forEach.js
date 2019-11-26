// ESS for loop
// var iot1 = ['도현','혁진','은애']
// for(var i = 0; i < iot1.length; i++) {
//   console.log(iot1[i])
// }

// //ES6+
// const IOT1 = ['수연','승찬','한석','경희','영선']
// IOT1.forEach(function(student) {
//   console.log(student)
// })

// // 한 줄로 리팩토링 가능!
// IOT1.forEach( student => console.log(student))

// // forEach는 기본으로 들어오는 return 값은 없다.
// const result = IOT1.forEach(student => console.log(student))
// console.log(result) //undefined

// [실습] for를 forEach로 바꾸기!
// function handleStudents() {
//   const students = [
//     {id: 1, name: '오은애', status: '응애?'},
//     {id: 15, name:'서혁진', status: '기염둥이...'},
//     {id: 28, name: '김영선', status: '너무 쉽네 JS...'},
//   ]

//   for(let i = 0; i < students.length; i++) {
//     console.log(students[i])
//     console.log(students[i].name)
//     console.log(students[i].status)
//   }

//   students.forEach(function(student) {
//     console.log(student)
//     console.log(student.name)
//     console.log(student.status)
//   })
// }
// handleStudents()

// [실습] images 배열 안에 있는 정보를 곱해 넓이를 구하여 areas 배열에 저장하세요.
const images = [
  { height: 30, width: 55},
  { height: 50, width: 178},
  { height: 81, width: 35},
]

const areas = []

function handleImages() {
  images.forEach(function(image) {
    console.log(image.height * image.width)
    areas.push(image.height * image.width)
  })
}
handleImages()

console.log(areas)


