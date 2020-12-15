const info = document.getElementById('info'),
    five = document.getElementById('five'),
    ten = document.getElementById('ten'),
    twenty = document.getElementById('twenty'),
    fifty = document.getElementById('fifty');

const close_btn = document.querySelector('.close-btn');

info.style.display = 'none';

five.addEventListener('click', five_func);
ten.addEventListener('click', ten_func);
twenty.addEventListener('click', twenty_func);
fifty.addEventListener('click', fifty_func);
info.addEventListener('click', close_func);

close_btn.addEventListener('click', close_func);

function close_func() {
    info.style.display = 'none';
}

function more_info(amount) {
    info.style.display = 'flex';
    const plan = document.querySelector('.info-h1');
    const tbody = document.querySelector('.table-body');


    if (amount === 5000) {
        plan.textContent = '$5,000 + ';

        tbody.innerHTML =
            `
        <tr class="winner__table">
        <td>intrest rate %</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>8.5</td>
        </tr>
        <tr class="winner__table">
            <td>total intrest</td>
            <td>300</td>
            <td>2,100</td>
            <td>4,800</td>
            <td>10,200</td>
            </tr>
        <tr class="winner__table">
            <td>USDT (tethers) Monthly Withdrawal fees %</td>
            <td>1.5</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr class="winner__table">
            <td>USD (Cash) Monthly Withdrawal fees %</td>
            <td>3.3</td>
            <td>3</td>
            <td>3</td>
            <td>3</td>
        </tr>

        <tr class="winner__table">
            <td>USDT (tethers) Final total Withdrawal fees %</td>
            <td>1.5</td>
            <td>0.5</td>
            <td>0.5</td>
            <td>0.5</td>
        </tr>
        <tr class="winner__table">
            <td>USD (Cash) Final total Withdrawal fees %</td>
            <td>3.3</td>
            <td>1.5</td>
            <td>1.5</td>
            <td>1.5</td>
        </tr>
        
        `;
    }
    if (amount === 10000) {
        plan.textContent = '$10,000 + ';
        tbody.innerHTML =
            `
    <tr class="winner__table">
    <td>intrest rate %</td>
        <td>7%</td>
        <td>8%</td>
        <td>9%</td>
        <td>9.5%</td>
    </tr>
    <tr class="winner__table">
        <td>total intrest</td>
        <td>700</td>
        <td>4,800</td>
        <td>10,200</td>
        <td>22,800</td>
        </tr>
    <tr class="winner__table">
        <td>USDT (tethers) Monthly Withdrawal fees %</td>
        <td>1.5</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr class="winner__table">
        <td>USD (Cash) Monthly Withdrawal fees %</td>
        <td>3.3</td>
        <td>3</td>
        <td>3</td>
        <td>3</td>
    </tr>

    <tr class="winner__table">
        <td>USDT (tethers) Final total Withdrawal fees %</td>
        <td>1.5</td>
        <td>0.5</td>
        <td>0.5</td>
        <td>0.5</td>
    </tr>
    <tr class="winner__table">
        <td>USD (Cash) Final total Withdrawal fees %</td>
        <td>3.3</td>
        <td>1.5</td>
        <td>1.5</td>
        <td>1.5</td>
    </tr>
    
    `;

    }
    if (amount === 20000) {
        plan.textContent = '$20,000 + ';

        tbody.innerHTML =
            `
    <tr class="winner__table">
    <td>intrest rate %</td>
        <td>8%</td>
        <td>9%</td>
        <td>9.5%</td>
        <td>10%</td>
    </tr>
    <tr class="winner__table">
        <td>total intrest</td>
        <td>1,600</td>
        <td>10,800</td>
        <td>22,800</td>
        <td>48,000</td>
        </tr>
    <tr class="winner__table">
        <td>USDT (tethers) Monthly Withdrawal fees %</td>
        <td>1.5</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr class="winner__table">
        <td>USD (Cash) Monthly Withdrawal fees %</td>
        <td>3.3</td>
        <td>3</td>
        <td>3</td>
        <td>3</td>
    </tr>

    <tr class="winner__table">
        <td>USDT (tethers) Final total Withdrawal fees %</td>
        <td>1.5</td>
        <td>0.5</td>
        <td>0.5</td>
        <td>0.5</td>
    </tr>
    <tr class="winner__table">
        <td>USD (Cash) Final total Withdrawal fees %</td>
        <td>3.3</td>
        <td>1.5</td>
        <td>1.5</td>
        <td>1.5</td>
    </tr>
    
    `;

    }
    if (amount === 50000) {
        plan.textContent = '$50,000 + ';
        tbody.innerHTML =
            `
    <tr class="winner__table">
    <td>intrest rate %</td>
        <td>8%</td>
        <td>9%</td>
        <td>9.5%</td>
        <td>10%</td>
    </tr>
    <tr class="winner__table">
        <td>total intrest</td>
        <td>4000</td>
        <td>27,000</td>
        <td>57,000</td>
        <td>120,000</td>
        </tr>
    <tr class="winner__table">
        <td>USDT (tethers) Monthly Withdrawal fees %</td>
        <td>1.5</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr class="winner__table">
        <td>USD (Cash) Monthly Withdrawal fees %</td>
        <td>3.3</td>
        <td>3</td>
        <td>3</td>
        <td>3</td>
    </tr>

    <tr class="winner__table">
        <td>USDT (tethers) Final total Withdrawal fees %</td>
        <td>1.5</td>
        <td>0.5</td>
        <td>0.5</td>
        <td>0.5</td>
    </tr>
    <tr class="winner__table">
        <td>USD (Cash) Final total Withdrawal fees %</td>
        <td>3.3</td>
        <td>1.5</td>
        <td>1.5</td>
        <td>1.5</td>
    </tr>
    
    `;
    }

}



function close_func(e) {
    if (e.target.id === 'info' || e.target.id === 'close-btn') {
        info.style.display = 'none';
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