$(document).ready(function() {
    console.log("hello!")
    console.log("correct question counter: " + counter)

    // For slider questions
    if (item.type == "slider"){

        console.log(item.answer_range[0])
        let slider = document.getElementById("myRange");
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
            if (slider.value >= item.answer_min && slider.value <= item.answer_max){
                $("#question-result").html("<div class='row correct-answer'>Correct!</div>")
                incrementCounter()
            }
            else {
                $("#question-result").html("<div class='row incorrect-answer'>Incorrect!</div>")
                if (item.answer_min == item.answer_max){
                    $("#question-feedback").html("<div class='row feedback'>The correct answer was "+item.answer_min+"</div>")
                }
                else {
                    $("#question-feedback").html("<div class='row feedback'>The correct answer was between "+item.answer_min+" and "+item.answer_max+"</div>")
                }
            }
            $(".check-answer-button").remove()
            enable_next_button()
        });
    }

    // For multiple choice questions
    else if (item.type == "mcq"){
    
        $(".check-answer-button" ).click(function() {

            let radio = $("input[type=radio][name=radio]:checked").val();
            console.log("Radio chosen: " + radio)

             if (radio == item.answer){
                $("#question-result").html("<div class='row correct-answer'>Correct!</div>")
                incrementCounter()
            }
            else {
                $("#question-result").html("<div class='row incorrect-answer'>Incorrect!</div>")
                // $("#question-feedback").html("<div class='row feedback'>The correct answer was answer "+item.answer+".</div>")
                $("#option_" + radio).addClass("incorrect_highlight")

            }
            $("#option_" + item.answer).addClass("correct_highlight")
            $(".check-answer-button").remove()



            enable_next_button()
        });
    }
})

function enable_next_button(){
    $("#next_button").attr("disabled", false)
}

function incrementCounter(){
    let data_to_save = {"counter": counter}
    console.log("data_to_save: " + JSON.stringify(data_to_save))

    $.ajax({
        type: "POST",
        url: "/check_answer",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_to_save),
        success: function(results){
            console.log("Incremented Counter")            
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    }) 
}
