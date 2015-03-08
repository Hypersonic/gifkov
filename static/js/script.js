window.onload = function() {
    document.getElementById('searchform').onsubmit = function(x) {
        console.log(x.target.children[0].value);
        x.preventDefault();
    }
}
