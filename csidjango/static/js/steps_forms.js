$(document).ready(function(){
    var table_forms = $('#table_forms').DataTable();
    var table_documents = $('#table_documents').DataTable();
    $('#option_field').hide();

    // FORMS

    var load_table_form = function (){
        $.get("/api/forms/"+sections_id, function (result) {
            var rows = [];
            var data = JSON.parse(result.result);
            
            if(result.done){
                var i = 1;
                data.forEach(function(item) {
                    var actions = `
                        <button type="button" class="btn btn-warning btn-sm action-edit form" id="`+ item.pk +`"><i class="fa fa-edit"></i> Ubah</button>
                        <button type="button" class="btn btn-danger btn-sm action-delete form" id="`+ item.pk +`"><i class="fa fa-trash"></i> Hapus</button>
                    `;

                    var type = "";
                    switch(item.fields.form_type){
                        case 0:
                            type = "Angka";
                            break;
                        case 1:
                            type = "Teks";
                            break;
                        case 2:
                            type = "Radio";
                            break;
                        case 3:
                            type = "Dropdown";
                            break;
                        default:
                            type = "Angka";
                            break;
                    }

                    rows.push([
                        i++,
                        item.fields.name,
                        type,
                        item.fields.options,
                        item.fields.tooltip,
                        actions,
                    ]);
                });

                table_forms.clear();
                table_forms.rows.add(rows);
                table_forms.draw();
            }
        });
    }

    load_table_form();

    $( "#form_steps_forms" ).submit(function( event ) {
        $("#form_type").prop('disabled', false);
        var formData = new FormData(this);
        
        $.ajax({
            type: "POST",
            url: "/api/forms/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(result.done == "Failed"){
                    alert("Gagal menambahkan form");
                    return false;
                }
            }
        });
    });

    $(document).on("click",".action-detail.form",function () {
        location.href = '/process/forms/'+this.id
    });

    $(document).on("click",".action-edit.form",function () {
        $.get("/api/forms/"+sections_id+"?id="+this.id, function (result) {
            var data = JSON.parse(result.result);
            $("#forms_id").val(data[0].pk);
            $("#steps_forms_name").val(data[0].fields.name);
            $("#steps_forms_tooltip").val(data[0].fields.tooltip);
            $("#form_type option[value="+data[0].fields.form_type+"]").prop('selected', true);
            $("#form_type").prop('disabled', true);

            if(data[0].fields.options){
                $('#option_field').show();
                $("#steps_forms_options").val(data[0].fields.options);
            }

            $("#modal_form").modal('show');
        });
    });
    
    $(document).on("click",".action-delete.form",function () {
        var conf = confirm("Apakah anda yakin akan menghapus data ini?");

        if(conf){
            $.get("/api/forms/delete?id="+this.id, function (result) {
                if(result.done){
                    alert("Berhasil menghapus data");
                }else{
                    alert("Gagal menghapus data");
                }

                load_table_form();
            });
        }
    });

    $("#addForm").click(function (){
        $("#form_type").prop('disabled', false);
    });

    // DOCUMENTS
    
    var load_table_documents = function (){
        $.get("/api/docs/"+sections_id, function (result) {
            var rows = [];
            var data = JSON.parse(result.result);
            
            if(result.done){
                var i = 1;
                data.forEach(function(item) {
                    var actions = `
                        <button type="button" class="btn btn-warning action-edit document" id="`+ item.pk +`"><i class="fa fa-edit"></i> Ubah</button>
                        <button type="button" class="btn btn-danger action-delete document" id="`+ item.pk +`"><i class="fa fa-trash"></i> Hapus</button>
                    `;

                    rows.push([
                        i++,
                        item.fields.name,
                        item.fields.tooltip,
                        actions,
                    ]);
                });

                table_documents.clear();
                table_documents.rows.add(rows);
                table_documents.draw();
            }
        });
    }

    load_table_documents();

    $( "#form_offline_documents" ).submit(function( event ) {
        var formData = new FormData(this);
        
        $.ajax({
            type: "POST",
            url: "/api/docs/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(result.done == "Failed"){
                    alert("Gagal menambahkan dokumen");
                    return false;
                }
            }
        });
    });

    $(document).on("click",".action-edit.document",function () {
        $.get("/api/docs/"+sections_id+"?id="+this.id, function (result) {
            console.log(result);
            var data = JSON.parse(result.result);
            $("#document_id").val(data[0].pk);
            $("#offline_documents_name").val(data[0].fields.name);
            $("#offline_documents_tooltip").val(data[0].fields.tooltip);

            $("#modal_document").modal('show');
        });
    });
    
    $(document).on("click",".action-delete.document",function () {
        var conf = confirm("Apakah anda yakin akan menghapus data ini?");

        if(conf){
            $.get("/api/docs/delete?id="+this.id, function (result) {
                if(result.done){
                    alert("Berhasil menghapus data");
                }else{
                    alert("Gagal menghapus data");
                }

                load_table_documents();
            });
        }
    });

    $(document).on("change","#form_type",function () {
        var value = $('#form_type').val();
        if(value === "2" || value === "3"){
            $('#option_field').show();
        }else{
            $('#option_field').hide();
        }
    });
});