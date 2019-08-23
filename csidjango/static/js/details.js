$(document).ready(function(){
    $('#menu-'+active).addClass('active');
    $('#'+active).addClass('active');

    var load_steps = function (steps_id){
        $.get("/api/details/"+steps_id, function (result) {
            var sections = result.result.sections;
            var details = result.result.details;
            var docs = result.result.docs;
            var forms = [];
            var docs_forms = [];
            var form_fields = "";
            var doc_fields = "";

            Object.keys(sections).forEach(function (key) {
                forms[key] = "";
                docs_forms[key] = "";
            });

            details.forEach(function(item) {
                forms[item.section] += form_builder(item.field, item.type, item.name, item.value, item.tooltip, item.options.split(","), steps_id);
            });

            docs.forEach(function(item) {
                docs_forms[item.section] += docs_form_builder(item.field, item.name, item.path, item.tooltip, steps_id);
            });

            Object.keys(sections).forEach(function (key) {
                form_fields += `<h4><b>`+ sections[key].title +`</b></h4><p>`+ sections[key].description +`</p>`;
                form_fields += forms[key];

                doc_fields += `<h4><b>`+ sections[key].title +`</b></h4><p>`+ sections[key].description +`</p>`;
                doc_fields += docs_forms[key];
            });

            $('#form_details_'+steps_id).html(form_fields);
            $('#form_docs_'+steps_id).html(doc_fields);
        });
    }

    load_steps(active);

    $(document).on("submit",".form-steps",function (event) {
        event.preventDefault(event);
        var formData = new FormData(this);

        $.ajax({
            type: "POST",
            url: "/api/details/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(!result.done){
                    alert("Gagal menyimpan data");
                    return false;
                }else{
                    alert("Berhasil menyimpan data");
                    location.reload();
                }
            }
        });
    });

    $(document).on("submit",".form-steps-docs",function (event){
        event.preventDefault(event);
        var formData = new FormData(this);

        $.ajax({
            type: "POST",
            url: "/api/details/docs/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(!result.done){
                    alert("Gagal menyimpan data");
                    return false;
                }else{
                    alert("Berhasil menyimpan data");
                    location.reload();
                }
            }
        });
    });

    $(document).on("click",".steps-menu-item",function () {
        var step = this.id.split('-')[1];
        load_steps(step);
    });

    $(document).on("click",".reset-form",function () {
        var detail = this.id.split("-");

        $.ajax({
            type: "GET",
            url: "/api/details/form/reset/"+detail[0]+"/"+detail[1],
            success: function (result) {
                if(!result.done){
                    alert("Gagal mengatur ulang data");
                    return false;
                }else{
                    alert("Berhasil mengatur ulang data");
                    location.reload();
                    return false;
                }
            }
        });
    });

    $(document).on("click",".reset-doc",function () {
        var detail = this.id.split("-");

        $.ajax({
            type: "GET",
            url: "/api/details/doc/reset/"+detail[0]+"/"+detail[1],
            success: function (result) {
                if(!result.done){
                    alert("Gagal mengatur ulang data");
                    return false;
                }else{
                    alert("Berhasil mengatur ulang data");
                    location.reload();
                    return false;
                }
            }
        });
    });
});