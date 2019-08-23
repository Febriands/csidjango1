var dateConvert = function(timestamp, hms=false){
    timestamp = timestamp * 1000;

    var date = new Date(timestamp);

    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();

    month = month < 10 ? '0'+month : month;
    day = day < 10 ? '0'+day : day;
    hour = hour < 10 ? '0'+hour : hour;
    minutes = minutes < 10 ? '0'+minutes : minutes;
    seconds = seconds < 10 ? '0'+seconds : seconds;

    return hms ? year+'-'+month+'-'+day+' '+hour+':'+minutes+':'+seconds : year+'-'+month+'-'+day;
}

var form_builder = function(field, type, label, value, tooltip, options=null, steps_id){
    var tmp_type = "text";
    switch(type){
        case 0:
            tmp_type = "number";
            break;
        case 1:
            tmp_type = "text";
            break;
    }

    value = value ? value : "";
    tooltip = tooltip ? "<br/><small>*) "+ tooltip +"</small>" : "";

    var form = `
        <div class="form-group">
            <label class="control-label">
                ` + label + `
            </label>
            | <a href="#" id="`+ steps_id+"-"+field +`" class="reset-form" style="opacity: 0.5;">Reset</a>
    `;


    if(type === 0 || type === 1) {
        form += `<input type="` + tmp_type + `" name="` + field + `" class="form-control col-md-12 col-xs-12" value="` + value + `">`;
    }else if(type === 2){
        options.forEach(function (item) {
            var selected = "";

            if(value == item){
                selected = "checked";
            }

            form += `
                <div class="radio">
                    <label>
                        <input type="radio" value="` + item + `" name="` + field.toString() + `" `+ selected +`> `+ item +`
                    </label>
                </div>
            `;
        });
    }else if(type === 3){
        form += `
            <select class="form-control col-md-12 col-xs-12" name="`+ field.toString() +`">
        `;

        options.forEach(function (item) {
            var selected = "";

            if(value == item){
                selected = "selected";
            }

            form += `
                <option value="`+ item +`" `+ selected +`>`+ item +`</option>
            `;
        });

        form += `
            </select>
        `;
    }else if(type === 4){
        var value_list = value.split(",");
        options.forEach(function (item) {
            var selected = "";

            if(value_list.includes(item)){
                selected = "checked";
            }

            form += `
                <div class="checkbox">
                    <label>
                        <input type="checkbox" name="`+ field.toString() +`" value="`+ item +`" `+ selected +`> `+ item +`
                    </label>
                </div>
            `;
        });
    }

    form += tooltip + `
            </div>
        `;

    return form;
}

var docs_form_builder = function(field, label, current, tooltip, steps_id){
    var files = "";
    if(current){
        var current_file_list = current.split("|");
        var file_list = [];

        current_file_list.forEach(function (item) {
            var path = "/media/docs/"+item;
            file_list.push(`<a href="` + path +`" download><b>` + item + `</b></a>`);
        });

        files = file_list.join("<br/>")
    }else{
        files = "<i>belum ada berkas</i>";
    }

    tooltip = tooltip ? "<small>*) "+ tooltip +"</small>" : "";

    var form = `
        <div class="form-group">
            <label class="control-label">
                `+ label +`
            </label>
            | <a href="#" id="`+ steps_id+"-"+ field +`" class="reset-doc" style="opacity: 0.5;">Reset</a>
            <p>
                Saat ini: <br/>`+ files +`
            </p>
            <input type="file" name="`+ field +`" class="form-control col-md-12 col-xs-12" multiple>
            ` + tooltip + `
        </div>
    `;

    return form;
}