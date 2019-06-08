$(document).ready(function(){
    $('#menu-'+active).addClass('active');
    $('#'+active).addClass('active');

    var load_steps = function (steps_id){
        $.get("/api/details/"+steps_id, function (result) {
            var details = result.result.details;
            var docs = result.result.docs;
            var forms = "";
            var docs_forms = "";

            details.forEach(function(item) {
                forms += form_builder(item.field, item.type, item.name, item.value);
            });

            docs.forEach(function(item) {
                docs_forms += docs_form_builder(item.field, item.name, item.path);
            });

            $('#form_details_'+steps_id).html(forms);
            $('#form_docs_'+steps_id).html(docs_forms);
        });
    }

    load_steps(active);

    $( ".form-steps" ).submit(function( event ) {
        var formData = new FormData(this);

        $.ajax({
            type: "POST",
            url: "/api/details/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(result.done == "Failed"){
                    alert("Gagal menyimpan data");
                    return false;
                }
            }
        });
    });

    $( ".form-steps-docs" ).submit(function( event ) {
        var formData = new FormData(this);

        $.ajax({
            type: "POST",
            url: "/api/details/docs/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(result.done == "Failed"){
                    alert("Gagal menyimpan data");
                    return false;
                }
            }
        });
    });

    $(document).on("click",".steps-menu-item",function () {
        var step = this.id.split('-')[1];
        load_steps(step);
    });
});