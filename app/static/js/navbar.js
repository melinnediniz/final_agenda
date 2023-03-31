window.onscroll = function() {stick_div()};
let navbar = document.getElementsByClassName("navbar");
let sticky = navbar.offsetTop;

document.body.onload = createNavbar;

function createNavbar(){
    const navbar = `
        <a id="menu-item" href="#">
        <img class="menu-icon" src="/static/img/nav-menu.svg" alt="menu"/>
        </a>
            <h3 id="title">Agenda</h3>
        <a id="logout" href="#">
        <img class="menu-icon" src="/static/img/logout.svg" alt="logout"/>
        </a>
    `;

    const page = document.getElementById("page")
    let divNavbar = document.createElement("div")
    divNavbar.className = "navbar"
    divNavbar.innerHTML += navbar
    page.appendChild(divNavbar) 
    page.insertBefore(divNavbar, page.firstChild)
}

function stick_div() {
  if (window.scrollY >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
