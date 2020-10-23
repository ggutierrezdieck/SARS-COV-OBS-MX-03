
$(document).ready(function() {
    // AJAX request for when clicking on a patient link
    $(".paciente").click( function(){
        id = $(this).attr('id');
        const request = new XMLHttpRequest();
        
        request.onreadystatechange = function() {

            if (this.readyState == 4 && this.status == 200) {
              document.getElementById("content").innerHTML =
              this.responseText;
              

               function  closeMed(){
                if ($(this).parent().parent().find('#id_nombreMedicamento').val() == "" ){
                  if ($("div[id*='medicamento']").length > 1){
                    $(this).closest('#medicamento').remove();
                  } else {
                    alert('No puedes borrar el ultimo medicamento,solo dejalo vacio')
                  }
                } else {
                    alert('No puedes remover un medicamento existente.') 
                }
              };

              // Coning , and clearing medicamento form, when new medicamento is added to allow multiple inputs
              $('#addMed').click(function(){
                $("<hr>").insertBefore("#beforeMedicamento");
                let clone = $("#medicamento").clone()
                // Clearing input values in cloned item
                clone.find('input[type=text]').val('');
                clone.find('input[type=date]').val('');
                //inserting before medicamenteo
                clone.insertBefore("#beforeMedicamento");
                $('.fa-times-circle').click(closeMed);
              });

              // Adding closing functionality xlose icon
              $('.fa-times-circle').click(closeMed);

             
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

