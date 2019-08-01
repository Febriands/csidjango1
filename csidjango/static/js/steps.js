$(document).ready(function(){
    var table_steps = $('#table_steps').DataTable();

    var load_table = function (){
        $.get("/api/steps/"+types_id, function (result) {
            var rows = [];
            var data = JSON.parse(result.result);
            
            if(result.done){
                var i = 1;
                data.forEach(function(item) {
                    var actions = `
                        <button type="button" class="btn btn-primary btn-sm action-detail" id="`+ item.pk +`"><i class="fa fa-search"></i> Detail</button>
                        <button type="button" class="btn btn-warning btn-sm action-edit" id="`+ item.pk +`"><i class="fa fa-edit"></i> Ubah</button>
                        <button type="button" class="btn btn-danger btn-sm action-delete" id="`+ item.pk +`"><i class="fa fa-trash"></i> Hapus</button>
                    `;

                    var status = "";
                    switch (item.fields.step_type) {
                        case 0:
                            status = `<span class="badge bg-blue">Sertifikasi Awal</span>`;
                            break;
                        case 1:
                            status = `<span class="badge bg-orange">Survailen 1</span>`;
                            break;
                        case 2:
                            status = `<span class="badge bg-orange">Survailen 2</span>`;
                            break;
                    }

                    rows.push([
                        "Tahap " + item.fields.order,
                        item.fields.name,
                        status,
                        actions,
                    ]);
                });

                table_steps.clear();
                table_steps.rows.add(rows);
                table_steps.draw();
            }
        });
    }

    load_table();

    $( "#form_steps" ).submit(function( event ) {
        if($('#steps_survailen div').hasClass("checked")){
            $('input[name=survailen]').val(1);
        }else{
            $('input[name=survailen]').val(0);
        }

        var formData = new FormData(this);
        
        $.ajax({
            type: "POST",
            url: "/api/steps/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(result.done == "Failed"){
                    alert("Gagal menambahkan tahap sertifikasi");
                    return false;
                }
            }
        });
    });

    $(document).on("click",".action-detail",function () {
        location.href = '/process/sections/'+this.id
    });

    $(document).on("click",".action-edit",function () {
        $.get("/api/steps/"+types_id+"?id="+this.id, function (result) {
            var data = JSON.parse(result.result);
            $("#steps_id").val(data[0].pk);
            $("#steps_name").val(data[0].fields.name);

            $("#step_type").val(data[0].fields.step_type);

            $(".modal.fade.bs-example-modal-sm").modal('show');
        });
    });
    
    $(document).on("click",".action-delete",function () {
        var conf = confirm("Apakah anda yakin akan menghapus data ini?");

        if(conf){
            $.get("/api/steps/delete?id="+this.id, function (result) {
                if(result.done){
                    alert("Berhasil menghapus data");
                }else{
                    alert("Gagal menghapus data");
                }

                load_table();
            });
        }
    });
});