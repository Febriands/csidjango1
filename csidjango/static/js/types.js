$(document).ready(function(){
    var table_types = $('#table_types').DataTable();

    var load_table = function (){
        $.get("/api/types/", function (result) {
            var rows = [];
            var data = JSON.parse(result.result);
            
            if(result.done){
                var i = 1;
                data.forEach(function(item) {
                    var actions = `
                        <button type="button" class="btn btn-primary action-detail" id="`+ item.pk +`"><i class="fa fa-search"></i> Tahap</button>
                        <button type="button" class="btn btn-warning action-edit" id="`+ item.pk +`"><i class="fa fa-edit"></i> Edit</button>
                        <button type="button" class="btn btn-danger action-delete" id="`+ item.pk +`"><i class="fa fa-trash"></i> Delete</button>
                    `;

                    rows.push([
                        i++,
                        item.fields.name,
                        actions,
                    ]);
                });

                table_types.clear();
                table_types.rows.add(rows);
                table_types.draw();
            }
        });
    }

    load_table();

    $( "#form_types" ).submit(function( event ) {
        var formData = new FormData(this);
        
        $.ajax({
            type: "POST",
            url: "/api/types/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(result.done == "Failed"){
                    alert("Gagal menambahkan jenis sertifikasi");
                    return false;
                }
            }
        });
    });

    $(document).on("click",".action-detail",function () {
        location.href = '/process/steps/'+this.id
    });

    $(document).on("click",".action-edit",function () {
        $.get("/api/types/?id="+this.id, function (result) {
            var data = JSON.parse(result.result);
            $("#types_id").val(data[0].pk);
            $("#types_name").val(data[0].fields.name);

            $(".modal.fade.bs-example-modal-sm").modal('show');
        });
    });
    
    $(document).on("click",".action-delete",function () {
        var conf = confirm("Apakah anda yakin akan menghapus data ini?");

        if(conf){
            $.get("/api/types/delete?id="+this.id, function (result) {
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