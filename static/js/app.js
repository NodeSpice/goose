// Movement of login Page

// // Movement Animation to happen
// const card = document.querySelector('.card001');
// const container = document.querySelector('.container001');

// // Animate Items
// const title = document.querySelector(".title001");
// const image = document.querySelector(".logo001 img");
// const description = document.querySelector(".info001 h3");


// // Moving Animation event
// container.addEventListener('mousemove', (e) =>{
//     let xAxis = (window.innerWidth / 2 - e.pageX) /25;
//     let yAxis = (window.innerHeight / 2 - e.pageY) /25;
//     card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`; 
// });

// // Animate In
// container.addEventListener('mouseenter', (e) => {
//     card.style.transition = "none";
//     //Popout
//     title.style.transform = "translateZ(150px)";
//     image.style.transform = "translateZ(200px) rotateZ(-45deg)";
//     description.style.transform = "translateZ(125px)";
// });

// // Animate Out
// container.addEventListener('mouseleave', (e) => {
//     card.style.transition = "all 0.5s ease";
//     card.style.transform = `rotateY(0deg) rotateX(0deg)`;
//     //Popout
//     title.style.transform = "translateZ(0px)";
//     image.style.transform = "translateZ(0px) rotateZ(0deg)";
//     description.style.transform = "translateZ(0px)";
// });

// Login Page

$('.button').on('click', function () {
    $('.login').addClass('loading').delay(2200).queue(function () {
        $(this).addClass('active')
    });
});