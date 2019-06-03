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
                        <button type="button" class="btn btn-primary action-detail" id="`+ item.pk +`"><i class="fa fa-search"></i> Detail</button>
                        <button type="button" class="btn btn-warning action-edit" id="`+ item.pk +`"><i class="fa fa-edit"></i> Ubah</button>
                        <button type="button" class="btn btn-danger action-delete" id="`+ item.pk +`"><i class="fa fa-trash"></i> Hapus</button>
                    `;

                    rows.push([
                        "Tahap " + item.fields.order,
                        item.fields.name,
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
        location.href = '/process/forms/'+this.id
    });

    $(document).on("click",".action-edit",function () {
        $.get("/api/steps/"+types_id+"?id="+this.id, function (result) {
            var data = JSON.parse(result.result);
            $("#steps_id").val(data[0].pk);
            $("#steps_name").val(data[0].fields.name);

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