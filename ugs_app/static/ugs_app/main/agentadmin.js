$(document).ready(function(){
// /////////////////////////////////

$('#account_reg').on('submit',function(e){
    e.preventDefault()
    $('.adduser_err').html('')
    data=$(this).serializeArray()
    if($('.pass1').val() != $('.pass2').val()){
    $('.adduser_err').append('<div class="alert alert-danger alert-dismissible fade show" role="alert">\
    <strong>Password Not Matched!</strong>\
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\
    </div>')
    }else{
        
        $.ajax({
            method:'POST',
            url:'account_reg',
            data:data,
            success:function(res){
                if(res.data == 'ok'){
                  $('#account_reg').trigger('reset')
                //   load_users()
                    $('.adduser_err').append('<div class="alert alert-success alert-dismissible fade show" role="alert">\
                    <strong>Account was Created!</strong>\
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\
                    </div>')
                }
            }
        })

    }

    
})







// ///////////////////////////////



})