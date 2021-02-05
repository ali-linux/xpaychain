const info = document.getElementById("info"),
  five = document.getElementById("five"),
  ten = document.getElementById("ten"),
  twenty = document.getElementById("twenty"),
  fifty = document.getElementById("fifty");

const close_btn = document.querySelector(".close-btn");

info.style.display = "none";

five.addEventListener("click", five_func);
ten.addEventListener("click", ten_func);
twenty.addEventListener("click", twenty_func);
fifty.addEventListener("click", fifty_func);
info.addEventListener("click", close_func);

close_btn.addEventListener("click", close_func);

function close_func() {
  info.style.display = "none";
}

function more_info(amount) {
  info.style.display = "flex";
  const plan = document.querySelector(".info-h1");
  const tbody = document.querySelector(".table-body");

  if (amount === 5000) {
    plan.textContent = "5,000 USDT + ";

    tbody.innerHTML = `
        <tr class="winner__table">
        <td>6 month</td>
        <td>7</td> 
        <td>2,100</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
            </tr>
        <tr class="winner__table">
        <td>12 month</td>
        <td>8</td> 
        <td>4,800</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
        </tr>
        <tr class="winner__table">
        <td>24 month</td>
        <td>8.5</td> 
        <td>10,200</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
        </tr>
        `;
  }
  if (amount === 10000) {
    plan.textContent = "10,000 USDT + ";
    tbody.innerHTML = `
    <tr class="winner__table">
    <td>6 month </td>
        <td>8%</td>
        <td>4800</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
    </tr>
    <tr class="winner__table">
        <td>12 month</td>
        <td>9%</td>
        <td>10,800</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
        </tr>
    <tr class="winner__table">
        <td>24 month</td>
        <td>9.5%</td>
        <td>22,800</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
    </tr>
    `;
  }
  if (amount === 20000) {
    plan.textContent = "20,000 USDT + ";

    tbody.innerHTML = `
    <tr class="winner__table">
    <td>6 month </td>
        <td>9%</td>
        <td>10,800</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
    </tr>
    <tr class="winner__table">
        <td>12 month</td>
        <td>9.5%</td>
        <td>22,800</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
        </tr>
    <tr class="winner__table">
        <td>24 month</td>
        <td>10%</td>
        <td>48,000</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
    </tr>
    `;
  }
  if (amount === 50000) {
    plan.textContent = "50,000 USDT + ";
    tbody.innerHTML = `
    <tr class="winner__table">
    <td>6 month </td>
        <td>9%</td>
        <td>33,800</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
    </tr>
    <tr class="winner__table">
        <td>12 month</td>
        <td>9.5%</td>
        <td>57,800</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
        </tr>
    <tr class="winner__table">
        <td>24 month</td>
        <td>10%</td>
        <td>120,000</td>
        <td>1</td>
        <td>3</td>
        <td>0.5</td>
        <td>1.5</td>
    </tr>
    `;
  }
}

function close_func(e) {
  if (e.target.id === "info" || e.target.id === "close-btn") {
    info.style.display = "none";
  }
}

function five_func(e) {
  more_info(5000);
}

function ten_func(e) {
  more_info(10000);
}

function twenty_func(e) {
  more_info(20000);
}

function fifty_func(e) {
  more_info(50000);
}
