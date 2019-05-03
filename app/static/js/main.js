$(document).ready(function () {
  $("#update").click(function(){
    Swal.fire({
    type: 'success',
    title: 'Success',
    text: 'Profile Updated ',
    timer:2000,
    showConfirmButton:false
  })
  })
  $("#delete").click(function(){
    alert("are you sure")
    Swal.fire({
    type: 'success',
    title: 'Deleted',
    text: 'Your blog has been deleted',
    showConfirmButton:false
  })
})
  /*business logig*/

  $("#dele").click(function(){
    $(".del").show()
    $("#dele").hide()



  })
  $("#change").click(function(){
    $(".profiles").show()
    $("#change").hide()
  })
  $("#update").click(function(){
    $("#change").show()
    $(".profiles").hide()
  })

  $("#write").click(function(){

    $(".com").slideDown(2000)
      $(".com").show()

  })

  $("#yespro").mouseover(function(){
    $("#change").show()
  })
  $("#change").click(function(){
    $(".pro").show()
    $("#change").hide()
  })
  $("#yespro").mouseleave(function(){
    $("#change").hide()


  })
  $("#update").click(function(){
    $("#change").hide()
    $(".pro").hide()
  })


  $("#scro").click(function(){
    $("html,body").animate({scrollTop:$(document).height()},1000);
      return false;
  })


});
