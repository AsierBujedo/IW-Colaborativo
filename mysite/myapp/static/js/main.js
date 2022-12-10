window.onload = function () {
    var lightMode = window.localStorage.getItem('lightMode');
    var lightModeToggle = document.querySelector('#ldmode');

    var enableLightMode = () => {
        document.body.classList.add('bodyLightMode');
        document.getElementById("footer").classList.add('footerLightMode');
        const collection1 = document.getElementsByTagName("a");
        Array.from(collection1).forEach(function(item) {
            item.classList.add('aLightMode')
        });
        window.localStorage.setItem('lightMode', 'enabled');
        lightModeToggle.setAttribute('checked', true);
    }

    var disableLightMode = () => {
        document.body.classList.remove('bodyLightMode');
        document.getElementById("footer").classList.remove('footerLightMode');
        const collection1 = document.getElementsByTagName("a");
        Array.from(collection1).forEach(function(item) {
            item.classList.remove('aLightMode')
        });
        window.localStorage.setItem('lightMode', null);
    }

    if (lightMode === 'enabled') {
        enableLightMode();
    }

    lightModeToggle.addEventListener('click', () => {
        lightMode = window.localStorage.getItem('lightMode');
        if (lightMode !== 'enabled') {
            enableLightMode();
        } else {
            disableLightMode();
        }
    });
}  

/* $(document).ready(function(){
    $('#ldmode').click(function(){
    var element = document.body;
    element.classList.toggle("dark"); 
    });
}); */    