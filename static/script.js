let cookies = 0;
let cookiesPerSecond = 0;

const items = {
    Cursor: { price: 15, cps: 0.1, owned: 0 },
    Grandma: { price: 100, cps: 1, owned: 0 },
    Factory: { price: 500, cps: 5, owned: 0 },
    Mine: { price: 2000, cps: 10, owned: 0 },
    Shipment: { price: 7000, cps: 20, owned: 0 },
    'Alchemy Lab': { price: 50000, cps: 50, owned: 0 },
    Portal: { price: 1000000, cps: 100, owned: 0 },
    'Time Machine': { price: 123456789, cps: 500, owned: 0 },
};

function updateUI() {
    document.getElementById('cookie-count').innerText = `🍪 ${cookies}`;
    document.getElementById('cps').innerText = `cookies/second: ${cookiesPerSecond.toFixed(1)}`;

    for (let item in items) {
        const button = document.querySelector(`[data-item='${item}']`);
        if (cookies >= items[item].price) {
            button.classList.remove('disabled');
        } else {
            button.classList.add('disabled');
        }
    }
}

function clickCookie() {
    cookies++;
    updateUI();
}

function buyItem(item) {
    if (cookies >= items[item].price) {
        cookies -= items[item].price;
        items[item].owned++;
        cookiesPerSecond += items[item].cps;
        items[item].price = Math.ceil(items[item].price * 1.15); // Збільшення ціни

        document.querySelector(`[data-item='${item}'] .price`).innerText = `🍪 ${items[item].price}`;
        document.querySelector(`[data-item='${item}'] .owned`).innerText = `Owned: ${items[item].owned}`;

        updateUI();
    }
}

setInterval(() => {
    cookies += cookiesPerSecond / 10; // Підрахунок кожні 100 мс для плавності
    updateUI();
}, 100);

function resetGame() {
    cookies = 0;
    cookiesPerSecond = 0;
    for (let item in items) {
        items[item].price = {
            Cursor: 15,
            Grandma: 100,
            Factory: 500,
            Mine: 2000,
            Shipment: 7000,
            'Alchemy Lab': 50000,
            Portal: 1000000,
            'Time Machine': 123456789,
        }[item];
        items[item].owned = 0;
        document.querySelector(`[data-item='${item}'] .price`).innerText = `🍪 ${items[item].price}`;
        document.querySelector(`[data-item='${item}'] .owned`).innerText = `Owned: 0`;
    }
    updateUI();
}
