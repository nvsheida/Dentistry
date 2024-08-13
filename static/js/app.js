const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});


// sign up

const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


// Menu

const mainHead=document.querySelector('.main-head');
const logo = document.querySelector('.icon');
window.addEventListener('scroll', function(){
  if(this.scrollY >200){
    mainHead.classList.add('slidedown')
    logo.style.color = '#000';
    logo.border.color = '#000';
  }else{
    mainHead.classList.remove('services')
    logo.style.color = '';
  }
})
