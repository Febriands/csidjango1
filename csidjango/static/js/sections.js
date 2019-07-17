$(document).ready(function(){
    var table_sections = $('#table_sections').DataTable();

    var load_table = function (){
        $.get("/api/sections/"+steps_id, function (result) {
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

                    rows.push([
                        i++,
                        item.fields.title,
                        item.fields.description,
                        actions,
                    ]);
                });

                table_sections.clear();
                table_sections.rows.add(rows);
                table_sections.draw();
            }
        });
    }

    load_table();

    $( "#form_sections" ).submit(function( event ) {
        var formData = new FormData(this);

        $.ajax({
            type: "POST",
            url: "/api/sections/save",
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
        $.get("/api/sections/"+steps_id+"?id="+this.id, function (result) {
            var data = JSON.parse(result.result);
            $("#sections_id").val(data[0].pk);
            $("#sections_title").val(data[0].fields.title);
            $("#sections_description").val(data[0].fields.description);

            $(".modal.fade.bs-example-modal-sm").modal('show');
        });
    });

    $(document).on("click",".action-delete",function () {
        var conf = confirm("Apakah anda yakin akan menghapus data ini?");

        if(conf){
            $.get("/api/sections/delete?id="+this.id, function (result) {
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