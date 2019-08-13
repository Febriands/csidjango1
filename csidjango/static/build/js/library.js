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

var form_builder = function(field, type, label, value, tooltip, options=null){
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
    `;


    if(type === 0 || type === 1) {
        form += `<input type="` + tmp_type + `" name="` + field + `" required="required" class="form-control col-md-12 col-xs-12" value="` + value + `">`;
    }else if(type === 2){
        options.forEach(function (item) {
            form += `
                <div class="radio">
                    <label>
                        <input type="radio" value="` + item + `" name="` + field.toString() + `"> `+ item +`
                    </label>
                </div>
            `;
        });
    }else if(type === 3){
        form += `
            <select class="form-control col-md-12 col-xs-12" name="`+ field.toString() +`">
        `;

        options.forEach(function (item) {
            form += `
                <option value="`+ item +`">`+ item +`</option>
            `;
        });

        form += `
            </select>
        `;
    }

    form += tooltip + `
            </div>
        `;

    return form;
}

var docs_form_builder = function(field, label, current, tooltip){
    var path = "/media/docs/"+current;
    current = current ? `<a href="` + path +`"><b>` + current + `</b></a>` : "<i>belum ada berkas</i>";
    tooltip = tooltip ? "<small>*) "+ tooltip +"</small>" : "";

    var form = `
        <div class="form-group">
            <label class="control-label">
                `+ label +`
            </label>
            <p>
                Saat ini: `+ current +`
            </p>
            <input type="file" name="`+ field +`" class="form-control col-md-12 col-xs-12">
            ` + tooltip + `
        </div>
    `;

    return form;
}