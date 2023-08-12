function updateTime() {
    var now = new Date();
    var day = now.toLocaleDateString('vi-VN', { weekday: 'long' });
    var date = now.toLocaleDateString('vi-VN', { day: 'numeric', month: 'numeric', year: 'numeric' });
    var time = now.toLocaleTimeString('vi-VN', { hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: false });

    var clock = document.getElementById('theClock');
    clock.innerHTML = day + ', ' + date + ' ' + time;
}
setInterval(updateTime, 1000);    

