function success(evt,d,e) {
    mapping = ["Kein Zeichen","Punkt","Komma","!","?"]

    data = JSON.parse( evt.target.responseText );
    document.querySelector('#result').innerHTML = "<dl>" +
    data.result.map(function(probability, index) {
        active = ((""+index) == data.max) ? "active" : "";
        return "<dt class="+active+">"+mapping[index]+"</dt><dd class="+active+">"+probability.toFixed(2)+"</dd>";
    }).join("") + "</dl>";
    console.log(data);
}
function showTip(target) {
    data = "text=" + encodeURI( target.value );

    var ajax = new XMLHttpRequest();
    ajax.open( "GET", "/api/v1/predict?" + data, true);
    ajax.onload = success;
    ajax.send();
}


document.addEventListener('DOMContentLoaded', function(){
    // See more options here: https://github.com/qrohlf/trianglify#options
    var pattern = Trianglify({
        seed: 31337,
        width: window.innerWidth,
        height: window.innerHeight
    });
    document.body.appendChild(pattern.canvas())

    document.addEventListener('input', function(e){
        showTip(e.target);
    });
    var input = document.querySelector('textarea');
    input.value = "Hier kommt der Text hin";
    showTip(input);
});