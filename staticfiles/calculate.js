document.addEventListener('DOMContentLoaded', function() {
    const moneyInput = document.getElementById('id_money');
    const monthInput = document.getElementById('id_month');
    const monthTomoneyInput = document.getElementById('id_monthTomoney');

    function calculateMonthTomoney() {
        const money = parseFloat(moneyInput.value);
        const month = parseFloat(monthInput.value);

        if (!isNaN(money) && !isNaN(month) && month > 0) {
            const monthTomoney = money / month;
            monthTomoneyInput.value = monthTomoney.toFixed(2); // 2 o'nlik nuqta bilan
        } else {
            monthTomoneyInput.value = "Invalid input";
        }
    }

    if (moneyInput && monthInput) {
        moneyInput.addEventListener('input', calculateMonthTomoney);
        monthInput.addEventListener('input', calculateMonthTomoney);
    }
});
