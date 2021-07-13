// Navbar
(() => {

    const openNavMenu = document.querySelector(".open-nav-menu"),
        closeNavMenu = document.querySelector(".close-nav-menu"),
        navMenu = document.querySelector(".nav-menu"),
        menuOverlay = document.querySelector(".menu-overlay"),
        mediaSize = 991;

    openNavMenu.addEventListener("click", toggleNav);
    closeNavMenu.addEventListener("click", toggleNav);
    // close the navMenu by clicking outside
    menuOverlay.addEventListener("click", toggleNav);

    function toggleNav() {
        navMenu.classList.toggle("open");
        menuOverlay.classList.toggle("active");
        document.body.classList.toggle("hidden-scrolling");
    }

    navMenu.addEventListener("click", (event) => {
        if (event.target.hasAttribute("data-toggle") &&
            window.innerWidth <= mediaSize) {
            // prevent default anchor click behavior
            event.preventDefault();
            const menuItemHasChildren = event.target.parentElement;
            // if menuItemHasChildren is already expanded, collapse it
            if (menuItemHasChildren.classList.contains("active")) {
                collapseSubMenu();
            }
            else {
                // collapse existing expanded menuItemHasChildren
                if (navMenu.querySelector(".menu-item-has-children.active")) {
                    collapseSubMenu();
                }
                // expand new menuItemHasChildren
                menuItemHasChildren.classList.add("active");
                const subMenu = menuItemHasChildren.querySelector(".sub-menu");
                subMenu.style.maxHeight = subMenu.scrollHeight + "px";
            }
        }
    });
    function collapseSubMenu() {
        navMenu.querySelector(".menu-item-has-children.active .sub-menu")
            .removeAttribute("style");
        navMenu.querySelector(".menu-item-has-children.active")
            .classList.remove("active");
    }
    function resizeFix() {
        // if navMenu is open ,close it
        if (navMenu.classList.contains("open")) {
            toggleNav();
        }
        // if menuItemHasChildren is expanded , collapse it
        if (navMenu.querySelector(".menu-item-has-children.active")) {
            collapseSubMenu();
        }
    }

    window.addEventListener("resize", function () {
        if (this.innerWidth > mediaSize) {
            resizeFix();
        }
    });

})();

/*

// Contact Form

const form = document.getElementById('form');
const name = document.getElementById('name');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
const message = document.getElementById('message');

// Add Events

form.addEventListener('submit', (event) => {
    event.preventDefault();
    validate();
});

const sendData = (nameVal, sRate, count) => {
    if (sRate === count) {
        swal("Thanks " + nameVal, "We will get back to you soon!", "success");
        // location.href = `file name?name=${nameVal}`;
    }
}

// For final data validation

const successMsg = (nameVal) => {
    let formCon = document.getElementsByClassName('form-control');
    var count = formCon.length - 1;
    for (var i = 0; i < formCon.length; i++) {
        if (formCon[i].className === "form-control success") {
            var sRate = 0 + i;
            sendData(nameVal, sRate, count);
        } else {
            return false;
        }
    }
}

// More Email Validate

const isEmail = (emailVal) => {
    var atSymbol = emailVal.indexOf("@");
    if (atSymbol < 1) {
        return false;
    }

    var dot = emailVal.lastIndexOf('.');
    if (dot < atSymbol + 4) {
        return false;
    }

    if (dot === emailVal.length - 1) {
        return false;
    }

    return true;
}

// Define Validate Function

const validate = () => {
    const nameVal = name.value.trim();
    const emailVal = email.value.trim();
    const phoneVal = phone.value.trim();
    const messageVal = message.value.trim();

    // validate name

    if (nameVal === "") {
        setErrorMsg(name, 'Enter your Name');
    } else if (nameVal.length < 2) {
        setErrorMsg(name, 'Minimum 3 Characters allowed');
    } else {
        setSuccessMsg(name);
    }

    // Validate Email

    if (emailVal === "") {
        setErrorMsg(email, 'Enter Valid Email');
    } else if (!isEmail(emailVal)) {
        setErrorMsg(email, 'Not Valid');
    } else {
        setSuccessMsg(email);
    }

    // Validate Phone Number

    if (phoneVal === "") {
        setErrorMsg(phone, 'Enter Phone Number');
    } else if (phoneVal.length < 6 || phoneVal.length > 15) {
        setErrorMsg(phone, 'Mobile Number Not Valid');
    } else {
        setSuccessMsg(phone);
    }

    // Validate Message

    if (messageVal === "") {
        setErrorMsg(message, 'Enter Message');
    } else {
        setSuccessMsg(message);
    }

    successMsg(nameVal);

}

function setErrorMsg(input, errormsgs) {
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    formControl.className = "form-control error";
    small.innerText = errormsgs;
}

function setSuccessMsg(input) {
    const formControl = input.parentElement;
    formControl.className = "form-control success";
}

*/