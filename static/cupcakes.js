
const BASE_URL = '/api/cupcakes'

$(document).ready(listCupcakes)
$('button').click(addCupcake)

async function listCupcakes(){
    const resp = await axios.get(BASE_URL)
    const cupcakes = resp.data.cupcakes
    for(let i in cupcakes){
        const $list = $('.cupcakes')
        const $newLi = $(`<li class="list-group-item"></li>`)
        const $flavor = $(`<h4>${cupcakes[i]['flavor']}</h4>`)
        const $size = $(`<small class="d-block text-end">size: ${cupcakes[i]['size']}</small>`)
        const $rating = $(`<small class="d-block text-end">rating: ${cupcakes[i]['rating']}</small>`)
        $flavor.appendTo($newLi)
        $size.appendTo($newLi)
        $rating.appendTo($newLi)
        $newLi.appendTo($list)
    }
}

async function addCupcake(evt){
    evt.preventDefault()
    console.log($("#flavor").val())

    const data = {
        'flavor': $("#flavor").val(),
        'size' : $("#size").val(),
        'rating': parseFloat($("#rating").val()),
        'image': $("#image").val()
    };

    
    await axios.post(BASE_URL, json=data)
    $('input').val("")
    $('.cupcakes').empty()
    listCupcakes()

}