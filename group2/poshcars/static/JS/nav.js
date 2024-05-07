document.addEventListener("DOMContentLoaded", function () {
   const iconBtn = document.querySelector("#iconBtn");

   const mobile = document.querySelector("#mobileview");

   const menuItems = document.querySelectorAll(".navbar-links li a");

   const menuBar = document.querySelector("#bars");

   const path = window.location.pathname;


   function adjustContentMargin() {
      const contentBelowNavbar = document.querySelector("#content-below-navbar");

      const contentHome = document.querySelector("#content-home");
      if (mobile.classList.contains("hide")) {
      } else {
        contentBelowNavbar.style.marginTop = mobile.offsetHeight + "px";

      //   contentHome.style.marginTop = "20%";
      //   contentHome.style.height = "100vh";
      }
    }


   menuItems.forEach(function(menuItem){
      if (menuItem.href.includes(path)){
         //  menuItem.classList.add("active");
      }
  
  });

  iconBtn.addEventListener('click', function(){
   mobile.classList.toggle("hide");
   if (mobile.classList.contains('hide')){
       menuBar.classList.remove('fa-xmark')
       menuBar.classList.add('fa-bars')
     
   }

   else{
       menuBar.classList.remove('fa-bars')
       menuBar.classList.add('fa-xmark')
      
   }
   adjustContentMargin();

})
adjustContentMargin();  

  });


