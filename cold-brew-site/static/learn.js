
// Code for cart pages (three draggable elements and a droppable cart)

// Things that work: 
	// Images revert when they're invalid and update the state of the cart
	// The correct image, draggable2, stays in place in the cart

// TODO:

  // Randomize/hardcode different correct images

  $(document).ready(function(){

    // Code for 3 page draggable elements

    $( "#draggable1" ).draggable({ revert: "invalid" });
    $( "#draggable2" ).draggable({ revert: "invalid" });
    $( "#draggable3" ).draggable({ revert: "invalid" });
    
    // Shopping cart accepting code
      // I spent WAY too long figuring this out before realizing "accept:" isn't ideal.
        // Our savior: https://stackoverflow.com/questions/10842623/jquery-drag-revert-on-drop-to-specific-div
    
    $( "#droppable" ).droppable({
      classes: {
        // "ui-droppable-active": "ui-state-active",
        "ui-droppable-hover": "ui-state-hover"
      },

      drop: function( event, ui ) {
        if(item["accepting"].includes(ui.draggable.attr("img_id"))){
          enable_next_button()
          $("#hint_text").html(item["accept_hint"])
        }
        else{
          // Revert image back to original position and show reject message
          ui.draggable.draggable('option','revert',true);
          $("#hint_text").html(item["reject_hint"])
        }

        // If we want to add additional properties to the cart:

        // $( this )
        //   .addClass( "ui-state-highlight" )
        //   .find( "p" )
        //     .html( "Dropped!" );
      }
    });
})



$(document).ready(function() {
    //console.log(item.images.items())
    //console.log("hello!")
    //console.log(item.answer_range[0])
    //console.log("counter: " + counter)
    let slider = document.getElementById("learnRange1");
    let output = document.getElementById("demo");
    output.innerHTML = slider.value; // Display the default slider value

    const min = slider.min
    const max = slider.max
    const value = slider.value

    slider.style.background = `linear-gradient(to right, #900C3F 0%, #900C3F ${(value-min)/(max-min)*100}%, #dedcde ${(value-min)/(max-min)*100}%, #dedcde 100%)`

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
      output.innerHTML = this.value;
      this.style.background = `linear-gradient(to right, #900C3F 0%, #900C3F ${(this.value-this.min)/(this.max-this.min)*100}%, #dedcde ${(this.value-this.min)/(this.max-this.min)*100}%, #dedcde 100%)`
    }


    $( ".check-answer-button" ).click(function() {
        if (slider.value == item.answer1){
            $("#hint_text").html("<div class='row'>"+item.accept_hint+"</div>")
            //$("#hint_text").html("")
            enable_next_button()
        }
        else {
            $("#hint_text").html("<div class='row'>"+item.reject_hint+"</div>")
            //$("#hint_text").html("")
        }
      });
})



function enable_next_button(){
    $("#next_button").attr("disabled", false)
}