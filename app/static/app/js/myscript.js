$('.plus-cart').click(function(){
   var id=$(this).attr("pid").toString();
   var eml=this.parentNode.children[2];
  
   $.ajax({
      type:"GET",
      url:"/pluscart",
      data:{
         prod_id:id
      
      },
      success:function(data){
         console.log("data=", data);
         eml.innerText=data.quantity
         document.getElementById("amount").innerText=data.amount
         document.getElementById("totalamount").innerText=data.totalamount
      }

   })
})

$('.minus-cart').click(function(){
   var id=$(this).attr("pid").toString();
   var eml=this.parentNode.children[2];
   
   $.ajax({
      type:"GET",
      url:"/minuscart",
      data:{
         prod_id:id
      
      },
      success:function(data){
         console.log("data=", data);
         eml.innerText=data.quantity
         document.getElementById("amount").innerText=data.amount
         document.getElementById("totalamount").innerText=data.totalamount
      }

   })
})

$(document).ready(function () {
   $(".remove-cart").click(function () {
       var id = $(this).attr("pid").toString();
       var eml = this;

       $.ajax({
           type: "GET",
           url: "/removecart/",
           data: { prod_id: id },
           success: function (data) {
               console.log("Remove response:", data);

               // ✅ Remove the item from the UI
               $(eml).closest(".row").remove();

               // ✅ Update total amount dynamically
               $("#amount").text("Rs. " + data.amount);
               $("#totalamount").text("Rs. " + data.totalamount);
       // ✅ If cart is empty, show "Cart is Empty" message
               if (data.amount === 0) {
                   $(".container .row").html("<h1 class='text-center mb-5'>Cart is Empty</h1>");
               }
           },
           error: function (error) {
               console.log("Error:", error);
           }
       });
   });
});
 


$(document).on('click', '.plus-wishlist', function(event){
   event.preventDefault();  // Prevent default behavior
   var id = $(this).attr("pid").toString();
   var button = $(this); // Store reference to button

   $.ajax({
       type: "GET",
       url: "/pluswishlist",
       data: { prod_id: id },
       success: function(data){
           alert(data.message); // Show only one success message

           // Update the button dynamically
           button.removeClass('plus-wishlist').addClass('minus-wishlist');
           button.html('<i class="fa fa-heart text-danger"></i>'); // Change icon/color
       }
   });
});

$(document).on('click', '.minus-wishlist', function(event){
   event.preventDefault();  // Prevent default action
   var id = $(this).attr("pid").toString();
   var button = $(this); // Store reference to button

   $.ajax({
       type: "GET",
       url: "/minuswishlist",
       data: { prod_id: id },
       success: function(data){
           alert(data.message); // Show only one success message

           // Update the button dynamically
           button.removeClass('minus-wishlist').addClass('plus-wishlist');
           button.html('<i class="fa fa-heart text-gray"></i>'); // Change icon/color
       }
   });
});




