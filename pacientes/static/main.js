
$(document).ready(function() {
    // AJAX request for when clicking on a patient link
    $(".paciente").click( function(){
        id = $(this).attr('id');
        const request = new XMLHttpRequest();
        
        request.onreadystatechange = function() {

            if (this.readyState == 4 && this.status == 200) {
              document.getElementById("content").innerHTML =
              this.responseText;
          }
      };
      request.open('GET', 'q/' + id , false);
      request.send();
      return false
    });


    // AJAX request for when creating a new patient
    $("#nuevo").click( function(){
        const request = new XMLHttpRequest();
        
        request.onreadystatechange = function() {

            if (this.readyState == 4 && this.status == 200) {
              document.getElementById("content").innerHTML =
              this.responseText;
          }
      };
      request.open('GET', 'n', false);
      request.send();
      $('#content > #sidebar').hide();
      return false
    });
 });

