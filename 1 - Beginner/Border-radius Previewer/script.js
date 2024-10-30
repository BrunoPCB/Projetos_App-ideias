
function change_border(){

    let quadrado     = document.getElementById('box');
    let top_left     = document.getElementById('ip_top_left');
    let top_rigth    = document.getElementById('ip_top_right');
    let bottom_left  = document.getElementById('ip_bottom_left');
    let bottom_rigth = document.getElementById('ip_bottom_right');
    let size         = document.getElementById('ip_tamanho');

    console.log(top_left == null)

    if (top_left.value != '') {
        quadrado.style.borderTopLeftRadius = top_left.value + 'px';
    }
    
    if (top_rigth.value != '') {
        quadrado.style.borderTopRightRadius = top_rigth.value + 'px';
    }

    if (bottom_left.value != '') {
        quadrado.style.borderBottomLeftRadius = bottom_left.value + 'px';
    }
    
    if (bottom_rigth.value != '') {
        quadrado.style.borderBottomRightRadius = bottom_rigth.value + 'px';
    } 
    
    var content = document.getElementById('css_comand');

    var border_css = 'border-radius: ' + top_left.value + 'px ' + top_rigth.value + 'px ' + bottom_rigth.value + 'px ' + bottom_left.value + 'px';

    console.log(border_css);

    content.value =  border_css;

}

function copy_css_comand(){
    var content = document.getElementById('css_comand');

    navigator.clipboard.writeText(content.value);
}
