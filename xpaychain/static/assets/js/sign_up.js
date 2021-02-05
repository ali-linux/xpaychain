//show password

const x = document.querySelector(".register-area");
const y = document.querySelector(".register-area");

const show_password = document.querySelector("#show-password"),
  hide_password = document.querySelector("#hide-password"),
  show_password2 = document.querySelector("#show-password2"),
  hide_password2 = document.querySelector("#hide-password2"),
  password1 = document.querySelector("#password"),
  password2 = document.querySelector("#password2");

x.addEventListener("click", kk);
y.addEventListener("click", yy);

function kk(e) {
  if (e.target.id === "show-password") {
    show_password.style.display = "none";
    hide_password.style.display = "inline";
    password1.setAttribute("type", "text");
  }
  if (e.target.id === "hide-password") {
    show_password.style.display = "inline";
    hide_password.style.display = "none";
    password1.setAttribute("type", "password");
  }
}

function yy(e) {
  if (e.target.id === "show-password2") {
    show_password2.style.display = "none";
    hide_password2.style.display = "inline";
    password2.setAttribute("type", "text");
  }
  if (e.target.id === "hide-password2") {
    show_password2.style.display = "inline";
    hide_password2.style.display = "none";
    password2.setAttribute("type", "password");
  }
}

//add file

document.querySelectorAll('.uploader input[type="file"]').forEach((el) =>
  el.addEventListener("change", (ev) => {
    if (ev.target.files && ev.target.files.length) {
      const text = Array.from(ev.target.files)
        .map((x) => x.name)
        .join(", ");
      el.parentNode.querySelector(".placeholder").innerText = text;
    }
  })
);
