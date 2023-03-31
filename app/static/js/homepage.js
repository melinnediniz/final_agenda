const daysTag = document.querySelector(".days");
let currentDate = document.querySelector(".current-date");
let prevNextIcon = document.querySelector(".icons");
let prev = document.querySelector("#prev");
let next = document.querySelector("#next");
let date = new Date();
let currYear = date.getFullYear();
let currMonth = date.getMonth();

console.log(prev, next)

const monthsName = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

const renderCalendar = () => {
    let firstDayMonth = new Date(currYear, currMonth, 1).getDay(); 
    let lastDateMonth = new Date(currYear, currMonth + 1, 0).getDate();
    let lastDayMonth = new Date(currYear, currMonth, lastDateMonth).getDay();
    let lastDateLastMonth = new Date(currYear, currMonth, 0).getDate();
    let liTag = "";
    for (let i = firstDayMonth; i > 0; i--) {
        liTag += `<li class="inactive"><p>${lastDateLastMonth - i + 1}</p></li>`;
    }
    for (let i = 1; i <= lastDateMonth; i++) { 
        let isToday = i === date.getDate() && currMonth === new Date().getMonth() 
                     && currYear === new Date().getFullYear() ? "active" : "";
        liTag += `<li class="${isToday}"><p>${i}</p></li>`;
    }
    for (let i = lastDayMonth; i < 6; i++) {
        liTag += `<li class="inactive"><p>${i - lastDayMonth + 1}</p</li>`
    }
    currentDate.innerText = `${monthsName[currMonth]}, ${currYear}`;
    daysTag.innerHTML = liTag;
}

renderCalendar();

function instanceNewYear(){
    date = new Date(currYear, currMonth, new Date().getDate());
    currYear = date.getFullYear();
    currMonth = date.getMonth();
}

prev.addEventListener("click", () =>{
    currMonth = currMonth - 1;

    if(currMonth < 0){
        instanceNewYear();
    }
    else{
        date = new Date();
    }
    renderCalendar();
})

next.addEventListener("click", () =>{
    currMonth = currMonth + 1;

    if(currMonth > 11){
        instanceNewYear();
    }
    else{
        date = new Date();
    }
    renderCalendar();
})

