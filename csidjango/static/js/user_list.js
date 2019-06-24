$(document).ready(function(){
    var table_user_list = $('#table_user_list').DataTable();

    var load_table = function (){
        $.get("/api/user_list/", function (result) {
            var rows = [];
            var data = JSON.parse(result.result);
            
            if(result.done){
                var i = 1;
                data.forEach(function(item) {
                    var actions = `
                        <button type="button" class="btn btn-primary action-detail" id="`+ item.pk +`"><i class="fa fa-search"></i> Profile</button>
                        <button type="button" class="btn btn-warning action-edit" id="`+ item.pk +`"><i class="fa fa-edit"></i> Ubah</button>
                        <button type="button" class="btn btn-danger action-delete" id="`+ item.pk +`"><i class="fa fa-trash"></i> Hapus</button>
                    `;

                    rows.push([
                        i++,
                        item.fields.name,
                        actions,
                    ]);
                });

                table_user_list.clear();
                table_user_list.rows.add(rows);
                table_user_list.draw();
            }
        });
    }

    load_table();

    $( "#form_user_list" ).submit(function( event ) {
        var formData = new FormData(this);
        
        $.ajax({
            type: "POST",
            url: "/api/user_list/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(result.done == "Failed"){
                    alert("Gagal menambahkan user");
                    return false;
                }
            }
        });
    });

    $(document).on("click",".action-detail",function () {
        location.href = '/accounts/profile/'+this.id
    });

    $(document).on("click",".action-edit",function () {
        $.get("/api/user_list/?id="+this.id, function (result) {
            var data = JSON.parse(result.result);
            $("#user_list_id").val(data[0].pk);
            $("#user_list_name").val(data[0].fields.name);

            $(".modal.fade.bs-example-modal-sm").modal('show');
        });
    });
    
    $(document).on("click",".action-delete",function () {
        var conf = confirm("Apakah anda yakin akan menghapus data ini?");

        if(conf){
            $.get("/api/user_list/delete?id="+this.id, function (result) {
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