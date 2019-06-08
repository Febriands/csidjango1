$(document).ready(function(){
    var table_certifications = $('#table_certifications').DataTable();

    var load_types = function (){
        $.get("/api/types/", function (result) {
            var rows = [];
            var data = JSON.parse(result.result);

            if(result.done){
                var options = "";
                data.forEach(function(item) {
                    options += `
                        <option value="`+ item.pk +`">`+ item.fields.name +`</option>
                    `;
                });

                $("#certifications_type").html(options);
            }
        });
    }

    load_types();

    var load_table = function (){
        $.get("/api/certifications/", function (result) {
            var rows = [];
            var data = result.result;
            
            if(result.done){
                var i = 1;
                data.forEach(function(item) {
                    var actions = `
                        <button type="button" class="btn btn-primary action-detail" id="`+ item.id +`"><i class="fa fa-search"></i> Detail</button>
                        <button type="button" class="btn btn-danger action-delete" id="`+ item.id +`"><i class="fa fa-trash"></i> Hapus</button>
                    `;

                    var progress = `
                        <div>
                            <p>`+ item.progress_text +`</p>
                            <div class="">
                            <div class="progress progress_md" style="width: 100%;">
                                <div class="progress-bar bg-green" role="progressbar" data-transitiongoal="`+ item.progress +`" aria-valuenow="100" style="width: 100%;"></div>
                            </div>
                            </div>
                        </div>
                    `;

                    rows.push([
                        i++,
                        item.type,
                        item.name,
                        item.applicant,
                        progress,
                        dateConvert(item.created),
                        dateConvert(item.updated),
                        actions,
                    ]);
                });

                table_certifications.clear();
                table_certifications.rows.add(rows);
                table_certifications.draw();
            }
        });
    }

    load_table();

    $( "#form_certifications" ).submit(function( event ) {
        var formData = new FormData(this);
        
        $.ajax({
            type: "POST",
            url: "/api/certifications/save",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                if(result.done == "Failed"){
                    alert("Gagal mengajukan sertifikasi");
                    return false;
                }
            }
        });
    });

    $(document).on("click",".action-detail",function () {
        location.href = '/process/details/'+this.id
    });
    
    $(document).on("click",".action-delete",function () {
        var conf = confirm("Apakah anda yakin akan menghapus data ini?");

        if(conf){
            $.get("/api/certifications/delete?id="+this.id, function (result) {
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